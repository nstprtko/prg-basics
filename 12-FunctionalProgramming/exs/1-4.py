def ms_to_kmh(ms):
    speed = lambda ms : ms * 3.6
    return speed(ms)

result = ms_to_kmh(10)
print(result)