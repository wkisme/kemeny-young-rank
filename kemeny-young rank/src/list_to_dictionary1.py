def list_to_dictionary1(list1):
    dic = {}
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            #print(list1[i])
            if list1[i] - list1[j] < 0:
                dic[(i, j)] = 'greater'
            else:
                dic[(i, j)] = 'smaller'
    return dic