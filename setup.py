try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description' : 'Ficha do jogador web para o livro-jogo "Cidadela do Caos"',
'author' : 'Saulo Andrade',
'url' : 'URL to get it at',
'download_url' : 'Where to download it',
'author_email' : 'sauloandradegames@gmail.com',
'version' : '0.1',
'install_requires' : ['nose'],
'packages' : ['CHAOS'],
'scripts' : [],
'name' : 'Chaos Citadel Web'
}

setup(**config)
