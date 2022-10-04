from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('01.index.html')

@app.route('/menu', methods=['GET','POST'])
def menu():
    if request.method == 'GET':
        return render_template('02.Menu.html')
    else:
        return render_template('03.Menu_res.html')

if __name__ == '__main__':
    app.run(debug=True)