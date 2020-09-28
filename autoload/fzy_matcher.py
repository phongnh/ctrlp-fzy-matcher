import os
import sys
import vim
from subprocess import Popen, PIPE


def ctrlp_fzy_match():
    fzy_bin    = vim.eval('s:fzy_bin')
    query      = vim.eval('a:str')
    candidates = vim.eval('a:items')
    limit      = int(vim.eval('a:limit'))

    fzy_cmd = [fzy_bin, f'--show-matches={query}', f'--num-of-matches={limit}']

    fzy_process = Popen(
        fzy_cmd,
        stdin=PIPE,
        stdout=PIPE,
        text=True,
        encoding='utf-8'
    )

    fzy_process.stdin.flush()
    fzy_process.stdin.writelines('\n'.join(candidates))
    fzy_process.stdin.close()

    result = [ line.rstrip() for line in fzy_process.stdout ]

    return result
