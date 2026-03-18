# app.py
from flask import Flask
import os

app = Flask(__name__)
@app.route('/')
def hello():
  #获取系统环境信息，证明这是在Docker里运行
  return "<h1>Hello DevOps from Vancouver!</h1><p>Running on Docker Container!</p>"

if __name__ == "__main__":
  #监听所有IP的5000端口
  app.run(host='0.0.0.0', port=5000)
