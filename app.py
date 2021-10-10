from flask import Flask,request, url_for, redirect, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)