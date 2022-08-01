#!/usr/bin/env python3.5 

import sys

# Batch

# Constantes
pbloc="01/07/2023" # Date de bascule dans la nouvelle grille des GND MDC ADJ
sbloc="01/01/2024" # Date de bascule dans la nouvelle grille des ADC MJR

# Grille ancienne
# Indice , Ancienneté dans l'échelon , Ancienneté de service
aindices_gnd=[[343,348,353,364,379,391,401,411,422,435,454,477],[24,24,24,24,30,30,30,36,36,36,42,999],[0,0,0,0,0,0,0,0,0,0,0,0]]
aindices_mdc=[[388,398,412,426,445,463,481],[42,42,36,36,0,0,0],[0,10,13,18,21,24,27]]
aindices_adj=[[422,429,439,449,467,473,482,484,503],[36,36,36,36,36,24,24,36,36],[0,0,0,18,21,24,27,30,33]]
aindices_adc=[[466,476,484,488,493,505,517,527,539],[24,36,36,36,42,36,36,36,36],[0,0,21,24,26.5,28.5,30.5,32.5,34.5]]
aindices_mjr=[[495,515,536,550,564,574,590],[36,42,36,36,36,36,0],[0,27,29,31,33,35,0]]

# Grille nouvelle
nindices_gnd=[[351,357,366,382,389,405,419,434,453,470,488,506,527],[12,12,18,24,24,24,24,30,30,30,30,30,999]]
nindices_mdc=[[389,405,419,434,453,470,488,506,527],[24,24,24,30,30,30,30,30,999]]
nindices_adj=[[419,434,453,470,488,506,527],[24,30,30,30,30,30,999]]
nindices_adc=[[473,484,503,513,523,543,560],[24,30,30,30,30,36,999]]
nindices_mjr=[[510,530,544,562,574,610],[24,24,24,30,30,999]]
nindices_mef=[[615,635,655,685],[24,24,24,999]]

