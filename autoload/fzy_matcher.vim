if !has('python3')
    echom 'ctrlp-fzy-matcher requires python3!'
    finish
endif

let s:root_dir = escape(expand('<sfile>:p:h'), '\')
unsilent execute 'py3file ' . s:root_dir . '/fzy_matcher.py'

function! s:hide_current_file(ispath, crfile) abort
    return a:ispath && !get(g:, 'ctrlp_match_current_file', 0) && getftype(a:crfile) == 'file'
endfunction

function! fzy_matcher#match(items, str, limit, mmode, ispath, crfile, regex) abort
    call clearmatches()

    let s:candidates = a:items[0:a:limit]

    if s:hide_current_file(a:path, a:crfile)
        call remove(s:candidates, index(s:candidates, a:crfile))
    endif

    if empty(a:str)
        return s:candidates
    endif

    call matchadd('CtrlPMatch',
                \ '\v' . substitute(a:str, '.', '\0[^\0]{-}', 'g')[:-8])
    call matchadd('CtrlPLinePre', '^>')

    let result = py3eval('ctrlp_fzy_match()')

    return result
endfunction
