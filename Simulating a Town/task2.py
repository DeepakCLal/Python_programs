#Read from the file town_start.txt

food_read1 = open('town_start.txt','r')

#Open the file town_end.txt for writing the results otained from the calculations performed

food_write1 = open('town_end.txt','w')

#Initialise an empty array to store the final results onto

results = [0,0,0]

#Initialise two temporary variables which will be used for calculations

temp = 0
temp_pop = 0

#Open town_start.txt and store each element into a temporary list.

with open('town_start.txt') as file:
  temp_list = [str(i) for i in file]

#Convert the data-type of the contents in the temporary list(default data-type:'string') into integer('int')
#temp_list[0] = results[0] = number of food present
#temp_list[1] = results[1] = number of people(population)
#temp_list[2] = results[2] = current year

temp_list = list(map(int, temp_list))

#Check if the population is equal to food and performing necessary calculations
#All the food is consumed by the people and then food is ordered for 80 percent of the population at the end of the year

if temp_list[1] == temp_list[0] :
	results[0] = (temp_list[0] - temp_list[1]) + (0.8 * temp_list[1])

#Check if the population is less than the food and performing necessary calculations
#Some food is thrown away and then food is ordered for 80 percent of the population at the end of the year

elif temp_list[1] < temp_list[0]:
	temp = temp_list[0] - temp_list[1]
	results[0] = ((temp) - (temp/5)) + (temp_list[1] * 0.8)

#Check if the population is greater than the food and performing necessary calculations
#Some food is thrown away and then food is ordered for 80 percent of the population at the end of the year

elif temp_list[1] > temp_list[0] :
	temp = temp_list[1] - temp_list[0]
	temp_pop = temp_list[0]
	results[0] = ((temp) - (temp/5))  + (temp_pop * 0.8)

#Write the population number into the final array

results[1] = temp_list[1]

#Increment the year and write it onto the final array

results[2] = temp_list[2] + 1

#Convert the contents of the resulting array into 'int' data-type(to remove the decimal points) and then 
#convert them to 'string' inorder to write them into the resulting file
results = list(map(int, results))

results = list(map(str, results))

#Write the contents of the resulting list onto the file town_end.txt

for lines in results:
	food_write1.write(lines+'\n')


#Close all the files after performing necessary operations

file.close()
food_write1.close()
food_read1.close()