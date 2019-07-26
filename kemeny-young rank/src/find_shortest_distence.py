from src.find_smallest_in_list import find_smallest_in_list

def find_shortest_distance(matrix1):
    '''for i in list_of_dictionary:

        sorted(i, key=lambda key1=i.__getitem__: key1[1], reverse=False)
        sorted(i, key=lambda key1=i.__getitem__: key1[0], reverse=False)
        '''
    dic = {}
    m, n = matrix1.shape
    #print(matrix1)

    for i in range(n):
        if (i+1) % 3 == 0:
            #print(i)

            candidate = [0, 1, 9]
            l1 = []
            l1[:] = []
            for item in candidate:

                sum1 = 0
                for j in range(m):
                    if matrix1[j,i] == item:
                        sum1 += 0  #same
                    elif abs(matrix1[j, i] - item) == 1:
                        sum1 += 2  #vice
                    else:
                        sum1 += 1  #no_sense

                l1.append(item)
                l1.append(sum1)
            item1 = find_smallest_in_list(l1)
            dic[(matrix1[0, i-2], matrix1[0, i-1])] = item1
    return dic


