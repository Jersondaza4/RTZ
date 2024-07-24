# RTZ


## Running

From the terminal, run:

```bash
bin/devserver_run
```

## Commands

To run any other command on the app container you can do:

    docker compose exec web python3 manage.py run_huey
    docker compose exec web python3 manage.py createsuperuser
    docker compose exec web python3 manage.py shell_plus
    docker compose exec web pytest
    docker compose exec web bash

## Add python packages

Add the package name to the `requirements.in` or `dev-requirements.in` file and run:

    docker compose exec web uv pip compile --generate-hashes requirements.in -o requirements.txt -v
    docker compose exec web uv pip compile --generate-hashes dev-requirements.in -o dev-requirements.txt -v
    ./bin/build_docker_image

    en windows local:
    python -m piptools compile --generate-hashes requirements.in -o requirements.txt -v
    python -m piptools compile --generate-hashes dev-requirements.in -o dev-requirements.txt -v

To upgrade pre-commit versions:

    pre-commit autoupdate

## Add javascript packages

To add a javascript package run:

    docker compose exec web pnpm add htmx

## Upgrade packages

To upgrade js packages run:

    docker compose exec web pnpm update --interactive

For python packages run:

    docker compose exec web uv pip compile --generate-hashes --upgrade requirements.in -o requirements.txt -v
    docker compose exec web uv pip compile --generate-hashes --upgrade dev-requirements.in -o dev-requirements.txt -v
    ./bin/build_docker_image

    en windows local:
    python -m piptools compile --generate-hashes --upgrade requirements.in -o requirements.txt -v
    python -m piptools compile --generate-hashes --upgrade dev-requirements.in -o dev-requirements.txt -v

## Local email

To see email sending in your local environment open browser and go to http://localhost:8025/

## Translation

When text is changed you must run:

    docker compose exec web python3 manage.py makemessages --locale=es

Translate and commit the *.po files, they will be compiled automatically when deploying.

If want to compile the files locally you must run:

    docker compose exec web python3 manage.py compilemessages
