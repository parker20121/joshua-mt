# joshua-mt

Dockerfile extends a Centos 7 image and installs Joshua 
machine translation software 

	http://joshua-decoder.org/

Docker downloads and compiles the Joshua software, storing
the results on a Centos 7 image. The Joshua software
can be found in the following Linux directory

	/opt/joshua-v6.0.1

To create the docker image, run the following command:

	docker build - < Dockerfile
	
The latest image is posted to Docker Hub

	parker20121/joshua:6.0.1
	
This can be downloaded and run in Docker using the following command:

	docker run -t -i parker20121/joshua:6.0.1 /bin/bash
	
All that remains is pushing the bundle file to the docker container, 
where you can then run the Joshua server on port 5674. Once the bundle 
is unzipped, run the following command

	nohup ./run-joshua.sh &
	

