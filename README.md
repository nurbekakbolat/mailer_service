# mailer_service
To create docker image follow:

docker build -t mailer-service .

docker run -d -p 8000:8000 mailer-service

python -m pytest test_main.py
