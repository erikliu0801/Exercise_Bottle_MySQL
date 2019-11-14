FROM python:3.7
WORKDIR /bottle
ADD bottle_api.py requirements.txt  /bottle/
RUN pip install -r requirements.txt
CMD [ "python",bottle_api.py ]