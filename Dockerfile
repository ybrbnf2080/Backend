FROM python:3

WORKDIR /app

RUN y |  apt update #&& y| apt upgrade 


RUN apt install apparmor
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 


CMD [ "python3" , "main.py"]
