# Removing PIIs from PDFs

This repository contains a Docker-based application using Python to remove PII from PDFs. The program is meant to remove PIIs (specifically names, addresses, and emails) from PDFs to ensure digital privacy. Please make sure that 1) all PDF pages are compiled into one PDF, and named under 'example1.pdf', 2) names and addresses to be removed are added to 'personal_info.txt'. 

### Instructions to run the application:
In your terminal, please run the following codes.

1. clone this repository into personal computing environment 
`$ git clone [enter repository HTPPS]`

*Inside the 'removePII-app' folder:*
2. edit 'example1.pdf' file to contain all PDFs 

3. edit 'personal_info.txt' to contain all names and addresses to be removed

4. build the Docker image 
`$ docker build -t [image_name] . `

5. launch the Docker image
`$ docker run [image_name]`

6. PDF with removed PII will be automatically created under 'redacted.pdf'

### Summary of files
- [Dockerfile](https://github.com/redcarrott/Personal-Projects/blob/main/Dockerfile) - to create Docker environment
- [commands.md](https://github.com/redcarrott/Personal-Projects/blob/main/commands.md) - useful Docker commands
- [main.py](https://github.com/redcarrott/Personal-Projects/blob/main/main.py) - Python script
- [example1.pdf](https://github.com/redcarrott/Personal-Projects/blob/main/example1.pdf) - compiled singular PDF file (of all PDF pages)
- [personal_info](https://github.com/redcarrott/Personal-Projects/blob/main/personal_info.txt) - dictionary of personal info (names, addresses) to be removed
- [testing-1.ipynb](https://github.com/redcarrott/Personal-Projects/blob/main/testing-1.ipynb) - Jupyter Notebook to test Python scripts
- [redacted.pdf](https://github.com/redcarrott/Personal-Projects/blob/main/redacted.pdf) - outcome PDF of running application.
