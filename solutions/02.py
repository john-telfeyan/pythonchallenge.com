# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/def/map.html
i guess we're supposed to use the map() function
http://book.pythontips.com/en/latest/map_filter.html
'''

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.\
 bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle\
 qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet = "abcdefghijklmnopqrstuvwxyz "
key =      "----g-----m---q----------- " 
translation = ""

for l in message:
    if (l in alphabet):
        try:
            t = key[alphabet.find(l)]
        except IndexError:
            t = " "

#       if t == '-':
#              t  = l
    translation += t
        

print(translation)

abc_wheel = alphabet*2