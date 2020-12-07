import sys

def estrai_dssp(dss):
	f=open(dssp)
	for line in f:
		if line[0]==">":continue
		else: 
			line=line.rstrip()
			return line

def trasforma_prof(prof):
	f=open(prof)
	diz_prof={}
	c=0
	for line in f:
		line=line.rstrip()
		if line[0]=="\t":continue
		new_line=line[3:].split("\t")
		if new_line[0] in [" ",""]: new_line.pop(0)
		diz_prof[c]=[]
		for num in new_line:
			diz_prof[c].append(float(num))
		c+=1
	return diz_prof
			
def stampa (prof,dssp,win):
	diz_ss={"H":1, "E":2, "-":3}
	for i in range (len(dssp)):
		print diz_ss[dssp[i]],
		ind=1
		for k in range (-win/2+1,win/2+1):
			pos=i+k
			if pos<0 or pos>=len(dssp):
				ind+=20
				continue
			else:
				for num in diz_prof[pos]:
					if  num==0.0:
						ind+=1
						continue
					seq= str(ind)+":"+str(num)
					print seq.replace(" ",""),
					ind+=1
		print "\n",	
				
if __name__=='__main__':
	lista=sys.argv[1]
	dssp_folder=sys.argv[2]
	prof_folder=sys.argv[3]
	win=int(sys.argv[4])
	f=open(lista)
	for line in f:
		line=line.rstrip()
		prof=(prof_folder+line+".txt").replace(" ","")
		dssp=(dssp_folder+line+".dssp").replace(" ","")
		dssp_seq=estrai_dssp(dssp)
        	diz_prof=trasforma_prof(prof)
        	stampa(diz_prof,dssp_seq,win)
