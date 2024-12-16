#PIP is python package manager, ex javascipt, npm
#pip install
#pip uninstall
#pip show
#pip list

import qrcode

data = 'https://nihongokyoshi-net.com/jlpt-grammars'

img = qrcode.make(data)

img.save('qr.png')