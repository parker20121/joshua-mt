FROM parker20121/joshua:6.0.1
MAINTAINER Matt Parker <matthew.parker@l-3com.com>

LABEL Description="Wraps Joshua machine translation tool with Joshua web service"

RUN yum install -y python-setuptools python2.7-dev libffi-devel libssl-dev
RUN easy_install pip

ADD https://bootstrap.pypa.io/get-pip.py /opt/pip/get-pip.py
RUN python /opt/pip/get-pip.py

RUN pip install pyopenssl ndg-httpsclient pyasn1
RUN pip install django==1.8
RUN pip install markdown defusedxml
RUN pip install lxml
RUN pip install dateutil
RUN pip install pyyaml
RUN pip django-tastypie

ADD ../joshua-web/Joshua /opt/joshua-web

WORKDIR /opt/joshua-web

EXPOSE 80

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:80"]

