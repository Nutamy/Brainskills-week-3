# 3.2.1 Функция возвращает минимум и максимум
#
listOfGivenNumbers = []
given_number = -1
while given_number != 0:
    try:
        given_number = float(input("Enter a number: "))
        listOfGivenNumbers.append(given_number)
    except:
        print("Wrong!")
        continue

def minMax(myList):
    myList.pop()
    myMin = min(myList)
    myMax = max(myList)
    print("Min={} Max={}".format(myMin,myMax))

minMax(listOfGivenNumbers)