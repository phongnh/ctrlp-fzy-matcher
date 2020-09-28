import os
import sys
import vim
from subprocess import Popen, PIPE


def ctrlp_fzy_match():
    query      = vim.eval('a:str')
    candidates = vim.eval('a:items')
    limit      = int(vim.eval('a:limit'))

    fzy_cmd = ['fzy', f"--show-matches={query}"]

    fzy_process = Popen(
        fzy_cmd,
        stdin=PIPE,
        stdout=PIPE,
        text=True,
        encoding='utf-8'
    )

    head_cmd = ['head', '-n 100']
    head_process = Popen(
        head_cmd,
        stdin=fzy_process.stdout,
        stdout=PIPE,
        text=True,
        encoding='utf-8'
    )

    fzy_process.stdin.flush()
    fzy_process.stdin.writelines('\n'.join(candidates))
    fzy_process.stdin.close()

    return [ line.rstrip() for line in head_process.stdout ]
