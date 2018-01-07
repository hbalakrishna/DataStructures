def toStr(num , base):
    conv_string = "0123456789ABCDEF"
    if num<base:
        return conv_string[num]
    else:
        return toStr(num//base, base) + conv_string[num%base]

print(toStr(1453, 16))