# A novel metric for assessing climatological surface habitability

[![arXiv preprint](https://img.shields.io/badge/arXiv-2407.05838-red "arXiv preprint")](https://arxiv.org/abs/2407.05838)

## Summary

* This repository contains the code used to create the figures and perform the analysis in [https://arxiv.org/abs/2407.05838](https://arxiv.org/abs/2407.05838)
* Note that the pre-processed data output from [1-preprocess.ipynb](https://github.com/hannahwoodward/2024-hab-metrics/blob/main/1-preprocess.ipynb) is stored in [/data](https://github.com/hannahwoodward/2024-hab-metrics/tree/main/data) which can be used to directly re-create the figures in [2-figures.ipynb](https://github.com/hannahwoodward/2024-hab-metrics/blob/main/2-figures.ipynb) 


## Steps to reproduce figures

* Clone this repository
* Follow instructions at [hannahwoodward/docker-jupyter-climate](https://github.com/hannahwoodward/docker-jupyter-climate) to:
  * Install Docker
  * Download the Docker image `woodwardsh/jupyter-climate:latest`
  * Start a new Docker (or podman) container inside the cloned copy of this repository, and
  * Open the Jupyter lab instance in the browser
* To re-create the figures from the pre-processed data stored in this repository, run the notebook [2-figures.ipynb](https://github.com/hannahwoodward/2024-hab-metrics/blob/main/2-figures.ipynb)
* Alternatively, follow the instructions provided in [1-preprocess.ipynb](https://github.com/hannahwoodward/2024-hab-metrics/blob/main/1-preprocess.ipynb) to first download and preprocess all the data from source before creating the figures