def Reclassement_simple(grade,aindice,ancienneteservice,ancienneteechelon) :
    # Le grade doit être au format des if
    # Gestion des échelons sans anciennete de service ou d'échelon terminale ////////****************//////////////************
    # Gendarme
    if grade.upper()=="GENDARME":
        i=0
        while aindice>nindices_gnd[0][i] :
            i=i+1
        # Ancienneté d'échelon
        # Recherche duree de l'echelon correspondant à l'indice nouveau
        dureen=nindices_gnd[1][nindices_gnd[0].index(nindices_gnd[0][i])]
        # Recherche duree echelon ancien
        dureea=aindices_gnd[1][aindices_gnd[0].index(aindice)]
        if dureea==0: # Passage à l'ancienneté de service
                dureea=(aindices_gnd[2][aindices_gnd[0].index(aindice)+1]-aindices_gnd[2][aindices_gnd[0].index(aindice)])*12
        reprise_e=round(ancienneteechelon*dureen/dureea)
        print("Reprise ancienneté échelon :",reprise_e)
        return nindices_gnd[0][i],reprise_e
    # MDC
    elif grade.upper()=="MDC":
        i=0
        while aindice>nindices_mdc[0][i] :
            i=i+1
        # Recherche duree de l'echelon correspondant à l'indice nouveau
        dureen=nindices_mdc[1][nindices_mdc[0].index(nindices_mdc[0][i])]
        # Recherche duree echelon ancien
        dureea=aindices_mdc[1][aindices_mdc[0].index(aindice)]
        if dureea==0: # Passage à l'ancienneté de service
                dureea=(aindices_mdc[2][aindices_mdc[0].index(aindice)+1]-aindices_mdc[2][aindices_mdc[0].index(aindice)])*12
        reprise_e=round(ancienneteechelon*dureen/dureea)
        # Recherche par l'ancienneté de service ancienne grille
        dureeas=(aindices_mdc[2][aindices_mdc[0].index(aindice)+1]-aindices_mdc[2][aindices_mdc[0].index(aindice)])*12
        reprise_s=round(ancienneteechelon*dureen/(aindices_mdc[2][aindices_mdc[0].index(aindice)+1]*12 -(ancienneteservice*12-ancienneteechelon)))
        print("Reprise ancienneté échelon :",reprise_e)
        print("Reprise ancienneté service :",reprise_s)
        if reprise_e>reprise_s:
            reprise=reprise_e
        else:
            reprise=reprise_s      
        return nindices_mdc[0][i],reprise
    
    elif grade.upper()=="ADJ":
        i=0
        while aindice>nindices_adj[0][i] :
            i=i+1
        # Recherche duree de l'echelon correspondant à l'indice nouveau
        dureen=nindices_adj[1][nindices_adj[0].index(nindices_adj[0][i])]
        # Recherche duree echelon ancien
        dureea=aindices_adj[1][aindices_adj[0].index(aindice)]
        if dureea==0: # Passage à l'ancienneté de service
                dureea=(aindices_adj[2][aindices_adj[0].index(aindice)+1]-aindices_adj[2][aindices_adj[0].index(aindice)])*12
        reprise_e=round(ancienneteechelon*dureen/dureea)
        # Recherche par l'ancienneté de service ancienne grille
        dureeas=(aindices_adj[2][aindices_adj[0].index(aindice)+1]-aindices_adj[2][aindices_adj[0].index(aindice)])*12
        reprise_s=round(ancienneteechelon*dureen/(aindices_adj[2][aindices_adj[0].index(aindice)+1]*12 -(ancienneteservice*12-ancienneteechelon)))
        print("Reprise ancienneté échelon :",reprise_e)
        print("Reprise ancienneté service :",reprise_s)
        if reprise_e>reprise_s:
            reprise=reprise_e
        else:
            reprise=reprise_s      
        return nindices_adj[0][i],reprise
    elif grade.upper()=="ADC":
        i=0
        while aindice>nindices_adc[0][i] :
            i=i+1
        # Recherche duree de l'echelon correspondant à l'indice nouveau
        dureen=nindices_adc[1][nindices_adc[0].index(nindices_adc[0][i])]
        # Recherche duree echelon ancien
        dureea=aindices_adc[1][aindices_adc[0].index(aindice)]
        if dureea==0: # Passage à l'ancienneté de service
                dureea=(aindices_adc[2][aindices_adc[0].index(aindice)+1]-aindices_adc[2][aindices_adc[0].index(aindice)])*12
        reprise_e=round(ancienneteechelon*dureen/dureea)
        # Recherche par l'ancienneté de service ancienne grille
        dureeas=(aindices_adc[2][aindices_adc[0].index(aindice)+1]-aindices_adc[2][aindices_adc[0].index(aindice)])*12
        reprise_s=round(ancienneteechelon*dureen/(aindices_adc[2][aindices_adc[0].index(aindice)+1]*12 -(ancienneteservice*12-ancienneteechelon)))
        print("Reprise ancienneté échelon :",reprise_e)
        print("Reprise ancienneté service :",reprise_s)
        if reprise_e>reprise_s:
            reprise=reprise_e
        else:
            reprise=reprise_s      
        return nindices_adc[0][i],reprise
    elif grade.upper()=="MJR":
        i=0
        while aindice>nindices_mjr[0][i] :
            i=i+1
        # Recherche duree de l'echelon correspondant à l'indice nouveau
        dureen=nindices_mjr[1][nindices_mjr[0].index(nindices_mjr[0][i])]
        # Recherche duree echelon ancien
        dureea=aindices_mjr[1][aindices_mjr[0].index(aindice)]
        if dureea==0: # Passage à l'ancienneté de service
                dureea=(aindices_mjr[2][aindices_mjr[0].index(aindice)+1]-aindices_mjr[2][aindices_mjr[0].index(aindice)])*12
        reprise_e=round(ancienneteechelon*dureen/dureea)
        # Recherche par l'ancienneté de service ancienne grille
        dureeas=(aindices_mjr[2][aindices_mjr[0].index(aindice)+1]-aindices_mjr[2][aindices_mjr[0].index(aindice)])*12
        reprise_s=round(ancienneteechelon*dureen/(aindices_mjr[2][aindices_mjr[0].index(aindice)+1]*12 -(ancienneteservice*12-ancienneteechelon)))
        print("Reprise ancienneté échelon :",reprise_e)
        print("Reprise ancienneté service :",reprise_s)
        if reprise_e>reprise_s:
            reprise=reprise_e
        else:
            reprise=reprise_s      
        return nindices_mjr[0][i],reprise

