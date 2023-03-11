FROM python:3.8.10

WORKDIR /
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt
COPY . /

CMD bash -c "while true; do sleep 1; done"