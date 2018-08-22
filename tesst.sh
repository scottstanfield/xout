#!/bin/sh
[ -e big1.txt ] || for i in {1..500}; do cat b6.txt >> big1.txt; done

fgrep --ignore-case --color=auto sanchez big1.txt | head
python3 xout.py big1.txt clean.big1.txt
fgrep --ignore-case --color=auto sanchez clean.big1.txt | head
