for i in range(1, 101):
    second_power= i **2
    third_power = i **3
    print(i, second_power, third_power)

output_file = 'powers.txt'
with open(output_file,'w') as file:
    print("Number\tSecond Power\tThird Power")
    print("=================================")
    file.write("Number\tSecond Power\tThird Power\n")
    file.write("=================================\n")

    for i in range(1, 101):
        second_power= i ** 2
        third_power = i ** 3
        print(f'{i}\t{second_power}\t\t {third_power}')
        file.write(f'{i}\t{second_power}\t {third_power}\n')