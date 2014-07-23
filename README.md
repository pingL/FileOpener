FileOpener
---

A tiny utility script based on python to index, search and open files quickly

#### Usage
Place `alias o='python -ux ~/bashwork/o.cmd'` in yout `.bashrc` file.

And, place `o.py` `o.cmd` files in `~/bashwork`

Using `o.cmd` file, if you want to open file Advanced Bash-Scripting Guide.pdf

`o . advanced bash`

However, if you aren't sure of the filename, like `../tv/cosmos/episode s2e3.mp4`. Then, use `,` instead of `.`. Like,

`o , cosmos s2e3 `

If you don't have bash on you system or only comfortable with py version. Then, use

`python o.py . advanced bash`

`python o.py . cosmos s2e3 `

To reset the index, use
`o -index `

--------

#### Credits
Thanks to [S Anand](http://www.s-anand.net/) for re-introducing Bash.

--------

##### TODO
Exclude certain directories and file extensions.
