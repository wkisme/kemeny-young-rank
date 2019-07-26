def output_processing2(dic):
    l1 = []

    for key, value in dic.items():
        if value == 'greater':
            l1.append(key[0])
            l1.append('>')
            l1.append(key[1])

        elif value == 'no_relation':
            l1.append(key[0])
            l1.append('~')
            l1.append(key[1])
        elif value == 'smaller':
            l1.append(key[1])
            l1.append('>')
            l1.append(key[0])

    dic1 = standard_list(l1)
    str1 = standard_dictionary(dic1)
    #print(str1)
    return str1

def standard_list(l1):
    dic = {}
    for i in range(len(l1)):
        if i % 3 == 0:
            if l1[i+1] == '>':
                if l1[i] in dic.keys():
                    dic[l1[i]] += 1
                else:
                    dic[l1[i]] = 1
            else:
                dic[(l1[i], l1[i+2])] = 'equal'
    for i in range(len(l1)):
        if (i+1) % 3 == 0:
            if l1[i] in dic.keys():
                pass
            else:
                dic[l1[i]] = 0
    for i in range(len(l1)):
        if (i) % 3 == 0:
            if l1[i] in dic.keys():
                pass
            else:
                dic[l1[i]] = 0
    for key, value in dic.items():
        if value == 'equal':
            if dic[key[0]] > dic[key[1]]:
                dic[key[1]] = dic[key[0]]
            else:
                dic[key[0]] = dic[key[1]]



    return dic


def standard_dictionary(dic):



    l1 = sorted(dic, key=dic.__getitem__, reverse=True)
    str1 = ''
    for i in range(len(l1)):
        if i < len(l1) - 1:
            if dic[l1[i]] == dic[l1[i+1]]:
                str1 += l1[i]
                str1 += '~'
            else:
                str1 += l1[i]
                str1 += '>'
        else:
            str1 += l1[i]



    return str1
