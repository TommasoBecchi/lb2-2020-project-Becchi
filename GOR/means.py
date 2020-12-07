import sys
import statistics
from math import sqrt

def mean_and_sd(lista,n):
	elenco=[]
	for i in lista:
		elenco.append(float(i[n]))
	sd=statistics.stdev(elenco)
	se=round(sd/(sqrt(5)),4)
	m=round(statistics.mean(elenco),4)
	return [m,se]

def calcolo(lista):
	sen=mean_and_sd(lista,0)
	ppv=mean_and_sd(lista,1)
	mcc=mean_and_sd(lista,2)
	return sen,ppv,mcc

if __name__=="__main__":
	valori=sys.argv[1]
	diz={"H":[],"E":[],"C":[],"Q":[]}
	f=open(valori)
	for line in f:
		line=line.rstrip()
		new_line=line[3:].split(" ")
		diz[line[0]].append(new_line)
	mh1,mh2,mh3=calcolo(diz["H"])
	me1,me2,me3=calcolo(diz["E"])
	mc1,mc2,mc3=calcolo(diz["C"])
	mq=mean_and_sd(diz["Q"],0)
	val=[["H",mh1,mh2,mh3],["E",me1,me2,me3],["C",mc1,mc2,mc3]]
	tit=["sen:","ppv:","mcc:"]
	for i in val:
		for j in range (len(i)):
			if j==0: print (i[j])
			else: print (tit[j-1],i[j][0],"~",i[j][1])
	print ("Q3:",mq[0],"~",mq[1])
