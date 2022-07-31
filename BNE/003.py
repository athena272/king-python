#Link repositorio: https://github.com/athena272/BNE_TI

def bubbleSort(list):
    for passNum in range(len(list)-1,0,-1):
        for i in range(passNum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

#Link repositorio: https://github.com/athena272/BNE_TI
