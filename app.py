data_point = [1,2,4,5]

def mean(data_points):
    counter = 0
    divisor = 0

    for data in data_point:
        counter += data
    for data in data_point:
        divisor += 1
    print(counter/divisor)

def median(data_points):
    if data_points.sorted():
        pass
    else:
        data_points.sort()

    if len(data_points)/2 !=0:
        dafssf

mean(data_point)