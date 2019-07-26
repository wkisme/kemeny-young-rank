def find_smallest_in_list(list1):

    item1 = list1[0]
    smallest_sum = list1[1]

    for i in range(len(list1)):
        if (i+1) % 2 == 0:

            sum1 = list1[i]
            item = list1[i-1]

            if smallest_sum > sum1:
                smallest_sum = sum1
                item1 = item
    return item1

