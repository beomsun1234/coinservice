FROM python:3.9-alpine
RUN mkdir /coinservice
ADD . /coinservice
WORKDIR /coinservice

RUN pip3 --trusted-host pypi.org --trusted-host files.pythonhosted.org install Django
RUN pip3 --trusted-host pypi.org --trusted-host files.pythonhosted.org install bs4

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]