

import csv

import copy



# def read_csv():
# 读取csv文件成功！

def readfile2():
    big_list= []
    with open('t2.csv', 'r') as myFile:
        lines = csv.reader(myFile)
        for line in lines:
            big_list.append(line)
    return big_list

# 存取csv


def readfile1():
    big_list= []
    with open('t1.csv', 'r') as myFile:
        lines = csv.reader(myFile)
        for line in lines:
            big_list.append(line)
    return big_list


# for i in l2:
#     print(i)

# l1 变压器id 索引：6  线路id:9
# l2 变压器id  索引：2  线路id：0
def ccc_l(l1,l2):
    f_list = []
    for item1 in l1:
        for item2 in l2:

            if item1[6] == item2[2] and item1[9] != item2[0]:
                f_item = item1+item2
                f_list.append(f_item)


    return f_list




# 保存csv文件

# def writeIntoCSV(myList):
#     with open('f.csv', 'wb') as myFile:
#         myWriter = csv.writer(myFile)
#         myWriter.writerows(myList)



if __name__ == "__main__":
    l1 = readfile1()
    l2 = readfile2()
    d = ccc_l(l1,l2)
    with open('dog.csv','w',encoding='utf-8',newline='' "") as myFile:
        myWriter = csv.writer(myFile)

        myWriter.writerows(d)


