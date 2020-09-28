import vim
from subprocess import Popen, PIPE


ENCODING = 'utf-8'


def ctrlp_fzy_match():
    fzy_bin    = vim.eval('s:fzy_bin')
    query      = vim.eval('a:str')
    candidates = vim.eval('a:items')
    limit      = int(vim.eval('a:limit'))

    fzy_process = Popen(
        [fzy_bin, f'--show-matches={query}', f'--num-of-matches={limit}'],
        stdin=PIPE,
        stdout=PIPE
    )

    fzy_process.stdin.flush()
    fzy_process.stdin.write(bytes('\n'.join(candidates), ENCODING))

    output = fzy_process.communicate()[0]
    result = output.decode(ENCODING).rstrip().split("\n")

    return result
