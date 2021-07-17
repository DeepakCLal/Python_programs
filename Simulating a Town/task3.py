#Import math library for performing floor function

import math

#Read from the file town_start.txt

population_read1 = open('town_start.txt','r')

#Open the file town_end.txt for writing the results obained from the calculations performed

population_write1 = open('town_end.txt','w')

#Initialise an empty array to store the final results onto

results = [0,0,0]

#Initialise a temporary varaible for performing the calculations

pop_new = 0

#Store the contents of the file town_start.txt onto a temporary list

with open('town_start.txt') as file:
	temp_list = [str(i) for i in file]

#Convert the data-type of the contents in the temporary list(default data-type:'string') into integer('int')
#temp_list[0] = results[0] = number of food present
#temp_list[1] = results[1] = number of people(population)
#temp_list[2] = results[2] = current year

temp_list = list(map(int, temp_list))

#Perform a check for draft year

if (temp_list[2] % 18 == 0) or (temp_list[2] == 0):

	#Population is increased by 30 percent on an yearly basis and then 40 percent of the resulting population is reduced in the draft year
	#If the population is equal to the amount of food present, perform the following calculations

	if temp_list[1] == temp_list[0]:
		results[1] = (temp_list[1] + (0.3 * temp_list[1]))
		results[1] -= (results[1] * 0.4)

	#If the population is less than the amount of food, then perform the following calculations

	elif temp_list[1] < temp_list[0]:
		results[1] = temp_list[1] + (0.3 * temp_list[1])
		results[1] -= (0.4 * results[1])
		results[1] = math.floor(results[1])

	#If the population is greater than the amount of food, then perform the following calculations

	elif temp_list[1] > temp_list[0]:
		pop_new = temp_list[0]
		results[1] = pop_new + (0.3 * pop_new)
		results[1] -= (0.4 * results[1])
		results[1] = math.floor(results[1])

#If the year is not a draft year, perform the following calculations

else:

	#Population is increased by 30 percent on an yearly basis
	#If the population is equal to the amount of food present, perform the following calculations

	if temp_list[1] == temp_list[0]:
		results[1] = (temp_list[1] + (0.3 * temp_list[1]))

	#If the population is less than the amount of food, then perform the following calculations

	elif temp_list[1] < temp_list[0]:
		results[1] = temp_list[1] + (0.3 * temp_list[1])
		results[1] = math.floor(results[1])

	#If the population is greater than the amount of food, then perform the following calculations

	elif temp_list[1] > temp_list[0]:
		pop_new = temp_list[0]
		results[1] = pop_new + (0.3 * pop_new)
		results[1] = math.floor(results[1])

#Write the amount of food into the final array

results[0] = temp_list[0]

#Increment the year and write it onto the final array

results[2] = temp_list[2] + 1

#Convert the contents of the resulting array into 'int' data-type(to remove the decimal points) and then 
#convert them to 'string' inorder to write them into the resulting file

results = list(map(int, results))

results = list(map(str, results))

#Write the contents of the resulting list onto the file town_end.txt

for lines in results:
	population_write1.write(lines + '\n')

#Close all the files after performing necessary operations

file.close()
population_write1.close()
population_read1.close()