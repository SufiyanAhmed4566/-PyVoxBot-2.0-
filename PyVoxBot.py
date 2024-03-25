import os 

if__name__="__main__";
print("welcome to PyVoxBot 2.0 by sufiyan")
while(True):
	os.system("hello its PyVoxBot   created by master sufiyan")
	a=input("enter the text you want me to speak:  ")

	if(a==exit):
		os.system("i am robospeaker is leaving now ")
		print("bye bye")
		break 
		
	command=f"say {a}";

	os.system(command)