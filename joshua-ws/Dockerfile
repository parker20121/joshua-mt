FROM parker20121/joshua
MAINTAINER Matt Parker <matthew.parker@l-3com.com>

RUN yum update -y
RUN yum install -y python
ADD https://bootstrap.pypa.io/get-pip.py /opt/pip
RUN python /opt/pip/get-pip.py

RUN pip install django==1.8
RUN pip install markdown defusedxml
RUN pip install lxml
RUN pip install dateutil
RUN pip install pyyaml
RUN pip django-tastypie

ADD https://github.com/annieweng/Joshua-web/archive/master.zip /opt
RUN mv /opt/master /opt/joshua-web
RUN ln -s /opt/joshua /opt/joshua-web/joshua

EXPOSE 80

