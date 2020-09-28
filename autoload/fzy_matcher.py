import vim
from subprocess import Popen, PIPE


ENCODING = 'utf-8'


def ctrlp_fzy_match():
    query      = vim.eval('a:str')
    candidates = vim.eval('a:items')
    limit      = int(vim.eval('a:limit'))

    use_custom_fzy = int(vim.eval('s:use_custom_fzy'))
    use_with_head  = int(vim.eval('s:use_with_head'))

    if use_custom_fzy == 1:
        return run_fzy(query, candidates, limit, True)

    if use_with_head == 1:
        return run_fzy_with_head(query, candidates, limit)

    return run_fzy(query, candidates, limit, False)


def run_fzy(query, candidates, limit, custom=False):
    fzy_cmd = ['fzy', f'--show-matches={query}']

    if custom is True:
        fzy_cmd.append(f'--num-of-matches={limit}')

    fzy_process = Popen(
        fzy_cmd,
        stdin=PIPE,
        stdout=PIPE
    )

    fzy_process.stdin.write(bytes('\n'.join(candidates), ENCODING))
    fzy_process.stdin.flush()

    output = fzy_process.communicate()[0]
    result = output.decode(ENCODING).rstrip().split("\n")

    if custom is False:
        result = result[0:limit]

    return result


def run_fzy_with_head(query, candidates, limit):
    fzy_process = Popen(
        ['fzy', f'--show-matches={query}'],
        stdin=PIPE,
        stdout=PIPE
    )

    fzy_process.stdin.write(bytes('\n'.join(candidates), ENCODING))
    fzy_process.stdin.flush()
    fzy_process.stdin.close()

    head_process = Popen(
        ['head', f'-n {limit}'],
        stdin=fzy_process.stdout,
        stdout=PIPE
    )

    result = [ line.decode(ENCODING).rstrip() for line in head_process.stdout ]

    return result
