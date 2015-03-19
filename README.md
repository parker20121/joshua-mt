# joshua-mt

Dockerfile to create an Centos 7 image with Joshua 
machine translation software 

	http://joshua-decoder.org/

This downloads and compiles the Joshua software, storing
the results on an Centos 7 image.

To create the docker image, run the following command:

	docker build - < Dockerfile
	
The result has been posted to Docker Hub

	parker20121/joshua:6.0.1
	
This can be downloaded and run in Docker using the following command:

	docker run -t -i parker20121/joshua:6.0.1 /bin/bash
	

	

