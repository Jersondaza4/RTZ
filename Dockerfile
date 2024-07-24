# syntax=docker/dockerfile:1
FROM python:3.12-slim-bookworm
LABEL org.opencontainers.image.source="https://github.com/Jersondaza4/RTZ"

ENV PYTHONUNBUFFERED="1" \
    PIP_DISABLE_PIP_VERSION_CHECK="1" \
    PIP_NO_CACHE_DIR="1" \
    NODE_VERSION="20" \
    PNPM_VERSION="8.15.1" \
    PNPM_HOME="/usr/local/bin/" \
    VIRTUAL_ENV="/usr/local"

RUN mkdir /code
WORKDIR /code
COPY requirements.txt dev-requirements.txt /code/

RUN apt-get update \
    && apt-get install --no-install-recommends -y curl \
    && curl -fsSL https://get.pnpm.io/install.sh | SHELL="$(which bash)" sh - \
    && pnpm env use --global ${NODE_VERSION} \
    && apt-get install --no-install-recommends -y libc6-dev gcc git libmagic-dev libproj-dev \
    && npm cache clean --force \
    && apt-get autoremove -y --purge \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean

RUN pip install -r requirements.txt -r dev-requirements.txt