FROM parker20121/joshua:6.0.1
MAINTAINER Matt Parker <matthew.parker@l-3com.com>

LABEL description="Wraps Joshua machine translation tool with Joshua web service"
LABEL version="6.0.1"

RUN yum install -y python-setuptools python-devel.x86_64 libffi-devel openssl-devel nc
RUN easy_install pip

ADD https://bootstrap.pypa.io/get-pip.py /opt/pip/get-pip.py
RUN python /opt/pip/get-pip.py

RUN pip install pyopenssl ndg-httpsclient pyasn1 django==1.8 markdown defusedxml lxml python-dateutil pyyaml django-tastypie

RUN git clone https://github.com/annieweng/Joshua-web.git
COPY Joshua-web /opt/joshua-web

# COPY /opt/joshua-web/patch/tastypie/utils/mime.py $PYTHON/dist-packages/tastype/utils/mime.py

WORKDIR /opt/joshua-web

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

