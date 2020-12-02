import sys
from math import log

def crea_diz(diz,line):
	new_line=line[3:].split("\t")
        new_line.pop(0)
	key=int(line[:2])
        diz[key]=[]
       	for num in new_line: diz[key].append(float(num))
	return diz

def trasforma_mod(mod):
	f=open(mod)
	diz_h={}
	diz_c={}
	diz_e={}
	diz_tot={}
	diz_ss={}
	for line in f:
		line=line.rstrip()
		if line[0]=="\t":
			s=line.split("\t")
			s.pop(0)
		elif line[0]!="#":
				if "H" in line: diz_h=crea_diz(diz_h,line)
				elif "E" in line: diz_e=crea_diz(diz_e,line)
				elif "C" in line: diz_c=crea_diz(diz_c,line)
				else: diz_tot= crea_diz(diz_tot,line)
		else:
			diz_ss[line[1]]=float(line[3:])

	return diz_h,diz_e,diz_c,diz_tot,diz_ss,s

def trasforma_prof(prof):
	f=open(prof)
        diz_prof={}
        c=0
        for line in f:
                line=line.rstrip()
                if line[0]=="\t": continue
                else:
			new_line=line[3:].split("\t")
			if new_line[0] in [" ",""]: new_line.pop(0)
			key=int(line[:3])
			diz_prof[key]=[]
			for num in new_line:
				diz_prof[key].append(float(num))
        return diz_prof

def information (diz,diz_tot,pss):
	info={}
	for d in diz.keys():
		info[d]=[]
		for i in range (len(diz[d])):
			arg=diz[d][i]/(diz_tot[d][i]*pss)
			info[d].append(round((log(arg,2)),4))
			
	return info

def prob(prof,info,i):
	tot=0
	for d in info.keys():
		pos=i+d
		if pos<=0 or pos>len(prof.keys()):continue
		for k in range (20):
			tot+= info[d][k]*prof[pos][k]
	return tot
 
def predicting(prof,info_h,info_e,info_c):
	s=""
	for i in prof.keys():
		prob_h=prob(prof,info_h,i)
		prob_e=prob(prof,info_e,i)
		prob_c=prob(prof,info_c,i)
		if max(prob_h,prob_e,prob_c)==prob_h: s+="H"
		elif max(prob_h,prob_e,prob_c)==prob_c: s+="-"
		else: s+="E"
	return s	

if  __name__=='__main__':
	prof=sys.argv[1]
	mod=sys.argv[2]
	dir_output=sys.argv[3]
	'''header=prof.replace(".","")
	header=header.replace("/","")
	header=header[:len(header)-3]'''
	header=prof.split("/")
	nome=header[len(header)-1]
	first=">"+nome[:len(nome)-4]
	diz_h,diz_e,diz_c,diz_tot,diz_ss,seq=trasforma_mod(mod)
	diz_prof=trasforma_prof(prof)
	info_h=information(diz_h,diz_tot,diz_ss["H"])
	info_e=information(diz_e,diz_tot,diz_ss["E"])
	info_c=information(diz_c,diz_tot,diz_ss["C"])
	result=predicting(diz_prof,info_h,info_e,info_c)
	nome=dir_output+nome[:len(nome)-4]+".pred"
	fres=open(nome,"w")
	contenuto=first+"\n"+result
	fres.write(contenuto)
	fres.close()	
