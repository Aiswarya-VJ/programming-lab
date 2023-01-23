
fle = open("/home/exam3/Desktop/sample.txt","r")

fle_wrt = open("/home/exam3/Desktop/write.txt","w")

fle_rd = open("/home/exam3/Desktop/write.txt","r")

i = 1
for line in fle:
    if(i%2 != 0):
        fle_wrt.write(line)
    i+=1
fle_wrt.close()

for line in fle_rd:
    print(line)