FROM python:3.8-slim-buster

# Force stdin, stdout and stderr to be totally unbuffered.
ENV PYTHONUNBUFFERED 1
# Python won’t try to write .pyc or .pyo files on the import of source modules.
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./server/requirements /server/requirements
RUN pip install -r /server/requirements/local.txt

COPY ./compose/local/server/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/server/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /server

ENTRYPOINT ["/entrypoint"]