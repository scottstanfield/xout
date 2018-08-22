import sys
import click
import signal
import os

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


def sigpipe():
    # Reset Python's default SIGPIPE handler for Linux
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

@click.command()
@click.argument('src', type=click.Path(exists=True, dir_okay=False, allow_dash=True))
@click.argument('dst', type=click.File('w'), default='-')
def cli(src, dst):
    sigpipe()

    is_file  = True if src != '-' else False
    filename = src if is_file else 'stdin'
    nbytes   = os.stat(src).st_size if is_file else -1

    print(is_file, click.format_filename(src), file=sys.stderr)
    print(nbytes, file=sys.stderr)

    with click.open_file(src, 'r') as lines:
        with click.progressbar(length=nbytes, label=filename, file=sys.stderr) as bar:
            for lineno, line in enumerate(lines):
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

                bar.update(len(line))

