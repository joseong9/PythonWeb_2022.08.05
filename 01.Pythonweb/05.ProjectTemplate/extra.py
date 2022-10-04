from flask import Blueprint, render_template, current_app, Response
import os, cv2, time
from datetime import datetime
import mediapipe as mp
import numpy as np

extra_bp = Blueprint('extra_bp', __name__)
menu = {'home':0, 'menu':0, 'map':0, 'extra':1}
faceCascade = cv2.CascadeClassifier('static/data/haarcascade_frontalface_default.xml')
num = 3

@extra_bp.route('/face_detect')
def face_detect():
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M")
    params = {'title':'Image Streaming', 'time': time_string}
    return render_template('extra/face_detect.html', menu=menu, **params)

def face_gen_frames():
    camera = cv2.VideoCapture(0)
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH) 
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)   
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 30
    out = cv2.VideoWriter('static/upload/face_video.avi', fourcc, fps, (int(width), int(height)))
   
    time.sleep(0.2)
    lastTime = time.time()*1000.0

    while True:
        _, image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       
        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)
        delt = time.time()*1000.0 - lastTime
        s = str(int(delt))
        #print (delt," Found {0} faces!".format(len(faces)) )
        lastTime = time.time()*1000.0
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.circle(image, (int(x+w/2), int(y+h/2)), int((w+h)/3), (255, 255, 255), 3)
        cv2.putText(image, s, (10, 25),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        now = datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        cv2.putText(image, timeString, (10, 45),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        #cv2.imshow("Frame", image)
        out.write(image)
      
        key = cv2.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
   
        _, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()
    out.realease()
    cv2.destroyAllWindows()
 
@extra_bp.route('/face_video_feed')
def face_video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(face_gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@extra_bp.route('/hand')
def hand():
    return render_template('extra/hand.html', menu=menu)

@extra_bp.route('/face_mesh')
def face_mesh():
    return render_template('extra/face_mesh.html', menu=menu)

@extra_bp.route('/pose')
def pose():
    return render_template('extra/pose.html', menu=menu)

@extra_bp.route('/holistic')
def holistic():
    return render_template('extra/holistic.html', menu=menu)

@extra_bp.route('/rps')
def rps():
    return render_template('extra/rps.html', menu=menu)

max_num_hands = 1
gesture = {
    0:'fist', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
    6:'six', 7:'rock', 8:'spiderman', 9:'yeah', 10:'ok',
}
rps_gesture = {0:'rock', 5:'paper', 9:'scissors'}

def rps_gen_frames():
    # MediaPipe hands model
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(max_num_hands=max_num_hands,
                           min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Gesture recognition model
    file = np.genfromtxt('static/data/gesture_train.csv', delimiter=',')
    angle = file[:,:-1].astype(np.float32)
    label = file[:, -1].astype(np.float32)
    knn = cv2.ml.KNearest_create()
    knn.train(angle, cv2.ml.ROW_SAMPLE, label)

    camera = cv2.VideoCapture(0)
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH) 
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)   
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 30
    out = cv2.VideoWriter('static/upload/rps_video.avi', fourcc, fps, (int(width), int(height)))
   
    time.sleep(0.2)
    lastTime = time.time()*1000.0

    while True:
        _, img = camera.read()
        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if result.multi_hand_landmarks is not None:
            for res in result.multi_hand_landmarks:
                joint = np.zeros((21, 3))
                for j, lm in enumerate(res.landmark):
                    joint[j] = [lm.x, lm.y, lm.z]

                # Compute angles between joints
                v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
                v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
                v = v2 - v1 # [20,3]
                # Normalize v
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                # Get angle using arccos of dot product
                angle = np.arccos(np.einsum('nt,nt->n',
                    v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                    v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

                angle = np.degrees(angle) # Convert radian to degree

                # Inference gesture
                data = np.array([angle], dtype=np.float32)
                ret, results, neighbours, dist = knn.findNearest(data, 3)
                idx = int(results[0][0])

                # Draw gesture result
                if idx in rps_gesture.keys():
                    cv2.putText(img, text=rps_gesture[idx].upper(), org=(int(res.landmark[0].x * img.shape[1]), 
                                int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                                fontScale=1, color=(255, 255, 255), thickness=2)

                mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

        out.write(img)
      
        key = cv2.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
   
        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()
    out.realease()
    cv2.destroyAllWindows()

@extra_bp.route('/rps_video_feed')
def rps_video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(rps_gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')