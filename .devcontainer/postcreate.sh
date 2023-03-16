#!/bin/zsh

# Install dependencies
poetry install

# Install precommit hooks
pre-commit install && pre-commit install -t commit-msg

# Install tailwind
#   See: https://dev.to/arctic_hen7/how-to-set-up-tailwind-css-with-yew-and-trunk-il9
yarn global add tailwindcss
