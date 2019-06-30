FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

RUN mkdir /code
WORKDIR /code
COPY ./app /code

# RUN adduser -D user
# USER user


# RUN mkdir /code /code/static
# WORKDIR /code
# ADD requirements.txt /code/
# RUN pip install -r requirements.txt
# ADD . /code/