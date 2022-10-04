from flask import Flask, render_template, request
from extra import extra_bp
import os

app = Flask(__name__)
app.secret_key = 'qwert12345'   # session, flash 사용하기 위해 설정
app.register_blueprint(extra_bp, url_prefix='/extra')

@app.route('/')
def home():
    menu = {'home':1, 'menu':0, 'map':0, 'extra':0}
    return render_template('index.html', menu=menu)

@app.route('/menu', methods=['GET','POST'])
def menu():
    menu = {'home':0, 'menu':1, 'map':0, 'extra':0}
    if request.method == 'GET':
        languages = [
            {'disp':'영어', 'val':'en'},
            {'disp':'일어', 'val':'jp'},
            {'disp':'중국어', 'val':'cn'},
            {'disp':'프랑스어', 'val':'fr'},
            {'disp':'스페인어', 'val':'es'}
        ]
        return render_template('menu.html', menu=menu,
                                options=languages)   # 서버에서 클라이언트로 정보 전달
    else:
        # 사용자가 입력한 정보를 서버가 읽음
        index = request.form['index']
        lang = request.form['lang']
        lyrics = request.form['lyrics']
        #print(lang, '\n', index, '\n', lyrics, sep='')
        # 사용자가 입력한 파일을 읽어서 upload 디렉토리에 저장
        f_image = request.files['image']
        fname = f_image.filename                # 사용자가 입력한 파일 이름
        filename = os.path.join(app.static_folder, 'upload/') + fname
        f_image.save(filename)

        # 모델 실행후 결과를 돌려줌
        result = '독수리 (73.52%)'
        mtime = int(os.stat(filename).st_mtime)
        return render_template('menu_res.html', result=result, menu=menu,
                                fname=fname, mtime=mtime)

@app.route('/map')
def map():
    menu = {'home':0, 'menu':0, 'map':1, 'extra':0}
    filename = os.path.join(app.static_folder, 'img/광주시_주요관공서.html')
    mtime = int(os.stat(filename).st_mtime)
    return render_template('map.html', menu=menu, mtime=mtime)

if __name__ == '__main__':
    #app.run(debug=True)                    # 로컬에서의 접속만 가능
    app.run(host='0.0.0.0', debug=True)     # 모든 호스트에서 접속 가능