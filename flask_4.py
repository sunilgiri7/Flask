from flask import Flask
app = Flask(__name__)

@app.route("/sub/<int:num,num2>")
def sub(num,num2):
    return str(num+num2)
print(sub(10,10))

if __name__=="__main__":
    app.run(debug=True)