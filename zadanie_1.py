numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

new_numbers = 0
nontype = 0
for chis in range(len(numbers)):
     if type(numbers[chis]) != int:
         new_numbers = numbers[:chis] + numbers[chis + 1:]
         nontype = chis
sr_arifm = [sum(new_numbers) / len(numbers)]
isprav_num = numbers[:nontype]  + sr_arifm + numbers[nontype + 1:]

print("Измененный список:", isprav_num)
