import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        

        print(file_name)
               
        images.append(file_name)

output=cv2.VideoWriter("friends.avi",cv2.VideoWriter_fourcc(*'DIVX'),5,(1280,720))    
print(len(images))
count = len(images)
for i in range(0,count+1):
    img=cv2.imread(images[i])
    #print(img.shape)
    #print(img)
    #cv2.imshow("image",img)
    output.write(img)
    cv2.waitKey(600)        