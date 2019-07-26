from src.list_to_dictionary1 import list_to_dictionary1



def list_to_dictionary2(list1):
    #print(list1)
    list2 = []
    for i in list1:
        list2.append(list_to_dictionary1(i))
    return list2