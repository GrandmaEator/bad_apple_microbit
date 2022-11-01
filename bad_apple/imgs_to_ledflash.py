import os
from natsort import natsorted # pip install natsort
from PIL import Image

gencode = ""

m = os.listdir("imgs")
print(natsorted(m))

for i in range(len(m)):
    im = Image.open("imgs\\" + m[i]) # Can be many different formats.
    pix = im.load()
    a = 0

    pixel = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    pixel[a] = pix[0,0][0]
    a = a + 1
    
    pixel[a] = pix[1,0][0]
    a = a + 1
    
    pixel[a] = pix[2,0][0]
    a = a + 1
    
    pixel[a] = pix[3,0][0]
    a = a + 1
    
    pixel[a] = pix[4,0][0]
    a = a + 1

    pixel[a] = pix[0,1][0]
    a = a + 1
    
    pixel[a] = pix[1,1][0]
    a = a + 1
    
    pixel[a] = pix[2,1][0]
    a = a + 1
    
    pixel[a] = pix[3,1][0]
    a = a + 1
    
    pixel[a] = pix[4,1][0]
    a = a + 1
    
    pixel[a] = pix[0,2][0]
    a = a + 1
    
    pixel[a] = pix[1,2][0]
    a = a + 1
    
    pixel[a] = pix[2,2][0]
    a = a + 1
    
    pixel[a] = pix[3,2][0]
    a = a + 1
    
    pixel[a] = pix[4,2][0]
    a = a + 1
    
    pixel[a] = pix[0,3][0]
    a = a + 1
    
    pixel[a] = pix[1,3][0]
    a = a + 1
    
    pixel[a] = pix[2,3][0]
    a = a + 1
    
    pixel[a] = pix[3,3][0]
    a = a + 1
    
    pixel[a] = pix[4,3][0]
    a = a + 1
    
    pixel[a] = pix[0,4][0]
    a = a + 1
    
    pixel[a] = pix[1,4][0]
    a = a + 1
    
    pixel[a] = pix[2,4][0]
    a = a + 1
    
    pixel[a] = pix[3,4][0]
    a = a + 1
    
    pixel[a] = pix[4,4][0]
    a = a + 1
    
    # print(pixel)

    for u in range(len(pixel)):
            if u == 0:
                gencode = gencode + "drawled(0,0,"+str(pixel[u])+");"
            if u == 1:
                gencode = gencode + "drawled(0,1,"+str(pixel[u])+");"
            if u == 2:
                gencode = gencode + "drawled(0,2,"+str(pixel[u])+");"
            if u == 3:
                gencode = gencode + "drawled(0,3,"+str(pixel[u])+");"
            if u == 4:
                gencode = gencode + "drawled(0,4,"+str(pixel[u])+");"
            if u == 5:
                gencode = gencode + "drawled(1,0,"+str(pixel[u])+");"
            if u == 6:
                gencode = gencode + "drawled(1,1,"+str(pixel[u])+");"
            if u == 7:
                gencode = gencode + "drawled(1,2,"+str(pixel[u])+");"
            if u == 8:
                gencode = gencode + "drawled(1,3,"+str(pixel[u])+");"
            if u == 9:
                gencode = gencode + "drawled(1,4,"+str(pixel[u])+");"
            if u == 10:
                gencode = gencode + "drawled(2,0,"+str(pixel[u])+");"
            if u == 11:
                gencode = gencode + "drawled(2,1,"+str(pixel[u])+");"
            if u == 12:
                gencode = gencode + "drawled(2,2,"+str(pixel[u])+");"
            if u == 13:
                gencode = gencode + "drawled(2,3,"+str(pixel[u])+");"
            if u == 14:
                gencode = gencode + "drawled(2,4,"+str(pixel[u])+");"
            if u == 15:
                gencode = gencode + "drawled(3,0,"+str(pixel[u])+");"
            if u == 16:
                gencode = gencode + "drawled(3,1,"+str(pixel[u])+");"
            if u == 17:
                gencode = gencode + "drawled(3,2,"+str(pixel[u])+");"
            if u == 18:
                gencode = gencode + "drawled(3,3,"+str(pixel[u])+");"
            if u == 19:
                gencode = gencode + "drawled(3,4,"+str(pixel[u])+");"
            if u == 20:
                gencode = gencode + "drawled(4,0,"+str(pixel[u])+");"
            if u == 21:
                gencode = gencode + "drawled(4,1,"+str(pixel[u])+");"
            if u == 22:
                gencode = gencode + "drawled(4,2,"+str(pixel[u])+");"
            if u == 23:
                gencode = gencode + "drawled(4,3,"+str(pixel[u])+");"
            if u == 24:
                gencode = gencode + "drawled(4,4,"+str(pixel[u])+");"
   
    gencode = gencode + "clearfps();"

# print(gencode)


f = open("gen.py", 'w')
f.write(gencode)
f.close()