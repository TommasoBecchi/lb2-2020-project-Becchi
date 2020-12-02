import sys


def crea_diz(win):
        amin="ACDEFGHILMNPQRSTVWYK"
        diz_h={}
        diz_e={}
        diz_c={}
        diz_tot={}
        for res in amin:
                diz_h[res]=[0.0 for i in range (win)]
                diz_e[res]=[0.0 for i in range (win)]
                diz_c[res]=[0.0 for i in range (win)]
                diz_tot[res]=[0.0 for i in range (win)]
        return diz_h,diz_e,diz_c,diz_tot

def estrai_ss(dssp):
        f=open(dssp)
        for line in f:
                line=line.rstrip()
                if line[0]==">": continue
                return line

def trasforma_prof (prof):
        f=open(prof)
        diz_prof={}
        c=0
        for line in f:
                line=line.rstrip()
                if line[0]=="\t":
                        s=""
                        for k in line: 
				if k!="\t" and k!=" ": s+=k
                else:
                        k_line=line[3:].replace("\t","")
                        new_line=k_line.replace(" ","-")
                        if new_line[0]=="-": new_line=new_line[1:]
                        new_line=new_line+"-"
                        i=0
                        diz_prof[int(c)]=[]
                        while i<(len(new_line)):
                                num=""
                                while new_line[i]!="-" and i<len(new_line):
                                        num+=new_line[i]
                                        i+=1
                                i+=1
                                diz_prof[c].append(float(num))
                        c+=1
        return diz_prof,s


def aggiorna_diz (diz_ss,n,seq,diz_prof,diz_tot,win):
        for i in range (-win//2+1,win//2+1):
                p=n+i
                if p<0 or p>=len(diz_prof.keys()):continue
                for k in range (20):
                        diz_ss[seq[k]][i+win//2]+=diz_prof[p][k]
                        diz_tot[seq[k]][i+win//2]+=diz_prof[p][k]
        return diz_ss,diz_tot

def stampa (diz,win,l,seq):
        for k in range (-win//2+1,win//2+1):
                print k,l,"\t",
                for i in range (20):
                        print diz[seq[i]][k+win//2],"\t",
                print "\n",

def normalizza(diz,norm):
        for k in diz.keys():
                for i in range (len(diz[k])):
                        diz[k][i]=round(diz[k][i]/norm[i],4)
        return diz
        
       
def principale (nome,dssp_folder,prof_folder,win,diz_h,diz_e,diz_c,diz_tot):
        dssp=dssp_folder+nome+"dssp"
        prof=prof_folder+nome+"txt"
        ss=estrai_ss(dssp)
        diz_prof,seq=trasforma_prof(prof)
        for n in range (len(ss)):
                x=ss[n]
                if x=="-": 
			cont[2]+=1
			diz_c,diz_tot=aggiorna_diz(diz_c,n,seq,diz_prof,diz_tot,win)
                elif x=="E":
			cont[1]+=1 
			diz_e,diz_tot=aggiorna_diz(diz_e,n,seq,diz_prof,diz_tot,win)
                elif x=="H":
			cont[0]+=1 
			diz_h,diz_tot=aggiorna_diz(diz_h,n,seq,diz_prof,diz_tot,win)
        return diz_h,diz_e,diz_c,diz_tot,seq,cont


if __name__=='__main__':
	lista=sys.argv[1]
	dssp_folder=sys.argv[2]
	prof_folder=sys.argv[3]
	win=int(sys.argv[4])
	diz_h,diz_e,diz_c,diz_tot=crea_diz(win)
	elenco=open(lista)
	cont=[0.0,0.0,0.0]
	for nome in elenco:
		nome=nome.rstrip()
		diz_h,diz_e,diz_c,diz_tot,seq,cont=principale(nome,dssp_folder,prof_folder,win,diz_h,diz_e,diz_c,diz_tot)
	norm=[0.0 for i in range (win)]
	for am in diz_tot.keys():
		for i in range (len(diz_tot[am])):
			norm[i]+=diz_tot[am][i]
	#print norm
	diz_h=normalizza(diz_h,norm)
        diz_e=normalizza(diz_e,norm)
        diz_c=normalizza(diz_c,norm)
        diz_tot=normalizza(diz_tot,norm)
        print "\t",
        for l in seq: print l,"\t",
        print "\n",
        stampa(diz_h,win,"H",seq)
        stampa(diz_e,win,"E",seq)
        stampa(diz_c,win,"C",seq)
        stampa(diz_tot,win,"",seq)
	v=["#H","#E","#C"]
	tot=0
	for i in cont:
		tot+=i
	for i in range(len(cont)):
		print v[i],"\t",round(cont[i]/tot,3)
