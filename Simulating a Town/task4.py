#Import math library for performing floor function

import math

#Read from the file town_start.txt

final_read = open('town_start.txt','r')

#Open the file town_end.txt for writing the results obained from the calculations performed

final_write = open('town_end.txt','w')

#Initialise a variable for counting the number of iterations performed

year = 0

#Store the contents of the file town_start.txt onto a temporary list

with open('town_start.txt') as file:
	final_list = [str(i) for i in file]

#Convert the data-type of the contents in the temporary list(default data-type:'string') into integer('int')
#final_list[0] = number of food present
#final_list[1] = number of people(population)
#final_list[2] = current year

final_list = list(map(int, final_list))

#Perform the iterations upto 100 years or until the population becomes zero

while year<100 and final_list[1]>0:

	#Check if the amount of food is less than the population

	if final_list[0] < final_list[1]:
		final_list[1] = final_list[0]

	#Perform the following calculations to the data in the final list
	#Changes to food is made
	#Population is increased by 30 percent on an yearly basis

	final_list[0] -= final_list[1]
	final_list[0] -= (final_list[0]/5)
	final_list[0] = math.floor(final_list[0])
	final_list[1] *= 1.3
	final_list[1] = math.floor(final_list[1])

	#Perform a check for the draft year

	if (final_list[2]%18 == 0):

		#If the year is a draft year, then perform the following calculations

		final_list[1] *= 0.6
		final_list[1] = math.floor(final_list[1])

	#Food is ordered for 80 percent of the population

	final_list[0] += (final_list[1] * 0.8)
	final_list[0] = math.floor(final_list[0])

	#The iteration count and year is incremented

	final_list[2] +=1
	year +=1

#Convert the final list into strings for writing into the town_end.txt file

final_list = list(map(str, final_list))

#Write the contents of the resulting list onto the file town_end.txt

for lines in final_list:
	final_write.write(lines + '\n')

#Close all the files after performing necessary operations

file.close()
final_write.close()
final_read.close()
