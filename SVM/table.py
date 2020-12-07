import sys
from math import sqrt

def estrai_seq(op):
	f=open(op)
	seq=""
	for line in f:
		line=line.rstrip()
		seq+=line[0]
	return seq

def aggiorna(table,n,pred):
	if pred=="1": table[n][0]+=1
	elif pred=="2": table[n][1]+=1
	elif pred=="3":table[n][2]+=1
	return table

def create_table(obs,pred):
	table=[[0.0 for i in range(3)] for i in range(3)]
	for i in range (len(obs)):
		if obs[i]=="1": table=aggiorna(table,0,pred[i])
		elif obs[i]=="2":table=aggiorna(table,1,pred[i])
		elif obs[i]=="3":table=aggiorna(table,2,pred[i])
	return table

def val (c,n,u,o):
	sen= c/(c+u)
	ppv=c/(c+o)
	den=(c+o)*(c+u)*(n+o)*(n+u)
	mcc=(c*n-o*u)/(sqrt(den))
	return sen,ppv,mcc

def parameters(table):
	ch=table[0][0]
	nh=table[2][2]+table[2][1]+table[1][1]+table[1][2]
	uh=table[0][1]+table[0][2]
	oh=table[1][0]+table[2][0]
	ce=table[1][1]
        ne=table[0][0]+table[0][2]+table[2][0]+table[2][2]
        ue=table[1][0]+table[1][2]
        oe=table[0][1]+table[2][1]
	cc=table[2][2]
        nc=table[0][0]+table[0][1]+table[1][0]+table[1][1]
        uc=table[2][0]+table[2][1]
        oc=table[0][2]+table[1][2]
	senh,ppvh,mcch=val(ch,nh,uh,oh)
	sene,ppve,mcce=val(ce,ne,ue,oe)
	senc,ppvc,mccc=val(cc,nc,uc,oc)
	tot=0
	for i in range(3):
		for j in range(3):
			tot+=table[i][j]
	q=(table[0][0]+table[1][1]+table[2][2])/tot
	print "H:",senh,ppvh,mcch
	print "E:",sene,ppve,mcce
	print "C:",senc,ppvc,mccc
	print "Q:",q



if __name__=='__main__':
	f_observed=sys.argv[1]
	f_predicted=sys.argv[2]
	obs=estrai_seq(f_observed)
	pred=estrai_seq(f_predicted)
	if len(obs)!=len(pred): print "ERROR"
	else:
		table=create_table(obs,pred)			
	parameters(table)
