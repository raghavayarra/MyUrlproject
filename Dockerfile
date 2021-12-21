#initialize a base image
FROM  python:3.9-alpine
#define the working directory
WORKDIR ./MyUrlproject
#adding docker file
COPY * ./
#run pip to install the requirements
RUN pip install -r requirements.txt
#define the command to start the computer
CMD ["python", "app.py"]