def Reclassement_terminal(grade,aindice,ancienneteservice,ancienneteechelon) :
    if grade.upper()=="GENDARME":
        nindice=488
        if ancienneteechelon>nindices_gnd[1][nindices_gnd[0].index(488)]:
            nindice=506
            # Recherche duree de l'echelon correspondant à l'indice nouveau
            dureen=nindices_gnd[1][nindices_gnd[0].index(nindice)]
            # On retire la durée de l'échelon correspondant à l'indice 488
            reprise=round(((ancienneteechelon-nindices_gnd[1][nindices_gnd[0].index(488)]))/((34-ancienneteservice)*12)*dureen) # 34 années de service pour une carrière complète
        else:
            # Maintien de son ancienneté d'échelon mais reprise à proportion de la durée du nouvel échelon
            dureen=nindices_gnd[1][nindices_gnd[0].index(nindice)]
            reprise=round(ancienneteechelon/((34-ancienneteservice)*12)*dureen)              
        return nindice,reprise
    # MDC
    elif grade.upper()=="MDC":
        nindice=488
        if ancienneteechelon>nindices_mdc[1][nindices_mdc[0].index(488)]:
            nindice=506
            # Recherche duree de l'echelon correspondant à l'indice nouveau
            dureen=nindices_mdc[1][nindices_mdc[0].index(nindice)]
            # On retire la durée de l'échelon correspondant à l'indice 488
            reprise=round(((ancienneteechelon-nindices_mdc[1][nindices_mdc[0].index(488)]))/((34-ancienneteservice)*12)*dureen) # 34 années de service pour une carrière complète
        else:
            # Maintien de son ancienneté d'échelon mais reprise à proportion de la durée du nouvel échelon
            dureen=nindices_mdc[1][nindices_mdc[0].index(nindice)]
            reprise=round(ancienneteechelon/((34-ancienneteservice)*12)*dureen)              
        return nindice,reprise
    #ADJ    
    elif grade.upper()=="ADJ":
        nindice=506
        if ancienneteechelon>nindices_adj[1][nindices_adj[0].index(506)]:
            nindice=527
            # Recherche duree de l'echelon correspondant à l'indice nouveau
            dureen=nindices_adj[1][nindices_adj[0].index(nindice)]
            # On retire la durée de l'échelon correspondant à l'indice 506
            reprise=round(((ancienneteechelon-nindices_adj[1][nindices_adj[0].index(506)]))/((34-ancienneteservice)*12)*dureen) # 34 années de service pour une carrière complète
        else:
            # Maintien de son ancienneté d'échelon mais reprise à proportion de la durée du nouvel échelon
            dureen=nindices_adj[1][nindices_adj[0].index(nindice)]
            reprise=round(ancienneteechelon/((34-ancienneteservice)*12)*dureen)              
        return nindice,reprise
    #ADC
    elif grade.upper()=="ADC":
        nindice=543
        if ancienneteechelon>nindices_adc[1][nindices_adc[0].index(543)]:
            nindice=560
            # Recherche duree de l'echelon correspondant à l'indice nouveau
            dureen=nindices_adc[1][nindices_adc[0].index(nindice)]
            # On retire la durée de l'échelon correspondant à l'indice 488
            reprise=round(((ancienneteechelon-nindices_adc[1][nindices_adc[0].index(488)]))/((34-ancienneteservice)*12)*dureen) # 34 années de service pour une carrière complète
        else:
            # Maintien de son ancienneté d'échelon mais reprise à proportion de la durée du nouvel échelon
            dureen=nindices_adc[1][nindices_adc[0].index(nindice)]
            reprise=round(ancienneteechelon/((34-ancienneteservice)*12)*dureen)              
        return nindice,reprise
    elif grade.upper()=="MJR":             
        return 610,ancienneteechelon

