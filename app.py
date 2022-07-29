from flask import Flask, request, render_template, url_for, redirect
import face
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/naver')
def naver():
    return '나는 네이비다'


@app.route('/sagi')
def myimage():
    return render_template("myimage.html")


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        # 여기에 imglink 데이터가 넘어와서
        # face.py 에 있는 기능이 동작이 되면
        # 될 것 같은데....
        imglink = request.form['imglink']
        face.mk_face(imglink)
        return redirect(url_for('myimage'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)