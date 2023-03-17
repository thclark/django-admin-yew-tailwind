

# -------------------- MY DEVELOPER SETUP -------------------

FROM windpioneers/gdal-python:little-gecko-gdal-2.4.1-python-3.9-dev

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

# Install localtunnel (so you can serve on the internet from your PC)
# RUN npm install -g localtunnel


# -------------------- YEW + TAILWIND SETUP -------------------

# Install the rust toolchain and give permission for all users to use it
#  See: https://stackoverflow.com/questions/49676490/when-installing-rust-toolchain-in-docker-bash-source-command-doesnt-work
ENV RUST_INSTALL_DIR=/home/vscode/.rust
ENV RUSTUP_HOME="${RUST_INSTALL_DIR}/rustup"
ENV CARGO_HOME="${RUST_INSTALL_DIR}/cargo"
RUN mkdir -p ${RUSTUP_HOME} && \
    mkdir -p ${CARGO_HOME}
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="${CARGO_HOME}/bin:${PATH}"
RUN chmod -R ugo+rwx ${RUST_INSTALL_DIR}

# Setup yew and trunk
#   See: https://yew.rs/docs/getting-started/introduction
RUN rustup target add wasm32-unknown-unknown
RUN cargo install trunk@0.16.0

# Install tailwind
#   See: https://dev.to/arctic_hen7/how-to-set-up-tailwind-css-with-yew-and-trunk-il9
RUN yarn global add tailwindcss
