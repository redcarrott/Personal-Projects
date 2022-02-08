# Removing PIIs from PDFs

This repository contains a Docker-based application using Python to remove PII from PDFs. The program is meant to remove PIIs, specifically names, addresses, and emails from PDFs to ensure digital privacy. Please make sure that all PDF pages are compiled into one PDF, and named under 'example1.pdf'. 

### Instructions to run the application:
In your terminal, please run the following codes.

1. build the Docker image 
`$ docker build -t [image_name] . `

2. launch the Docker image
`$ docker run [image_name]`

### Summary of files
