From python:3.7
MAINTAINER Juve Macias jmaciasc

ADD mac_address_vendor.py /

RUN pip install requests

ENTRYPOINT ["python3.7", "./mac_address_vendor.py"]