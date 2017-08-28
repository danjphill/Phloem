import os
files=[]
folders=[]

for file in os.listdir(os.getcwd()+"/static/video"):
	try:
 		for innerfile in os.listdir(os.getcwd()+"/static/video/"+file):
 			break
 		folders.append(file)
 	except:
 		files.append(file)
	
for file1 in files: 
	print "file" + file1

for folder in folders:
	print "folder" + folder
 		