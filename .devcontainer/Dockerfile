FROM windpioneers/gdal-python:statutory-crow-gdal-2.4.1-python-3.9-dev

# Bust any pre-existing apt cache
#     Solves: https://askubuntu.com/questions/1388000/failed-to-fetch-deb-debian-org-debian-pool-main-l-linux-linux-libc-dev-5-10-70-1
RUN apt-get update -y

# Tell zsh where you want to store history
#     !!!IMPORTANT!!! Do not commit this file
ENV HISTFILE="/workspace/.devcontainer/.zsh_history"

# Install poetry
#  TODO remove once https://github.com/windpioneers/gdal-python/issues/11 is released
USER vscode
ENV POETRY_HOME=/home/vscode/.poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH "$POETRY_HOME/bin:$PATH"
RUN poetry config virtualenvs.create false

# Install localtunnel
RUN npm install -g localtunnel
