from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
        <h1>Hello World!!!</h1>
        <hr>
        <p>디버그 모드에서는 변경 사항이 발생하면 자동적으로 서버가 재실행됩니다.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)