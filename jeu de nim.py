from random import randint
import sys






        
tas = [randint(1, 50), randint(1, 50), randint(1, 50),randint(1, 50)]  
print("Bienvenue ou NIM!! Les tas sont {}" .format(tas))
joueur1=input("donner le nom de 1er joueur ?")
joueur2=input("donner le nom de 2eme joueur ?")

pl=joueur1
score=0
y=1

print ("Joueur",repr(pl),"a jouer.")
while True:
        
        pc=int(input("Voulez-vous choisir les pierres à retirer de tas 1 ou 2 ou 3 ou 4 ?  "))
        if pc in [1,2,3,4] and tas[pc-1]!=0:
                while True:
                        pcoi=int(input("Donner le Nombre de pierres à retire de cette tas:"))
                        if 0<pcoi<=tas[pc-1] :
                                tas[pc-1] -= pcoi
                                print("Les tas maintenant contenir {}" .format(tas))
                                x=sum(tas)
                                if x==1:
                                        if pl==joueur1:
                                                score = sum(i*(10**i) for i in range(0,y+1))
                                                print ("Félicitations!!!",repr(pl),"a gagné avec un score de",repr(score))
                                        else:
                                                score = sum(i*(10**i) for i in range(0,y))
                                                print ("Félicitations!!!",repr(pl),"a gagné avec un score de",repr(score))
                                                print ("Jeu terminer.")
                                        sys.exit(0)
                                                
                                elif x==0:
                                        if pl==joueur1:
                                                score = sum(i*(10**i) for i in range(0,y))
                                                print ("Félicitations!!!",repr(joueur2),"a gagné avec un score de",repr(score))
                                                
                                        else:
                                                score = sum(i*(10**i) for i in range(0,y))
                                                print ("Félicitations!!!",repr(joueur1),"a gagné avec un score de",repr(score))
                                                print ("Jeu terminer.")
                                  
                                        sys.exit(0)
                                if pl==joueur1:
                                        
                                        pl=joueur2
                                        y = y+1
                                else :
                                        
                                        
                                        pl=joueur1
                                       
                                
                                print("Joueur",repr(pl),"a jouer.")
                                break
                        
                        else:
                                print("Nombre de pierres à retirer est invalid. Veuillez réessayer!")
                        
        else:
                print("Numéro du tas est invalid. Veuillez réessayer!")


        