def Reclassement_multiple(grade,aindice,ancienneteservice,ancienneteechelon) :
    if grade.upper()=="EG":
        nindice=340 # Indice EG 340 ou 343 ?
        reprise=ancienneteechelon
        return nindice,reprise
        
    elif grade.upper()=="GENDARME":
        if aindice==343:
            nindice=351
            reprise=round(ancienneteechelon/(aindices_gnd[1][aindices_gnd[0].index(aindice)+1]+aindices_gnd[1][aindices_gnd[0].index(aindice)])*12)
        elif aindice==348:
            nindice=351
            reprise=round((ancienneteechelon+aindices_gnd[1][aindices_gnd[0].index(aindice)])/(aindices_gnd[1][aindices_gnd[0].index(aindice)+1]+aindices_gnd[1][aindices_gnd[0].index(aindice)])*12)
        elif aindice==391:
            nindice=405
            reprise=round(ancienneteechelon/(aindices_gnd[1][aindices_gnd[0].index(aindice)+1]+aindices_gnd[1][aindices_gnd[0].index(aindice)])*12)
        elif aindice==401:
            nindice=405
            reprise=round((ancienneteechelon+aindices_gnd[1][aindices_gnd[0].index(aindice)])/(aindices_gnd[1][aindices_gnd[0].index(aindice)+1]+aindices_gnd[1][aindices_gnd[0].index(aindice)])*12)
        return nindice,reprise
    # MDC aucune situation
    #ADJ    
    elif grade.upper()=="ADJ":
        if aindice==473:
            nindice=488
            reprise_e=round(ancienneteechelon/(aindices_adj[1][aindices_adj[0].index(aindice)+2]+aindices_adj[1][aindices_adj[0].index(aindice)+1]+aindices_adj[1][aindices_adj[0].index(aindice)])*30)
            reprise_s=round(ancienneteechelon/(12*(aindices_adj[2][aindices_adj[0].index(484)+1]-aindices_adj[2][aindices_adj[0].index(473)]))*30)
        elif aindice==482:
            nindice=488
            reprise_e=round((ancienneteechelon+aindices_adj[1][aindices_adj[0].index(aindice)-1])/(aindices_adj[1][aindices_adj[0].index(aindice)-1]+aindices_adj[1][aindices_adj[0].index(aindice)+1]+aindices_adj[1][aindices_adj[0].index(aindice)])*30)
            reprise_s=round((ancienneteechelon+12*(aindices_adj[2][aindices_adj[0].index(482)]-aindices_adj[2][aindices_adj[0].index(473)]))/(12*(aindices_adj[2][aindices_adj[0].index(484)+1]-aindices_adj[2][aindices_adj[0].index(473)]))*30)
        elif aindice==484:
            nindice=488
            reprise_e=round((ancienneteechelon+aindices_adj[1][aindices_adj[0].index(aindice)-1]+aindices_adj[1][aindices_adj[0].index(aindice)-2])/(aindices_adj[1][aindices_adj[0].index(aindice)-2]+aindices_adj[1][aindices_adj[0].index(aindice)-1]+aindices_adj[1][aindices_adj[0].index(aindice)])*30)
            reprise_s=round((ancienneteechelon+12*(aindices_adj[2][aindices_adj[0].index(484)]-aindices_adj[2][aindices_adj[0].index(473)]))/(12*(aindices_adj[2][aindices_adj[0].index(484)+1]-aindices_adj[2][aindices_adj[0].index(473)]))*30)
        elif aindice==422:
            nindice=434
            reprise_e=round(ancienneteechelon/(aindices_adj[1][aindices_adj[0].index(aindice)+1]+aindices_adj[1][aindices_adj[0].index(aindice)])*30)
            reprise_s=0
        elif aindice==429:
            nindice=434
            reprise_e=round((ancienneteechelon+aindices_adj[1][aindices_adj[0].index(aindice)-1])/(aindices_adj[1][aindices_adj[0].index(aindice)-1]+aindices_adj[1][aindices_adj[0].index(aindice)])*30)
            reprise_s=0
        elif aindice==439:
            nindice=453
            reprise_e=round(ancienneteechelon/(aindices_adj[1][aindices_adj[0].index(aindice)+1]+aindices_adj[1][aindices_adj[0].index(aindice)])*30)
            reprise_s=0
        elif aindice==449:
            nindice=453
            reprise_e=round((ancienneteechelon+aindices_adj[1][aindices_adj[0].index(aindice)-1])/(aindices_adj[1][aindices_adj[0].index(aindice)-1]+aindices_adj[1][aindices_adj[0].index(aindice)])*30)
            reprise_s=round((ancienneteechelon+12*3)/(12*(6))*30) # Pas de borne inférieure au 3ème échelon, on ajoute à la main 3 ans soit 6 ans pour les deux échelons
        print("Reprise_e:",reprise_e)
        print("Reprise_s:",reprise_s)
        if reprise_e>reprise_s:
            reprise=reprise_e
        else:
            reprise=reprise_s
        return nindice,reprise
    #ADC 
    elif grade.upper()=="ADC":
        if aindice==476:
            nindice=484
            reprise_e=round(ancienneteechelon/(aindices_adc[1][aindices_adc[0].index(aindice)+1]+aindices_adc[1][aindices_adc[0].index(aindice)])*30)
            reprise_s=round(ancienneteechelon/(12*6)*30) # Pas de borne inférieure au 2ème échelon, on ajoute à la main 3 ans soit 6 ans pour les deux échelons
        elif aindice==484:
            nindice=484
            reprise_e=round((ancienneteechelon+aindices_adc[1][aindices_adc[0].index(aindice)-1])/(aindices_adc[1][aindices_adc[0].index(aindice)-1]+aindices_adc[1][aindices_adc[0].index(aindice)])*30)
            reprise_s=round((ancienneteechelon+12*3)/(12*6)*30) # Pas de borne inférieure au 2ème échelon, on ajoute à la main 3 ans soit 6 ans pour les deux échelons
        elif aindice==488:
            nindice=503
            reprise_e=round(ancienneteechelon/(aindices_adc[1][aindices_adc[0].index(aindice)-1]+aindices_adc[1][aindices_adc[0].index(aindice)])*30)
            reprise_s=round((ancienneteechelon)/(12*6.5)*30) # Codage en dur des durées
        elif aindice==493:
            nindice=503
            reprise_e=round(ancienneteechelon/(aindices_adc[1][aindices_adc[0].index(aindice)+1]+aindices_adc[1][aindices_adc[0].index(aindice)])*30)
            reprise_s=round((ancienneteechelon+12*3.5)/(12*6.5)*30) # Codage en dur des durées
        print("Reprise_e:",reprise_e)
        print("Reprise_s:",reprise_s)
        if reprise_e>reprise_s:
            reprise=reprise_e
        else:
            reprise=reprise_s
        return nindice,reprise
    #MJR
    elif grade.upper()=="MJR":
        if aindice==564:
            nindice=574
            reprise_e=round(ancienneteechelon/(aindices_mjr[1][aindices_mjr[0].index(aindice)+1]+aindices_mjr[1][aindices_mjr[0].index(aindice)])*30)
            reprise_s=round((ancienneteechelon)/(12*5)*30) # Duree des deux échelons 5 ans 2 pour le 5 et 3 pour le 6 qui est terminal sauf échelon exceptionnel
        elif aindice==574:
            nindice=574
            reprise_e=round((ancienneteechelon+aindices_mjr[1][aindices_mjr[0].index(aindice)-1])/(aindices_mjr[1][aindices_mjr[0].index(aindice)-1]+aindices_mjr[1][aindices_mjr[0].index(aindice)])*30)
            reprise_s=round((ancienneteechelon+2*12)/(12*5)*30) # Duree des deux échelons 5 ans 2 pour le 5 et 3 pour le 6 qui est terminal sauf échelon exceptionnel
    if reprise_e>reprise_s:
        reprise=reprise_e
    else:
        reprise=reprise_s
    return nindice,reprise

