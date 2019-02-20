#!/bin/bash

#-----INSTALLING_PYENV
pyenv install -s 2.7.15
pyenv install -s 3.7.1

pyenv global 2.7.15
pyenv virtualenv py2env

pyenv global 3.7.1
pyenv virtualenv py3env
