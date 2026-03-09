
FROM python:3.10.20-alpine3.22
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
CMD ["python","app.py"]
