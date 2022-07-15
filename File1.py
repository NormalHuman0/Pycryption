import random
a,b,c,d,x,pp='0','0','0','0',0,0
al=[chr(x) for x in range(65,91)]
for x in range(0,10):
    al.append(str(x))
dict = {
    " ":'0001'
}
for x in al:
    a,b,c,d=str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9))
    xx=dict.values()
    for e in xx:
        if e==a+b+c+d:
            a,b,c,d=str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9))
        else:
            pp=0
    dict[x]=a+b+c+d
#----------------
file=open("file.txt","w")
file.write(str(dict))
file.close()
text="ABC"
'''Variables=dir()
for name in Variables:
    if not name.startswith('__'):
        myvalue=eval(name)
        print(name, type(myvalue), "=", myvalue)'''
output=" ".join(dict[x] for x in text)
'''
output1=" ".join(dict[x] for x in text1)
output2=" ".join(dict[x] for x in text2)
print(output,output1,output2)'''
print(dict)