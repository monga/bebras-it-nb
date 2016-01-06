FROM jupyter/r-notebook

MAINTAINER Mattia Monga <monga@debian.org>

USER root
RUN wget https://packagecloud.io/github/git-lfs/packages/debian/jessie/git-lfs_1.1.0_amd64.deb/download -O git-lfs_1.1.0_amd64.deb \
    && dpkg -i git-lfs_1.1.0_amd64.deb \
    && rm git-lfs_1.1.0_amd64.deb

USER jovyan
RUN git lfs install &&  git clone https://github.com/monga/bebras-it-nb.git
WORKDIR bebras-it-nb
RUN git lfs pull
RUN conda install --yes -c mittner r-rstan && conda clean -yt


