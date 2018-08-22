# -*- coding: utf-8 -*-

# Consider this to add command line
# https://github.com/google/python-fire/blob/master/docs/guide.md

import click
import signal
import sys
import hashlib
import os

'''
usage:
    cat sabre.txt | python pii.py
'''

salt = os.getenv('SALT', 'nacl')

# record_number: [field0, field9]

# These should be 1 based
d = {
        5:  [6],
        7:  [7,13,14,15,17,18],
        8:  [10],
        10: [11,12],
        11: [6,7,8],
        15: [6,7,8],
        17: [5,7,9,11,13,15],
        18: [16,47],
        20: [8],
        21: [8],
        22: [8,9,10,11],
        24: [8],
}

def hasher(s):
    return len(s) * 'X'

    # return hashlib.md5(salt.encode() + s.encode()).hexdigest()[:10].upper()

def main():
    lineno = 0
    with sys.stdin as fp:
        for lineno, line in enumerate(fp):

            # remove trailing newline
            line = line.strip()

            # Each record is delimited by a pipe |
            line_a = line.split('|')

            # First field in each line is the 2 digit "record type"
            record_type = int(line_a[0])

            if record_type in d:
                pii_a = [hasher(f) if ind+1 in d[record_type] else f for ind, f in enumerate(line_a)]
                pii   = '|'.join(pii_a)
                print(pii)
            else:
                print(line)


def sigpipe():
    # Reset Python's default SIGPIPE handler for Linux
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# @click.option('--count', '-c', default=1, help='number of greetings')

@click.command()
@click.argument('src', type=click.File('r'))
@click.argument('dst', type=click.File('w'), default='-')
def cli(src, dst):
    sigpipe()

    for lineno, line in enumerate(src):

        # remove trailing newline
        line = line.strip()

        try:
            # Each record is delimited by a pipe |
            line_a = line.split('|')

            # First field in each line is the 2 digit "record type"
            record_type = int(line_a[0])

            if record_type in d:
                pii_a = [hasher(f) if ind+1 in d[record_type] else f for ind, f in enumerate(line_a)]
                pii   = '|'.join(pii_a)
                print(pii, file=dst)
            else:
                print(pii, file=dst)
        except:
            # if the line isn't in the expected form, pass it on unchanged
            print(line, file=dst)

if __name__ == '__main__':
    cli()
