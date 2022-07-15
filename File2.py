import ast
file=open('file.txt','r')
x=file.read()
dict=ast.literal_eval(x)
aa=str(input('Insert string(characters only): '))
a=aa.upper()
output=" ".join(dict[x] for x in a)
file2=open('file2.txt','w').write(output)
print(output)
