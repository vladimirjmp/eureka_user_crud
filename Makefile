# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

.PHONY: help

.DEFAULT_GOAL := help

help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: down build up ## See down, build, up, tests detail

build: ## Build the base images
	docker compose build

up: ## Run all services
	docker compose up -d

down: ## Stop an delete all containers
	docker compose down --remove-orphans

back-shell: ## Backend bash shell
	docker compose exec -it backend bash

back-logs: ## Backend logs
	docker compose logs --tail 100 -f backend

front-shell: ## Frontend bash shell
	docker compose exec -it backend bash

front-logs: ## Frontend logs
	docker compose logs --tail 100 -f frontend

dev-setup: ## Dev: Setup development environment with pre-commit hooks
	@pip install  -Ur backend/requirements/development.txt
	@pre-commit install -t pre-commit -t commit-msg --overwrite

dev-check: ## Dev: Run all pre-commit hooks.
	@pre-commit run --all-files
