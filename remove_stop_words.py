import pickle
import re
infile = "data_with_stop.txt"
outfile = "cleanedfile600.txt"

stop=open('stop words.txt','r')
delete_list= stop.readline().split()

fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
	line=line.lower()	
	line=line.split()
    	'''for word in delete_list:
		print line.remove(word)	
	'''
	l3 = [x for x in line if x not in delete_list] 
	regex = re.compile('[^a-zA-Z]')   	
	for k in range(0, len(l3)):
		regex = re.compile('[^a-zA-Z]') 
		l3[k] = regex.sub('', l3[k])
		fout.write(l3[k])
		fout.write(" ")
	fout.write("\n")	
	'''print l3	
	fout.write(l3)
	'''
	
fin.close()
fout.close()


