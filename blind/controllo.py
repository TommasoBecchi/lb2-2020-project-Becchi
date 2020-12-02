import sys

def controllo(prof):
	f=open(prof)
	riga=1
	buono=["0","1","2","3","4","5","6","7","8","9","."]
	for line in f:
		if riga==1: 
			riga+=1
			continue
		valori=line[3:]
		p=0
		lista=[]
		while p<len(valori):
			num=""
			while valori[p] in buono:
				num+=valori[p]
				p+=1
			if len(num)>0: lista.append(float(num))
			if len(lista)==20: break
			p+=1
		for k in lista:
			if k>0: return False	
	
	return True

if __name__=='__main__':
	prof=sys.argv[1]
	if controllo(prof):
		print prof
