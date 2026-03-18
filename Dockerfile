#使用官方轻量级Python镜像
FROM python:3.9-slim
#设置容器内部的工作目录
WORKDIR /app
#将当前目录下的app.py复制到容器的/app目录下
COPY app.py .
#安装Flask依赖
RUN pip install flask
# 告诉Docker容器启动时运行这个命令
CMD ["python", "app.py"]
