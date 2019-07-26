import re

def pre_processing_input1(str1):
    counter = 0
    l1 = ['end']*10
    l2 = []
    for i in str1:
        if i == 'a':
            l1[0] = counter
        if i == 'b':
            l1[1] = counter
        if i == 'c':
            l1[2] = counter
        if i == 'd':
            l1[3] = counter
        counter += 1
    for j in l1:
        if j is not 'end':
            l2.append(j)
    #print(l2)
    return l2

