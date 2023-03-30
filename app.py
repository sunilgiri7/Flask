from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

classifier = pipeline('sentiment-analysis')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        label = classifier(text)[0]['label']
        return render_template('index.html', output=label)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
