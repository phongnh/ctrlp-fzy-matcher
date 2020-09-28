ctrlp-fzy-matcher
=================

CtrlP matcher based on [fzy](https://github.com/jhawthorn/fzy)


## Installation

Use [vim + pathogen](http://vimcasts.org/episodes/synchronizing-plugins-with-git-submodules-and-pathogen)

    cd ~/.vim
    git submodule add https://github.com/phongnh/ctrlp-fzy-matcher bundle/ctrlp-fzy-matcher

Use vim plugin manager

    " https://github.com/VundleVim/Vundle.vim
    Plugin 'phongnh/ctrlp-fzy-matcher'
    :PluginInstall

    " https://github.com/junegunn/vim-plug
    Plug 'phongnh/ctrlp-fzy-matcher'
    :PlugInstall

    " https://github.com/Shougo/neobundle.vim
    NeoBundle 'phongnh/ctrlp-fzy-matcher'
    :NeoBundleInstall


## Configuration

```vim
let g:ctrlp_match_func = { 'match': 'fzy_matcher#match' }
```
