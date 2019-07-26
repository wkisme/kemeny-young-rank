def input1():
    l1 = []
    while (True):
        a = input('输入字符串: ')

        if a == 'q':
            break
        b = input('输入字符串个数：')
        for i in range(int(b)):
            l1.append(a)

    return l1
