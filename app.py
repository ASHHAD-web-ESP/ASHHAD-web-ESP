from flask import Flask,request, url_for, redirect, render_template, jsonify
from flask_socketio import SocketIO
from flask_executor import Executor
import pandas as pd
import json


app = Flask(__name__)
socketio = SocketIO(app)
thread = None

@app.route('/')
def home():
    return render_template("home.html")


@socketio.on("response_demo")
def background_task_func():
    """Example of how to send server generated events to clients."""

    socketio.sleep(5)
    print("send")
   
    data = {'Name': ['Tom', 'Joseph', 'Krish', 'John','Shadz'], 'Age': [20, 21, 19, 18,36]} 

    data_2= pd.DataFrame(data)
    
    df_json=data_2.to_json(orient='records')
    result = {"objects": json.loads(df_json)}
    socketio.emit('my_response',result, broadcast=True)


if __name__ == '__main__':
    app.run(debug=True)
    executor = Executor(app)
    socketio.run(app)
