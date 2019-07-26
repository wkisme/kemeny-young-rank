import numpy as np
# greater = 1 smaller = 0 no_sense = 2
def list_of_dictionary_to_matrix(list_of_dictionary):
    row = len(list_of_dictionary)
    col = len(list_of_dictionary[0])
    a = np.zeros((row, col*3))
    for i in range(len(list_of_dictionary)):
        counter = 0
        for j in list_of_dictionary[i].keys():
            a[i][counter] = j[0]
            counter +=1
            a[i][counter] = j[1]
            counter +=1
            if list_of_dictionary[i][j] == 'greater':
                a[i][counter] = 1
            else:
                a[i][counter] = 0 #smaller
            counter +=1
    return a
