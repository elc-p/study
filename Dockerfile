FROM ubuntu:latest

ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get upgrade -y && \
    apt-get update -y

RUN apt-get install -y \
    curl \
    build-essential \
    libgmp-dev \
    libffi-dev \
    libncurses-dev \
    pkg-config

# python setup
RUN apt-get install -y python3.12 && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

# Haskell setup
RUN curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | \
    BOOTSTRAP_HASKELL_NONINTERACTIVE=1 \
    BOOTSTRAP_HASKELL_GHC_VERSION=recommended \
    BOOTSTRAP_HASKELL_INSTALL_STACK=1 \
    sh

ENV PATH="/root/.ghcup/bin:/root/.ghc/bin:$PATH"
