



#请输入小写字母，不要有二元符号，like abcd 且是从大到小排序
#输入q代表输入结束
def produce_output(length):
    l2=[]
    str1=''

    while length>0:

        for i in range(length):
            l2.append(i)


        length-=1





if __name__ == '__main__':
    l1 = []
    while(True):
        a = input('input: ')
        if a == 'q':
            break
        l1.append(a)
    for i in l1:
        length=len(i)
        break

    output_num = length*(length-1)*(2**(length-1))
    #print(output_num)

    for i in range(output_num):
        sum =0
        for item in l1:
            pass



    #print(l1)

