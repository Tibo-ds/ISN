from PIL.Image import *

def changement(couleur, pixel):
    if pixel == "1" and (couleur % 2) == 0:
        couleur += 1
    elif pixel == "0" and (couleur % 2) == 1:
        couleur -= 1
    return couleur

messageACacher = "101010011001011001010010010110101001100101100101001001011010100110010110010100100101"
print(len(messageACacher))
if len(messageACacher)%3> 0:
    for loop in range(len(messageACacher)%3):
        messageACacher += "0"
 
messageACacher = str(messageACacher)
im = open('image.png')
x = 0
y = 0
(xMax,yMax) = im.size
for loop in range(0,len(messageACacher),3):
    if x != xMax:
        if y != yMax:
            (r,v,b) = Image.getpixel(im,(x,y))
            (pix1,pix2,pix3) = messageACacher[loop],messageACacher[loop+1],messageACacher[loop+2]
            print("avant :",r,v,b)
            r = changement(r,pix1)
            v = changement(v,pix2)
            b = changement(b,pix3)
            im.putpixel((x,y),(r,v,b))
            print("apres :",r,v,b)
            print(pix1,pix2,pix3)
            x += 1
        else:
            print('Image trop petite')
    else:
        x = 0
        y += 1
Image.show(im)
