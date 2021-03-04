[![Build Status](https://travis-ci.com/lucasOlivio/inquest.svg?branch=master)](https://travis-ci.com/github/lucasOlivio/inquest)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)
[![License](https://img.shields.io/npm/l/react-native-smart-badge.svg)](https://github.com/lucasOlivio/inquest/blob/master/LICENSE)

Test project to manage companies, persons and its assets through an API.

------------------------------------------------------------------------------------------------------------------------
# SERVER

# Prerequisites

- [Docker Windows](https://docs.docker.com/docker-for-windows/install/)
- [Docker Linux](https://docs.docker.com/engine/install/)
- [Docker Mac](https://docs.docker.com/docker-for-mac/install/)

- [Docker-compose](https://docs.docker.com/compose/install/)

- [Pre-commit](https://pre-commit.com/#install)

- [Newman](https://www.npmjs.com/package/newman)

# Local Development

- Create a folder named "local" inside the .envs and set the same variables as the .envs/test files

Start the dev server for local development:
```bash
docker-compose -f docker-compose.local.yml up
```

Run tests and tests coverage in container:

```bash
docker-compose -f docker-compose.local.yml run --rm server coverage run -m pytest
```

Run tests with postman collection:

```bash
newman run Inquest.postman_collection.json
```

Run any command inside the docker container:

```bash
docker-compose -f docker-compose.local.yml run --rm server [command]
```

- First local run will create initial users
    - An administrator user:
        - username: admin
        - password: admin
    - And an advertiser user:
        - username: test
        - password: test
