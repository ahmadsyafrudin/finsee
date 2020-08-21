FROM python:3.8

COPY ./src/finsee /opt/python/finsee
WORKDIR /opt/python/finsee
ENV PYTHONPATH=$PYTHONPATH:/opt/python
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r  /tmp/requirements.txt
RUN pip install uwsgi
EXPOSE 8000
RUN python manage.py collectstatic
CMD uwsgi --http "0.0.0.0:8000" --module finsee.app.wsgi --master --processes 2 --threads 2
