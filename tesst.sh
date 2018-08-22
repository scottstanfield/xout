#!/bin/sh
[ -e big1.txt ] || for i in {1..500}; do cat b6.txt >> big1.txt; done

python xout.py big1.txt clean.big1.txt
fgrep sanches clean.big1.txt
