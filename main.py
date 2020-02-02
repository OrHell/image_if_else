from PIL import Image
import numpy as np
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
for j in range (0, width):
    for i in range(0,height):
        first_image= im.getpixel((j,i))
        second_image = im2.getpixel((j,i))
        all_count = all_count + 1
        if first_image != second_image:
            count_error = count_error +1
        else:
            count_access = count_access +1
        
print ("Совпадений: ",count_access)
print ("Не совпадений: ",count_error)
print ("Всего сравнений:", all_count)