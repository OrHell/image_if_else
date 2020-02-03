from PIL import Image

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
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
 

percent = 100/(width*height)    
count_access = percent * count_access
count_access = toFixed(count_access,2)
count_error = percent *count_error
count_error = toFixed(count_error,2)
print ("Совпадений: "+str(count_access) + "%")
print ("Не совпадений: "+str(count_error)+ "%")
print ("Всего сравнений:", all_count)

# Функция записи изображения в файл

def image_writer(file_name,w,h,image,opened_image):
    file = open(file_name, 'w')
    for x in range(0,w):
        for y in range(0,h):
            opened_image = image.getpixel((x,y))
            fr = str(opened_image)
            file.write(fr+'\n')
    file.close()
image_writer("file_image.txt",width,height,im,first_image)
image_writer("file_image_second.txt", width, height,im2, second_image)

# Чтение изображения из файла
with open ("file_image.txt",'r') as file_image:
    image_array = [row.strip() for row in file_image]
with open ("file_image_second.txt",'r') as file_image:
    image_array_second = [row.strip() for row in file_image]
   # for line in file_image:
      #  image_array[cur] = line
      #  cur+=1
lengt_array = len(image_array)
