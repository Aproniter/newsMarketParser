FROM python:3.8
WORKDIR /web
COPY ./ /web
ENV PIP_DEFAULT_TIMEOUT=100
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
