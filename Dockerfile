# base image
FROM python:3.10


# port where the app will run
EXPOSE 5050


# move into the folder where the Flask app will go
WORKDIR /app


# copy requirements.txt into working directory
COPY requirements.txt .


# install required libraries specified in requirements.txt
RUN pip install -r requirements.txt


# copy from your system into the images' file system
# first dot: copy everything in the current folder (local)
# second dot: to the current folder of the image (/app as we specified above)
COPY . .


# commands that should run when the image starts a container
CMD ["flask", "--app", "app.py", "run", "--host", "0.0.0.0", "--port", "5050"]