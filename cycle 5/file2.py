# open file in read mode
fn = open('bcd.txt', 'r')

l=[]

for x in fn:
    l.append(x.strip())


print(l)

# open other file in write mode
fn1 = open('nfile.txt', 'w')


for x in l:
    fn1.write(str(l))
