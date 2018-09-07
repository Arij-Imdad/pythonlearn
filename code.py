#===========================================================================
#Write a function to fetch all files in a directory.
#Keep them in a list and sort the list alphabaticaly and add _edited 
#===========================================================================
import os


d=['a1','2','a6','3']
x=sorted(d , key =lambda t:t[0])
print(x)

filename = input("Input the extension: ")
path="/home/ebryx/Desktop/pythonlearn"



files = [os.path.splitext(file) 
for file in os.listdir(path)
 	if not file.startswith('.') if file.endswith(filename)]
newlist=[item[0] for item in files]

newlist.sort(key=lambda part: float(part[1:]))

#mysort=sorted(newlist , key =lambda t:t[1:])


#files.sort(key=lambda x : str(x).lower())


print (newlist)

	


