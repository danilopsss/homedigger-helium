FROM python:3.11.7-slim AS builer

ARG APP
ENV APP=$APP

COPY ./scripts . \
     ./alembic.ini \
     ./pyproject.toml \
     ./poetry.lock \
     /

COPY ./$APP /$APP
COPY ./alembic /alembic

RUN  ./build.sh
