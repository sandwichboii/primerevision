def primesTill(till):
    if till == 1:
        return []
    if till == 2:
        return [2]
    primes = [2]
    for i in range(3, till):
        if isPrime(primes, i):
            primes.append(i)
    return primes


def isPrime(pList, number):
    primeness = True
    place = 0
    while primeness and place < len(pList):
        primeness = (0 != (number % pList[place]))
        if not primeness:
            return False
        place = place + 1
    return True


def initialize(till):
    # get a specific array that is related to prime numbers

    firstArray = primesTill(till)
    # get prime numbers till 'till'

    secondArray = [2, 3]
    for i in range(2, len(firstArray)):
        if (secondArray[-1] - secondArray[-2]) < (firstArray[i] - secondArray[-1]):
            secondArray.append(firstArray[i])
    # an array where 1st is 2, 2nd is 3, and nth is smallest number that
    # satisfies nth-(n-1)th bigger than (n-1)th - (n-2)th

    thirdArray = [0]
    for i in secondArray:
        thirdArray.append(thirdArray[-1] + i)

    # turns the distance between each dates(secondArray) into raw dates
    thirdArray.remove(0)
    return thirdArray

print(initialize(1000))