def Affiche(gendarme):
    a="Grade: "+gendarme[0]+" Indice actuel: "+str(gendarme[1])+"\nAncienneté de service: "+str(gendarme[2])+" années \nAncienneté d'échelon: "+str(gendarme[3])+" mois\n"
    #print(a)
    situation=Identif_reclasse(gendarme)
    b="Nouvel indice: "+str(situation[0])+ "Nouvelle ancienneté dans l'échelon: "+str(situation[1])+" mois\n"
    ##print(b)
    c="***************\n"
    return a+b+c

# identification de la situation
def Identif_reclasse(gendarme):
    grade,aindice,ancienneteservice,ancienneteechelon=gendarme
    uni=[353,364,379,388,398,411,412,422,426,429,435,445,454,463,466,467,495,505,515,517,536,550]
    mul=[343,348,391,401,439,449,473,476,482,484,488,493,527,564,574]
    term=[477,481,503,539,590]
    if aindice in uni:
        reclasse=Reclassement_simple(grade,aindice,ancienneteservice,ancienneteechelon)
    elif aindice in term:
        reclasse=Reclassement_terminal(grade,aindice,ancienneteservice,ancienneteechelon)
    elif aindice in mul:
        reclasse=Reclassement_multiple(grade,aindice,ancienneteservice,ancienneteechelon)
    return reclasse

