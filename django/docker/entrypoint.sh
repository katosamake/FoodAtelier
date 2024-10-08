#!/bin/sh
cd src
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
# 環境変数のDEBUGの値がTrueの時はrunserverを、Falseの時はgunicornを実行します
if [ $DEBUG = "True" ]
then
    python manage.py runserver 0.0.0.0:8000
else
    # gunicornを起動させる時はプロジェクト名を指定します
    gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
fi