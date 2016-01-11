# Notebook per l'analisi IRT del Bebras italiano 2015

## Avvertenze

Il repository necessita di Git LFS (plugin github per la gestione
efficiente di file grandi):
[git-lfs](https://github.com/github/git-lfs).

Dopo il `clone` serve un `git lfs pull`.


## Docker

Per modificare il notebook viene fornito un `Dockerfile` che permette
di avere un'istanza Jupyter con R (e rstan).


    docker build -t r-notebook .
    git clone https://github.com/monga/bebras-it-nb.git
	cd bebras-it-nb
	git lfs pull
	docker run --rm -it -p 127.0.0.1:8888:8888 --user root --name mynotebook -v "$(pwd):/home/jovyan/work/bebras-it-nb" r-notebook
	x-www-browser http://localhost:8888
	
