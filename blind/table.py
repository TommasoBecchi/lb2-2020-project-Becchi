import sys
from math import sqrt

def estrai_seq(op):
	f=open(op)
	for line in f:
		line=line.rstrip()
		if line[0]==">":continue
		return line

def aggiorna(table,n,pred):
	if pred=="H": table[n][0]+=1
	elif pred=="E": table[n][1]+=1
	elif pred=="-":table[n][2]+=1
	return table

def create_table(table,dssp,pred):
	for i in range (len(dssp)):
		if dssp[i]=="H": table=aggiorna(table,0,pred[i])
		elif dssp[i]=="E":table=aggiorna(table,1,pred[i])
		elif dssp[i]=="-":table=aggiorna(table,2,pred[i])
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
	lista =sys.argv[1]
	dssp_fold=sys.argv[2]
	pred_fold=sys.argv[3]
	table=[[0.0,0.0,0.0] for i in range (3)]
	f=open(lista)
	for nome in f:
		nome=nome.rstrip()
		dssp=dssp_fold+nome+".dssp"
		pred=pred_fold+nome+".pred"
		dssp_seq=estrai_seq(dssp)
		pred_seq=estrai_seq(pred)
		if len(dssp_seq)!=len(pred_seq): print "ERROR"
		table=create_table(table,dssp_seq,pred_seq)
	parameters(table)

	
	
