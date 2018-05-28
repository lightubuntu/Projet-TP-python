import math

def carré_parfait(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
             return 1
    else:
            return 0
def produit(liste):
    p = 1
    for i in liste:
        p *= i
    return p
def sous_ensembles(s):
	
	if len(s) == 0:
		return [[]]
	
	h, t = s[0], s[1:]
	ss_excl_h = sous_ensembles(t)
	ss_incl_h = [([h] + ss) for ss in ss_excl_h]
	return ss_incl_h + ss_excl_h
def C(a,b):
    nb=0
    
    for i in sous_ensembles(range(a,b+1)):
        
        j=produit(i)
        t=carré_parfait(j)
        
    
        
        if t == 1:
            nb = nb+1
            
    return nb-1


