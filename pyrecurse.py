"""
Developer - kujalk
Date - 04/01/2018
Version - 1
"""

import os
import time
import fnmatch
import shutil

#Function for log time
def timestamp (message):
	#a-> append, w-> write, r->read
	f=open(log,'a')
	f.write('\n' + time.strftime('%d/%m/%Y %H:%M:%S')+" <<Info>> : " + message)
	f.close()
	
	
reply = input ("\nDid you use your Privilege Account to run this script\n  If yes press 'y' if not press 'n'\n : ")

if (reply=="y" or reply=="Y"):
	print ("\nPlease give the location without using the quotes")
	
	#Common path in the folder structure
	Firstpath=input( "\nPlease provide the 'Common path' : ")
	#Converting "\" in path to "/"
	Firstpath=Firstpath.replace("\\","/")
	
	#Name of the folder that's going to be deleted must be unique
	Search=input("Please provide the name of folder to be deleted : ")
	
	log=input("Provide a location for log Eg - [D:\Log.txt] : ")
	
	#Declaring a list type variable
	mylist=[]
	
	for root,dirs,files in os.walk(Firstpath):
		for name in fnmatch.filter(dirs,Search):
			mylist.append((os.path.join(root,name)))
			
	num=len(mylist)
	
	timestamp("'cache' folder is found in "+str(num)+" paths")
	
	for delete in mylist:
		shutil.rmtree(delete)
		timestamp ("Removed "+delete)

else:
	print ("Please right click the cmd window and run as different user \n Terminating !!!!")
	quit()
