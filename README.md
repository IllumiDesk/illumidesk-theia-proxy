# IllumiDesk Theia IDE

[Theia](https://www.theia-ide.org/) is a configurable web based IDE
built with components from [Visual Studio Code](https://code.visualstudio.com/). This setup was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/template).

## Notes

- This package is tested with an image based on one of the [Jupyter docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) running with JupyterHub.

## Why?

IllumiDesk's setup requires `docker volume` mounts with the local host instance. Files copied to the `jovyan` home directory during the docker build stage are overriden by the files located on the host directories when running a container based on the image. Therefore `node`, `nvm`, and `theia` are installed in directories that are globally accessible and are not mounted.

This package tweaks the command to use the globally installed `package.json` file required to run `theia`.

## Attributions

- [`jupyter-theia-proxy`](https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/theia)
- [`theia docker apps`](https://github.com/theia-ide/theia-apps)
- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)
