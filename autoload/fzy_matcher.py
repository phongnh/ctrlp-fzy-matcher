import os
import sys
import vim


def ctrlp_fzy_match():
    query      = vim.eval('a:str')
    candidates = vim.eval('s:candidates')
    limit      = int(vim.eval('a:limit'))

    return candidates
