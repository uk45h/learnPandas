# learn Pandas

I'm using Jupyter Docker Stacks - scipy-notebook
https://github.com/jupyter/docker-stacks

I've also updated it so You need to build your own docker (you need to be in createDocker because there you can find dockerfile)
docker build --rm -t jupyter/my-datascience-notebook .

Starting image:
docker run --rm -p 8888:8888 -v C:\kurs\learnPandas:/home/jovyan/work jupyter/my-datascience-notebook
where C:\kurs\learnPandas = your folder where you have cloned this git repo

