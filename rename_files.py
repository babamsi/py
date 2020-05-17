import os;

def rename_file():
	""" creating function that renames the files """
	file_list=os.listdir(r"/root/Desktop/projects/python/prank/prank");
	#print(file_list);
	saved_path = os.getcwd() #get current work directory
	print(saved_path)
	os.chdir(r"/root/Desktop/projects/python/prank/prank"); #change directory
	#looping each file to rename it
	for file_name in file_list:
		strr = str.maketrans("0123456789", "          ", "0123456789");
		os.rename(file_name, file_name.translate(strr));

	os.chdir(saved_path)

rename_file();

#os.listdir == lists all the files from the path
#there is string function called (translate) takes two args the first is table..
#that translate one set of characters to another set and the secnd args is list of characters to remove

