import base64
import os
import random
import string
import sys

pdfstring = sys.argv[1]

base64decodestring = base64.b64decode(pdfstring, validate=True)

if base64decodestring[0:4] != b'%PDF':
  raise ValueError('girdini kontrol et, pdf olmayabilir')


rastgelesayi=(random.randint(1, 1000))
kucukHarf = chr(random.randint(ord('a'), ord('z')))
buyukHarf = chr(random.randint(ord('A'), ord('Z')))
print(rastgelesayi)
print(kucukHarf)
print(buyukHarf)

if os.path.exists("script/base64topdfdocument.pdf"):
    f = open('script/base64topdfdocument{}{}{}.pdf'.format(rastgelesayi,kucukHarf,buyukHarf), 'wb')
    f.write(base64decodestring)
    f.close()

else:
    f = open('script/base64topdfdocument.pdf', 'wb')
    f.write(base64decodestring)  
    f.close()
