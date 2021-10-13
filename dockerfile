FROM python:3.6
MAINTAINER Dhinakaran
WORKDIR /app
RUN pip install -r requirements.txt
ADD python-exercise/twitter.py /app/twitter.py
CMD ["/app/twitter.py"]
ENTRYPOINT ["python"]
