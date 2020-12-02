import sys

def extract(pssm):
	f=open(pssm)
	riga=1
	for line in f:
		line=line.rstrip()
		if riga<3:
			riga+=1
			continue
		if line=="": break
		if riga==3:
			if line[88]=="V":
				p=92
				f=170
			elif line[68]=="V":
				p=72
				f=150
			print "\t",
			s=line[p:]
			for i in s: 
				if i !=" ": print i,"\t",
		else:
			pos=int(line[2:5])
			valori=line[p-1:f]
			lista=[pos]
			for i in range(0,len(valori),4):
				lista.append(int(valori[i:i+4])/100.0)
			for k in lista: print k,"\t",
		print "\n", 	
		riga+=1

if __name__=='__main__':
	pssm=sys.argv[1]
	extract(pssm)
