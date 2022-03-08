import os
import shutil
name = input("please tell me you name:")
if name != "help":
	path = os.getcwd()
	path1 = path
	for i in range(100):
		path1 = path1 + "\\" + "%"
		os.mkdir(path1)
	old_files = os.path.join(path,name)
	new_files = os.path.join(path1,name)
	os.rename(old_files,new_files)
else:
	path = os.getcwd()
	path1 = path	
	for i in range(100):
		path1 = path1 + "\\" + "%"
	path1 = path1 + "\\"
	a = os.listdir(path1)
	old_files = os.path.join(path,a[0])
	new_files = os.path.join(path1,a[0])
	os.rename(new_files,old_files)
	path1 = path + "\\" + "%"
	shutil.rmtree(path1)