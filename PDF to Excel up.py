import pandas as pd
from PIL import Image
import pytesseract
import os
from pdf2image import convert_from_path
import numpy as np
import re

#os.chdir('/Users/macbook/Desktop/PTE')
EXE=pd.DataFrame(np.nan,index=range(0,100000),columns=['ID','Text'])

####################################
####################################
######Convert PDF to image##########
####################################
####################################
pages = convert_from_path('A098001.pdf', 500)
for t in range(3,40):
    pages[t].save("%s.png"%t)

####Different pages 41 42######
pages[41].save("%s.png"%40)
pages[42].save("%s.png"%41)


####################################
####################################
#############Image to Text##########
####################################
####################################
left = 149
top = 290
right = 1406
bottom = 770
del z
del h
del i
del p
for p,h in zip(range(3,40),range(0,41)):
    im = Image.open(r"%s.png"%p)
    for z in range(0,10):
        for i in range(0,3):
            im1 = im.crop((left+i*1255, top+z*487, right+i*1255, bottom+z*487))

            im2=im1.crop((9,73,540,370))
            Ltext=pytesseract.image_to_string(im2,lang='hin')
            EXE.iloc[i+z*3+1+(h*40),1]=Ltext

            im3=im1.crop((550,10,1235,80))
            Ttext=pytesseract.image_to_string(im3,lang='eng+hin')
            EXE.iloc[i+z*3+1+(h*40),0]=Ttext

#####For last 2 different pages########
###Page40
del z
del h
del i
del p
p=40
im = Image.open(r"%s.png"%p)
h=100
for z in range(0, 2):
    for i in range(0, 3):
        im1 = im.crop((125 + i * 1255, 1635 + z * 521, 1383 + i * 1255, 2145 + z * 521))
        im2 = im1.crop((9, 73, 540, 370))
        Ltext = pytesseract.image_to_string(im2, lang='hin')
        EXE.iloc[i + z * 3 + 1 + (h * 40), 1] = Ltext
        im3 = im1.crop((550, 10, 1235, 80))
        Ttext = pytesseract.image_to_string(im3, lang='eng+hin')
        EXE.iloc[i + z * 3 + 1 + (h * 40), 0] = Ttext

i=0
z=0
h=200
im1 = im.crop((125 + i * 1255, 2908 + z * 487, 1383 + i * 1255, 3412 + z * 487))
im2 = im1.crop((38, 110, 700, 407))
Ltext = pytesseract.image_to_string(im2, lang='hin+eng')
EXE.iloc[i + z * 3 + 1 + (h * 40), 1] = Ltext
im3 = im1.crop((550, 10, 1235, 80))
Ttext = pytesseract.image_to_string(im3, lang='eng+hin')
EXE.iloc[i + z * 3 + 1 + (h * 40), 0] = Ttext

im1 = im.crop((125 + i * 1255, 3660 + z * 487, 1383 + i * 1255, 4165 + z * 487))
im2 = im1.crop((38, 110, 700, 407))
Ltext = pytesseract.image_to_string(im2, lang='hin+eng')
EXE.iloc[i + z * 3 + 1 + (h * 40)+1, 1] = Ltext
im3 = im1.crop((550, 10, 1235, 80))
Ttext = pytesseract.image_to_string(im3, lang='eng+hin')
EXE.iloc[i + z * 3 + 1 + (h * 40)+1, 0] = Ttext

im1 = im.crop((125 + i * 1255, 4405 + z * 487, 1383 + i * 1255, 4915 + z * 487))
im2 = im1.crop((38, 110, 700, 407))
Ltext = pytesseract.image_to_string(im2, lang='hin+eng')
EXE.iloc[i + z * 3 + 1 + (h * 40)+2, 1] = Ltext
im3 = im1.crop((550, 10, 1235, 80))
Ttext = pytesseract.image_to_string(im3, lang='eng+hin')
EXE.iloc[i + z * 3 + 1 + (h * 40)+2, 0] = Ttext


###Page41
del z
del h
del i
del p
p=41
h=300
im = Image.open(r"%s.png"%p)
for z in range(0, 2):
    for i in range(0,3):
        im1 = im.crop((125 + i * 1255, 460 + z * 521, 1383 + i * 1255, 972 + z * 521))
        im2 = im1.crop((38, 110, 700, 407))
        Ltext = pytesseract.image_to_string(im2, lang='hin')
        EXE.iloc[i + z * 3 + 1 + (h * 40), 1] = Ltext

        im3 = im1.crop((550, 10, 1235, 80))
        Ttext = pytesseract.image_to_string(im3, lang='eng+hin')
        EXE.iloc[i + z * 3 + 1 + (h * 40), 0] = Ttext

