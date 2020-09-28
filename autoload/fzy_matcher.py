import os
import sys
import vim
from subprocess import Popen, PIPE


def ctrlp_fzy_match():
    use_head   = vim.eval('s:use_head')
    query      = vim.eval('a:str')
    candidates = vim.eval('a:items')
    limit      = int(vim.eval('a:limit'))

    if use_head:
        process = _fzy_with_head(query, candidates, limit)
        result  = [ line.rstrip() for line in process.stdout ]
    else:
        process = _fzy_only(query, candidates)
        result  = []
        for line in process.stdout:
            if len(result) >= limit:
                break
            result.append(line.rstrip())

    return result


def _fzy_with_head(query, candidates, limit):
    fzy_process = _fzy_only(query, candidates)

    head_cmd = ['head', f'-n {limit}']
    head_process = Popen(
        head_cmd,
        stdin=fzy_process.stdout,
        stdout=PIPE,
        text=True,
        encoding='utf-8'
    )

    return head_process


def _fzy_only(query, candidates):
    fzy_cmd = ['fzy', '--show-matches', query]
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

    return fzy_process
