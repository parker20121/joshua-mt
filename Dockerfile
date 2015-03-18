FROM centos:7

MAINTAINER Matt Parker <matthew.parker at l-3com.com>

ENV container docker

# Enable Universal package repository
RUN yum install --assumeyes boost-devel gcc-c++ zlib-devel nano ant wget

ADD http://joshua-decoder.org/releases/6.0/ /opt

RUN tar -xf /opt/joshua-v6.0.1.tgz --dir /opt
ENV JOSHUA=/opt/joshua-v6.0.1

WORKINGDIR ${JOSHUA}
RUN ant kenlm

PORT 5674