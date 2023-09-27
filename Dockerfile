FROM python:3.11
RUN mkdir /online_attach_app
WORKDIR /online_attach_app
ADD . /online_attach_app/
RUN pip install -r requirments.txt
