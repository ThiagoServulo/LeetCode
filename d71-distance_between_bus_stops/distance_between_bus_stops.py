def distanceBetweenBusStops(distance, start, destination):
    if start > destination:
        start, destination = destination, start
    return min(sum(distance[start:destination]), 
               sum(distance[destination:]) + sum(distance[0:start]))


print(distanceBetweenBusStops([1,2,3,4], 0, 1)) # 1
print(distanceBetweenBusStops([1,2,3,4], 0, 2)) # 3
print(distanceBetweenBusStops([1,2,3,4], 0, 3)) # 4
print(distanceBetweenBusStops([7,10,1,12,11,14,5,0], 7, 2)) # 4
