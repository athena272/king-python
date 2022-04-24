def findDuplicate(listNum):
    tortoise = listNum[0]
    rabbit = listNum[0]
    while True:
        tortoise = listNum[tortoise]
        rabbit = listNum[listNum[rabbit]]
        
        if tortoise == rabbit:
            return tortoise
            

print(findDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 20, 27, 2]))