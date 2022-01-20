# Reading & writing into File

file=open('C:/Users/RAGHAVA/Desktop/Course2/test.txt','w')
file.write("this is my first file")
file.close()

#Reading

f=open('C:/Users/RAGHAVA/Desktop/Course2/test.txt','r')
print(f.read(5))

file.close()