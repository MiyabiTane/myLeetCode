def hammingWeight(n):
    #２進数の文字列に変換
    n=bin(n)
    print(n)
    count=0
    for s in n:
        if s=='1':
            count+=1
    return count

count=hammingWeight(0b00011101)
print(count)

#参考 : https://note.nkmk.me/python-bin-oct-hex-int-format/
