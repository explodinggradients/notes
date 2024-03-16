GIT_ROOT ?= $(shell git rev-parse --show-toplevel)

help: ## Show all Makefile targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'

build-docs: ## Build the doc site
	jupyter-book config sphinx $(GIT_ROOT)
	jupyter-book build $(GIT_ROOT)

watch-docs: ## Watch the doc site
	jupyter-book config sphinx $(GIT_ROOT)
	sphinx-autobuild $(GIT_ROOT) $(GIT_ROOT)/_build/html -b html --open-browser
