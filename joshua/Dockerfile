FROM centos:7
MAINTAINER Matt Parker <matt.parker at giantoak.com>

ENV container docker

# Enable Universal package repository
RUN yum update
RUN yum install --assumeyes boost-devel gcc-c++ zlib-devel nano ant wget tar make

# Install Joshua software
WORKDIR /opt
RUN wget -q http://cs.jhu.edu/~post/files/joshua-v6.0.1.tgz
RUN tar -xf joshua-v6.0.1.tgz --dir /opt

# Setup Joshua environment variables
ENV JOSHUA=/opt/joshua-v6.0.1
ENV JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.101-2.6.6.1.el7_2.x86_64
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8

# Compile ken lib and link to joshua lib folder
WORKDIR $JOSHUA
RUN ant kenlm
RUN rm /opt/joshua-v6.0.1.tgz

# Open server port
EXPOSE 5674
