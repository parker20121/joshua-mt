FROM parker20121/xdata-hive-cli:cdh53

MAINTAINER Matt Parker <matthew.parker@l-3com.com>

RUN yum install --assumeyes boost-devel gcc-c++ zlib-devel nano ant wget

WORKINGDIR /opt

ADD http://joshua-decoder.org/releases/6.0/

RUN tar -xf joshua-v6.0.1.tgz
ENV JOSHUA=/opt/joshua-v6.0.1

WORKINGDIR ${JOSHUA}
RUN ant kenlm

PORT 5674