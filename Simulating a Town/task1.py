#Read from the file town_start.txt

town_start_read = open('town_start.txt','r')

#Open the file town_end.txt for writing the results obtained from performing the required operation

town_end_write = open('town_end.txt','w')

#Get each element from town_start.txt and write it into town_end.txt

for starting_food in town_start_read:
    town_end_write.write(starting_food)

#Close both the files after the operation has been performed

town_end_write.close()
town_start_read.close()
