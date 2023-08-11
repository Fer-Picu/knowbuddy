from python:3.11.4
RUN mkdir -p /opt/app/ && cd /opt/app
WORKDIR /opt/app/knowbuddy
COPY manage.py ./
COPY knowbuddy ./knowbuddy
COPY requeriments.txt ./
RUN pip install --force-reinstall --no-cache-dir -r requeriments.txt
EXPOSE 8000
CMD [ "python", "manage.py" ,"runserver" , "0.0.0.0:8000"]
