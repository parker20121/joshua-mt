FROM centos:7
MAINTAINER Matt Parker <matthew.parker at l-3com.com>

ENV container docker

# Enable Universal package repository
RUN yum update
RUN yum install --assumeyes boost-devel gcc-c++ zlib-devel nano ant wget tar make

# Install Joshua software
WORKINGDIR /opt
RUN wget http://cs.jhu.edu/~post/files/joshua-v6.0.1.tgz
RUN tar -xf joshua-v6.0.1.tgz --dir /opt
ENV JOSHUA=/opt/joshua-v6.0.1
ENV JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.el7_0.x86_64

# Compile ken lib and link to joshua lib folder
WORKINGDIR ${JOSHUA}
RUN ant kenlm install
# RUN ln -s /lib/libken.so ${JOSHUA}/lib/libken.so

# Open server port
PORT 5674