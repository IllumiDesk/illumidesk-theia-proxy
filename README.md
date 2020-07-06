# IllumiDesk Theia IDE

[Theia](https://www.theia-ide.org/) is a configurable web based IDE
built with components from [Visual Studio Code](https://code.visualstudio.com/). This setup was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/template).

## Installation

## Requirements

#### Install THEIA IDE

Refer to [THEIA's official documentation](https://theia-ide.org/docs/composing_applications). If you are installing THEIA with docker, [this repo has some good docker-based examples](https://github.com/theia-ide/theia-apps) on how to get up and running with different setups.

### Install Jupyter Notebook

This extension relies on the Jupyter Notebook to run. [Refer to Jupyter's official documentaion](https://jupyter.org/install) for installation instructions.

### Install illumidesk-theia-proxy

Install this package:

```
pip install -d git+https://github.com/IllumiDesk/illumidesk-theia-proxy@v0.1.0#egg=illumidesk-theia-proxy
```

## Notes

- This package is tested with an image based on one of the [Jupyter docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) running with JupyterHub.
- THEIA requires Node 10x. The base `jupyter docker-stacks` images need some tweaking to make them work with `nvm` and the correct version of `node`. Refer to [this Dockerfile](https://github.com/IllumiDesk/illumidesk/src/illumidesk/workspaces/theia/templates/Dockerfile.theia) for an example.

## Why?

IllumiDesk's setup requires `docker volume` mounts with the local host instance. Files copied to the `jovyan` home directory during the docker build stage are overriden by the files located on the host directories when running a container based on the image. Therefore `node`, `nvm`, and `theia` are installed in directories that are globally accessible and are not mounted.

This package tweaks the command to use the globally installed `package.json` file required to run `theia`.

## Attributions

- [`jupyter-theia-proxy`](https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/theia)
- [`theia docker apps`](https://github.com/theia-ide/theia-apps)
- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
