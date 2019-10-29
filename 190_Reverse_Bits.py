def reverseBits(n):
    return int('{0:032b}'.format(n)[::-1],2)

#{0:032b}'.format(n) : num->32bit
#int(...,2) : num->2sinsu

#reference
#https://note.nkmk.me/python-bin-oct-hex-int-format#/