# Calcul différence de dates en mois annee
def Diffdate(date1,date2):
    d2=date2.split("/")
    d1=date1.split("/")
    d2=list(map(int,d2))
    d1=list(map(int,d1))
    a=a=d2[2]-d1[2]-1
    if (d2[1]>d1[1] or (d2[1]==d1[1] and d2[0]>=d1[0])):
        a=a+1
    else:
        d2[1]=d2[1]+12
    m=d2[1]-d1[1]-1
    if d2[0]>=d1[0]:
        m=m+1
        a=d2[2]-d1[2]
    return a,m
        

# Calcul de l'ancienneté d'échelon à la date de passage dans la nouvelle grille
def Calculancienneteechelon(grade,aindice,de):
    # Recherche date de bascule dans la nouvelle grille
    if (grade=="ADC" or grade=="MJR"):
        dateb=sbloc
    else:
        dateb=pbloc
    aeb=Diffdate(de,dateb)
    # Vérification qu'il ne franchit pas d'échelon dans la période
    if grade.upper()=="EG":
        dureea=12
        if dureea<(aeb[0]*12+aeb[1]): # Changement de grade dans la période
            gendarme=["GENDARME",aindices_gnd[0][0],aeb[0]*12+aeb[1]-dureea]
        else:
            gendarme=[grade,aindice,aeb[0]*12+aeb[1]]
    elif grade.upper()=="GENDARME":
        i=0
        while aindice>nindices_gnd[0][i] :
            i=i+1
        # Recherche duree echelon ancien
        dureea=aindices_gnd[1][aindices_gnd[0].index(aindice)]
        if dureea<(aeb[0]*12+aeb[1]): # Changement d'échelon dans la période
            gendarme=[grade,aindices_gnd[0][aindices_gnd[0].index(aindice)+1],aeb[0]*12+aeb[1]-dureea]
        else:
            gendarme=[grade,aindice,aeb[0]*12+aeb[1]]

    elif grade.upper()=="MDC":
        i=0
        while aindice>nindices_mdc[0][i] :
            i=i+1
        # Recherche duree echelon ancien
        dureea=aindices_mdc[1][aindices_mdc[0].index(aindice)]
        if dureea<(aeb[0]*12+aeb[1]): # Changement d'échelon dans la période
            gendarme=[grade,aindices_mdc[0][aindices_mdc[0].index(aindice)+1],aeb[0]*12+aeb[1]-dureea]
        else:
            gendarme=[grade,aindice,aeb[0]*12+aeb[1]]
    elif grade.upper()=="ADJ":
        i=0
        while aindice>nindices_adj[0][i] :
            i=i+1
        # Recherche duree echelon ancien
        dureea=aindices_adj[1][aindices_adj[0].index(aindice)]
        if dureea<(aeb[0]*12+aeb[1]): # Changement d'échelon dans la période
            gendarme=[grade,aindices_adj[0][aindices_adj[0].index(aindice)+1],aeb[0]*12+aeb[1]-dureea]
        else:
            gendarme=[grade,aindice,aeb[0]*12+aeb[1]]
    elif grade.upper()=="ADC":
        i=0
        while aindice>nindices_adc[0][i] :
            i=i+1
        # Recherche duree echelon ancien
        dureea=aindices_adc[1][aindices_adc[0].index(aindice)]
        if dureea<(aeb[0]*12+aeb[1]): # Changement d'échelon dans la période
            gendarme=[grade,aindices_adc[0][aindices_adc[0].index(aindice)+1],aeb[0]*12+aeb[1]-dureea]
        else:
            gendarme=[grade,aindice,aeb[0]*12+aeb[1]]
    elif grade.upper()=="MJR":
        i=0
        while aindice>nindices_mjr[0][i] :
            i=i+1
        # Recherche duree echelon ancien
        dureea=aindices_mjr[1][aindices_mjr[0].index(aindice)]
        if dureea<(aeb[0]*12+aeb[1]): # Changement d'échelon dans la période
            gendarme=[grade,aindices_mjr[0][aindices_mjr[0].index(aindice)+1],aeb[0]*12+aeb[1]-dureea]
        else:
            gendarme=[grade,aindice,aeb[0]*12+aeb[1]]
    return gendarme


