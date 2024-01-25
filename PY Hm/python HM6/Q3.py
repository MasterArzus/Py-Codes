from PIL import Image
import math
im=Image.open("C:\\Python\\zuoye\\202130430423-庄多懋\\源代码\\Q3\\bird.jpg")
im=im.convert('L')

im1=Image.open('C:\\Python\\zuoye\\202130430423-庄多懋\\源代码\\Q3\\1.jpg')
im2=Image.open('C:\\Python\\zuoye\\202130430423-庄多懋\\源代码\\Q3\\2.jpg')
im3=Image.open('C:\\Python\\zuoye\\202130430423-庄多懋\\源代码\\Q3\\3.jpg')
im4=Image.open('C:\\Python\\zuoye\\202130430423-庄多懋\\源代码\\Q3\\4.jpg')
im5=Image.open('C:\\Python\\zuoye\\202130430423-庄多懋\\源代码\\Q3\\5.jpg')
im6=Image.open('C:\\Python\\zuoye\\202130430423-庄多懋\\源代码\\Q3\\6.jpg')

im1=im1.convert('L')
im2=im2.convert('L')
im3=im3.convert('L')
im4=im4.convert('L')
im5=im5.convert('L')
im6=im6.convert('L')

List=[im1,im2,im3,im4,im5,im6]
List1_pixel=[0,0,0,0,0,0]

for i in range(6):
    for j in range(16):
        for k in range(16):
            List1_pixel[i]+=List[i].getpixel((j,k))
    List1_pixel[i]=List1_pixel[i]/(16*16)


List2=[]
List2_pixel=[]

for i in range(34):
    for j in range(34):
        x=im.crop((i*16,j*16,(i+1)*16,(j+1)*16))
        List2.append(x)

for i in range(len(List2)):
    List2_pixel.append(0)
    for j in range(16):
        for k in range(16):
            List2_pixel[i] += List2[i].getpixel((j, k))
    List2_pixel[i] = List2_pixel[i] / (1500)

for i in range(len(List2)):

    vs0 = abs(List1_pixel[0] - List2_pixel[i])
    vs1 = abs(List1_pixel[1] - List2_pixel[i])
    vs2 = abs(List1_pixel[2] - List2_pixel[i])
    vs3 = abs(List1_pixel[3] - List2_pixel[i])
    vs4 = abs(List1_pixel[4] - List2_pixel[i])
    vs5 = abs(List1_pixel[5] - List2_pixel[i])

    #以灰度相差最小的来替换
    if vs0<=vs1 and vs0<=vs2 and vs0<=vs3 and vs0<=vs4 and vs0<=vs5 :
        List2[i]=List[0]
    elif vs1<=vs0 and vs1<=vs2 and vs1<=vs3 and vs1<=vs4 and vs1<=vs5 :
        List2[i]=List[1]
    elif vs2<=vs0 and vs2<=vs1 and vs2<=vs3 and vs2<=vs4 and vs2<=vs5 :
        List2[i]=List[2]
    elif vs3<=vs0 and vs3<=vs2 and vs3<=vs1 and vs3<=vs4 and vs3<=vs5 :
        List2[i]=List[3]
    elif vs4<=vs0 and vs4<=vs2 and vs4<=vs3 and vs4<=vs1 and vs4<=vs5 :
        List2[i]=List[4]
    elif vs5<=vs0 and vs5<=vs2 and vs5<=vs3 and vs5<=vs4 and vs5<=vs1:
        List2[i]=List[5]

    # 以灰度相差最大的来替换
    # if vs0 >= vs1 and vs0 >= vs2 and vs0 >= vs3 and vs0 >= vs4 and vs0 >= vs5:
    #     List2[i] = List[0]
    # elif vs1 >= vs0 and vs1 >= vs2 and vs1 >= vs3 and vs1 >= vs4 and vs1 >= vs5:
    #     List2[i] = List[1]
    # elif vs2 >= vs0 and vs2 >= vs1 and vs2 >= vs3 and vs2 >= vs4 and vs2 >= vs5:
    #     List2[i] = List[2]
    # elif vs3 >= vs0 and vs3 >= vs2 and vs3 >= vs1 and vs3 >= vs4 and vs3 >= vs5:
    #     List2[i] = List[3]
    # elif vs4 >= vs0 and vs4 >= vs2 and vs4 >= vs3 and vs4 >= vs1 and vs4 >= vs5:
    #     List2[i] = List[4]
    # elif vs5 >= vs0 and vs5 >= vs2 and vs5 >= vs3 and vs5 >= vs4 and vs5 >= vs1:
    #     List2[i] = List[5]

x=0
for i in range(34):
    for j in range(34):
        im.paste(List2[x],(i*16,j*16,(i+1)*16,(j+1)*16))
        x += 1
        
im.show()
im.save('C:\\Python\\zuoye\\202130430423-庄多懋\\源代码\\Q3\\bird2.jpg')

