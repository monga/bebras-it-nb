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
	docker run --rm -it -p 127.0.0.1:8888:8888 --user root --name mynotebook -v "$(pwd):/notebooks" r-notebook
	docker exec mynotebook git pull
	docker exec mynotebook git lfs pull
	x-www-browser http://localhost:8888
	