i=0
z=0
h=400
im1 = im.crop((125 + i * 1255, 1728 + z * 487, 1383 + i * 1255, 2242 + z * 487))
im2 = im1.crop((38, 110, 700, 407))
Ltext = pytesseract.image_to_string(im2, lang='hin')
EXE.iloc[i + z * 3 + 1 + (h * 40), 1] = Ltext
im3 = im1.crop((550, 10, 1235, 80))
Ttext = pytesseract.image_to_string(im3, lang='eng+hin')
EXE.iloc[i + z * 3 + 1 + (h * 40), 0] = Ttext

im1 = im.crop((125 + i * 1255, 2483 + z * 487, 1383 + i * 1255, 2989 + z * 487))
im2 = im1.crop((38, 110, 700, 407))
Ltext = pytesseract.image_to_string(im2, lang='hin')
EXE.iloc[i + z * 3 + 1 + (h * 40)+1, 1] = Ltext
im3 = im1.crop((550, 10, 1235, 80))
Ttext = pytesseract.image_to_string(im3, lang='eng+hin')
EXE.iloc[i + z * 3 + 1 + (h * 40)+1, 0] = Ttext

im1 = im.crop((125 + i * 1255, 3233 + z * 487, 1383 + i * 1255, 3739 + z * 487))
im2 = im1.crop((38, 110, 700, 407))
Ltext = pytesseract.image_to_string(im2, lang='hin')
EXE.iloc[i + z * 3 + 1 + (h * 40)+2, 1] = Ltext
im3 = im1.crop((550, 10, 1235, 80))
Ttext = pytesseract.image_to_string(im3, lang='eng+hin')
EXE.iloc[i + z * 3 + 1 + (h * 40)+2, 0] = Ttext



del z
del h
del i
del p
h=500
for z in range(0, 2):
    for i in range(0,3):
        im1 = im.crop((125 + i * 1255, 3975 + z * 521, 1383 + i * 1255, 4490 + z * 521))
        im2 = im1.crop((38, 110, 700, 407))
        Ltext = pytesseract.image_to_string(im2, lang='hin')
        EXE.iloc[i + z * 3 + 1 + (h * 40), 1] = Ltext
        im3 = im1.crop((550, 10, 1235, 80))
        Ttext = pytesseract.image_to_string(im3, lang='eng+hin')
        EXE.iloc[i + z * 3 + 1 + (h * 40), 0] = Ttext

####################################
####################################
######Delete NA prepare for regex###
####################################
####################################
test = EXE.dropna(how='all')
test1=test.replace(r'^\s*$', np.nan, regex=True)
test1=test1.dropna(how='all')
fin=pd.DataFrame(np.nan,index=range(0,10000),columns=['ID','नाम','पिता का नाम','मकान संख्या','आयु','लिंग'])


####################################
####################################
######Split text in to columns######
####################################
####################################
for j in range(0,len(test1)):
    fin.iloc[j,0]=test1.iloc[j,0]

    text=test1.iloc[j,1]
    pattern1=re.compile(r'नाम : \D+\n?\W{0}')
    text1=re.findall(pattern1,text)
    text1=str(text1).split('\\n', 1)[0]
    #text1=re.sub(r'िता का नाम.+','.',str(text1))
    text1=str(text1).replace('पिता का नाम :','').replace('\\n\\n','').replace(': ','').replace("'",'').replace('[','').replace(']','').replace('पिता का नाम :','').replace('\n\n','').replace('िता का नाम','').replace('\\n','')
    fin.iloc[j,1]=text1


    pattern2=re.compile(r'पिता का नाम :\D+\s+|पति का नाम : \D+\n')
    text2=re.findall(pattern2,text)
    text2=str(text2).replace('पिता का नाम : ','').replace('पति का नाम','').replace('\\n\\n','').replace(': ','').replace("'",'').replace('[','').replace(']','').replace('\\n','').replace('\n','')
    fin.iloc[j,2]=text2

    pattern3=re.compile(r'मकान संख्या:\s?\d{1,10}')
    text3=re.findall(pattern3,text)
    text3=str(text3).replace('मकान संख्या:','').replace('\\n\\n','').replace(': ','').replace("'",'').replace('[','').replace(']','').replace('\\n','').replace(' ','')
    fin.iloc[j,3]=text3

    pattern4=re.compile(r'आयु : \d+')
    text4=re.findall(pattern4,text)
    text4=str(text4).replace('आयु : ','').replace('\\n\\n','').replace(': ','').replace("'",'').replace('[','').replace(']','').replace('\\n','')
    fin.iloc[j,4]=text4

    pattern5=re.compile(r'लिंग : \D+')
    text5=re.findall(pattern5,text)
    text5=str(text5).replace('लिंग : ','').replace('\\n\\n','').replace(': ','').replace("'",'').replace('[','').replace(']','').replace('\\n','')
    fin.iloc[j,5]=text5

fin.to_excel('final.xlsx')