# Ouverture fichier
entree='/var/www/html/cimm/indice/groupe/FileOutput.csv'
fichier = open('/var/www/html/cimm/indice/groupe/FileInput.csv', 'r',encoding='utf-8')
res=open(entree,'w+',encoding='utf-8')
i=1
for ligne in fichier:
    i=i+1
    if i==10:
        break
    x=ligne.split(",")
    nigend=x[0]
    if x[3]=="élève gendarme":
        grade="EG"
        aindice=343
    elif x[3]=="gendarme":
        grade="GENDARME"
        aindice=aindices_gnd[0][int(x[5])-1]
    elif x[3]=="maréchal des logis-chef":
        grade="MDC"
        aindice=aindices_mdc[0][int(x[5])-1]
    elif x[3]=="adjudant":
        grade="ADJ"
        aindice=aindices_adj[0][int(x[5])-1]
    elif x[3]=="adjudant-chef":
        grade="ADC"
        aindice=aindices_adc[0][int(x[5])-1]
    elif x[3]=="major":
        grade="MJR"
        aindice=aindices_mjr[0][int(x[5])-1]
    ans=float(x[7])+float(x[8])/12 # Si la date d'entrée en service est donnée, je peux recalculer avec diffdate()
    # Calcul de l'ancienneté d'échelon à la date du changement de grille
    ret=Calculancienneteechelon(grade,aindice,x[9]) # renvoi un tableau grade, indice majoré (éventuellement nouveau s'il y a eu changement d'échelon), ancienneté dans l'échelon à la date de changement de grille
    #print(ret)
    if ret[1]==aindice:
        gendarme=[ret[0],aindice,ans,ret[2]]
    else:
        gendarme=[ret[0],ret[1],ans,ret[2]]
    # Ecrire le résultat dans le fichier
    Identif_reclasse(gendarme)
    res.write(str(Affiche(gendarme)))
fichier.close()
res.close()

