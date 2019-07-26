def output_processing(dic):
    dic1 = {}
    for key, value in dic.items():
        l1 = [0]*2
        if key[0] == 0.0:
            l1[0] = 'a'
        elif key[0] == 1.0:
            l1[0] = 'b'
        elif key[0] == 2.0:
            l1[0] = 'c'
        elif key[0] == 3.0:
            l1[0] = 'd'
        if key[1] == 0.0:
            l1[1] = 'a'
        elif key[1] == 1.0:
            l1[1] = 'b'
        elif key[1] == 2.0:
            l1[1] = 'c'
        elif key[1] == 3.0:
            l1[1] = 'd'

        tuple1 = tuple(l1)

        if value == 1:
            dic1[tuple1] = 'greater'
        elif value == 0:
            dic1[tuple1] = 'smaller'
        elif value == 9:
            dic1[tuple1] = 'no_relation'

    return dic1



