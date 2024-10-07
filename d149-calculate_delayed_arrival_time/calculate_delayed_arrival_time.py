def findDelayedArrivalTime(arrivalTime, delayedTime):
    aux = arrivalTime + delayedTime
    return aux if aux < 24 else aux - 24

print(findDelayedArrivalTime(15, 5)) # 20