import setuptools

setuptools.setup(
    name="illumidesk-theia-proxy",
    version='0.1.1',
    url="https://github.com/illumidesk/illumidesk-theia-proxy",
    author="IllumiDesk Team",
    description="hello@illumidesk.com",
    packages=setuptools.find_packages(),
	keywords=['jupyter', 'theia', 'jupyterhub'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'theia = illumidesk_theia_proxy:setup_theia',
        ]
    },
    package_data={
        'illumidesk-theia-proxy': ['icons/*'],
    },
)
