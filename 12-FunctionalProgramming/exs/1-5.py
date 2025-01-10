def avg_speed(distance, hours, minutes):
    time = hours + (minutes / 60)
    speed = distance/ time

    return speed

distance = float(input())
hours = int(input())
minutes = int(input())

result = avg_speed(distance, hours, minutes)
print(result)