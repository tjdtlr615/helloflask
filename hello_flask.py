from flask import Flask, render_template #V (view)

app = Flask(__name__) #생성 

#http://localhost:5000/ (일반적인 웹은 80포트씀)
@app.route("/") # @:데코레이터 전처리해주는거
def index():
    return "hello flask"

#http://localhost:5000/hello
@app.route("/hello")
def abc():
    return render_template("hello.html")
if __name__=="__main__" :
    app.run(debug=True)  #debug=True 하면 코드에서 return 수정해도 새로고침하면 바로바로 페이지가 수정됨

