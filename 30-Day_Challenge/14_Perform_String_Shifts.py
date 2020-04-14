def stringShift(s, shift):
    def Shift(sh, pointer):
        if sh[0] == 1:
            pointer -= sh[1]
            if pointer < 0:
                pointer += len(s)
        elif sh[0] == 0:
            pointer += sh[1]
            if pointer > len(s)-1:
                pointer -= len(s)
        return pointer

    head = 0
    tail = len(s)-1
    for sh in shift:
        head = Shift(sh, head)
        tail = Shift(sh, tail)
    print(head, tail)
    return s[head:] + s[:(tail+1)] if head != 0 else s[head:]


ans = stringShift("joiazl",
                  [[1, 1], [1, 6], [0, 1], [1, 3], [1, 0], [0, 3]])
print(ans)
    
        





    
