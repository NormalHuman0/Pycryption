import ast
a1,t,b1,b2=0,0,[],[]
file=open('file.txt','r')
x=file.read()
dict=ast.literal_eval(x)
dict2= {y: x for x, y in dict.items()}
text=str(input('Input like this:1234 5678 9012'))
output="".join(dict2[x] for x in text)