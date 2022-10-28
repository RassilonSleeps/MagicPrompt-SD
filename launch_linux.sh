#!/usr/bin/env bash

function locate {
        dirname -- "$( readlink -f -- "$0"; )"
}

cd $( locate )

if [[ -a $( locate )/venv/bin/activate ]]
then
    source $( locate )/venv/bin/activate
elif [[ ! -d $( locate )/venv ]]
then
    python3 -m venv $( locate )/venv
    source $( locate )/venv/bin/activate
else
    echo "Could not locate venv/bin/activate";
    exit
fi

if [[ "$1" == "--jupyter" ]] || [[ "$1" == "--colab" ]] 
then
    python3 -m pip install -r notebook-requirements.txt | grep -v 'already satisfied'
elif [[ -z "$1" ]]
then
    python3 -m pip install -r requirements.txt | grep -v 'already satisfied'
fi

if [[ "$1" == "--jupyter" ]] 
then
    python3 -m jupyter notebook MagicPrompt.ipynb --no-browser
elif [[ "$1" == "--colab" ]] 
then
    python3 -m jupyter notebook --no-browser --NotebookApp.allow_origin="https://colab.research.google.com" --port=8888 --NotebookApp.port_retries=0
else
    python3 MagicPrompt.py
fi
