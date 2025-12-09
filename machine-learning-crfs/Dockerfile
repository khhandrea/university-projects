FROM python:3.9.16

# Mount volume
RUN mkdir /volume
WORKDIR /volume
ADD ./requirements.txt /volume

# Requirements
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
CMD jupyter notebook --ip 0.0.0.0 --allow-root