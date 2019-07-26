from src.pre_processing_input1 import pre_processing_input1


def pre_processing_input2(list1):
    l2 = []
    for i in list1:
        l2.append(pre_processing_input1(i))
    return l2
