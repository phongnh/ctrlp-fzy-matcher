if !has('python3')
    echom 'ctrlp-fzy-matcher requires python3!'
    finish
endif

if !executable('fzy')
    echom 'ctrlp-fzy-matcher requires fzy!'
    finish
endif

let s:root_dir = escape(expand('<sfile>:p:h'), '\')
unsilent execute 'py3file ' . s:root_dir . '/fzy_matcher.py'

let s:is_custom_fzy = (system('fzy --help') =~# 'num-of-matches')
let s:has_head      = executable('head')

function! s:hide_current_file(ispath, crfile) abort
    return a:ispath && !get(g:, 'ctrlp_match_current_file', 0) && getftype(a:crfile) == 'file'
endfunction

function! fzy_matcher#match(items, str, limit, mmode, ispath, crfile, regex) abort
    call clearmatches()

    if empty(a:str)
        let result = a:items[0:(a:limit)]
    else
        call matchadd('CtrlPMatch',
                    \ '\v' . substitute(a:str, '.', '\0[^\0]{-}', 'g')[:-8])
        call matchadd('CtrlPLinePre', '^>')

        let result = py3eval('ctrlp_fzy_match()')
    endif

    if s:hide_current_file(a:path, a:crfile)
        call remove(result, index(result, a:crfile))
    endif

    return result
endfunction
