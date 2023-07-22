FROM python:3-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

# Bundle app source
COPY . .
CMD [ "python3","Hello.py"]