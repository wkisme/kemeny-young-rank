from src.input import input1

from src.pre_processing_input2 import pre_processing_input2

from src.list_to_dictionary2 import list_to_dictionary2
from src.list_of_dictionary_to_matrix import list_of_dictionary_to_matrix
from src.find_shortest_distence import find_shortest_distance
#输入按照从大到小进行排序 like: abcd
from src.output_processing import output_processing
from src.output_processing2 import output_processing2

if __name__ == '__main__':
    l1 = input1()  #list of string
    l2 = pre_processing_input2(l1)#list of lists
    #print(l2)
    l3 = list_to_dictionary2(l2) #list of dictionary
    a = list_of_dictionary_to_matrix(l3)
    #print(a)
    dic1 = find_shortest_distance(a)
    #print(dic1)
    dic2 = output_processing(dic1)
    #print(dic2)
    str1 = output_processing2(dic2)
    print(str1)


