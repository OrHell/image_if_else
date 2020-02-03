from PIL import Image
import numpy as np
from matplotlib import pyplot
i=0
j=0
im = Image.open('test1.png')
im2 = Image.open('test2.png')
size = im.size
count_error = 0
count_access = 0
all_count = 0
width = size[0]
height = size[1]
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
for j in range (0, width):
    for i in range(0,height):
        first_image= im.getpixel((j,i))
        second_image = im2.getpixel((j,i))
        all_count = all_count + 1
        if first_image != second_image:
            count_error = count_error +1
        else:
            count_access = count_access +1
 

percent = 100/(width*height)    
count_access = percent * count_access
count_access = toFixed(count_access,2)
count_error = percent *count_error
count_error = toFixed(count_error,2)
print ("Совпадений: "+str(count_access) + "%")
print ("Не совпадений: "+str(count_error)+ "%")
print ("Всего сравнений:", all_count)



file = open("file_image.txt", 'w')

for j in range (0, width):
    for i in range(0,height):
        first_image= im.getpixel((j,i))
        fr = str(first_image)
        file.write(fr+'\n')
cur = 0       
file.close()



file = open("file_image_second.txt", 'w')

for j in range (0, width):
    for i in range(0,height):
        second_image= im2.getpixel((j,i))
        fr = str(second_image)
        file.write(fr+'\n')
cur = 0       
file.close()

with open ("file_image.txt",'r') as file_image:
    image_array = [row.strip() for row in file_image]
with open ("file_image_second.txt",'r') as file_image:
    image_array_second = [row.strip() for row in file_image]
   # for line in file_image:
      #  image_array[cur] = line
      #  cur+=1
lengt_array = len(image_array)
