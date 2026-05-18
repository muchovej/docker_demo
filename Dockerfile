FROM python:3.13-alpine AS build
ARG APP_DIR=/src

RUN apk --no-cache add curl build-base libffi-dev

ENV POETRY_VERSION=2.2.1
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH

COPY pyproject.toml poetry.lock ./
COPY . ./

RUN python -m venv --copies ${APP_DIR}/venv
RUN . ${APP_DIR}/venv/bin/activate && poetry install --no-root --only main

# DEPLOYMENT RUN
FROM python:3.13-alpine AS run
ARG APP_DIR=/src

COPY --from=build ${APP_DIR}/venv ${APP_DIR}/venv/
ENV PATH ${APP_DIR}/venv/bin:$PATH

WORKDIR ${APP_DIR}/
COPY . ./

RUN apk --no-cache add bash

CMD python -m src.hello