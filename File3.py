import ast
a1,t,b1,b2=0,0,[],[]
file=open('file.txt','r')
x=file.read()
dict=ast.literal_eval(x)
dict2= {y: x for x, y in dict.items()}
file2=open('file2.txt','r').read().split(' ')
output=" ".join(dict2[x] for x in file2)
def removeSpaces(string):
    string = string.replace(' ','')
    return string
xxx=removeSpaces(output)
for x in file2:
    if x == '0001':
        b1.append(a1)
    a1+=1
a1=0
for x in xxx:
    b2.append(x)
if not b1==[]:
    for x in b1:
        b2.insert(x,' ')
for x in b2:
    if t > 0:
        xx=x.lower()
        b2[t]=xx
    t+=1
end=''.join(b2)
print(end)


    

    
print()
input('...')
