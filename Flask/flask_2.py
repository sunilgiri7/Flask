###Building Url Dynamically
from flask import Flask,redirect,url_for
app= Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to my code'


@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The Result is PASSED</h1></body</html"


@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is"+str(score)



@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))


# @app.route('/fail/<int:score>')
# def fail(score):
#     return "the person has failed and the marks is"+str(score)


if __name__=='__main__':
    app.run(debug=True)