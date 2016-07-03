#!/bin/bash
rm -rf lib/
pip --version | grep python2.7 > /dev/null
if [[ 0 -ne $? ]]; then
	echo 'Pip must be run with python2.7 for standard env'
	exit 1
fi
pip install -t lib/ -r requirements.txt
