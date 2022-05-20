import numpy as np
import matplotlib.pyplot as plt

prix_bien = 236000
taux_annuel_CIC = 1.08/100

### Prix Notaire

remise_emoluments = False

def calcul_frais_de_notaire(prix_bien : int = 236000, remise_emoluments : bool = False):
    prix_mutation = 5.80665/100 * prix_bien
    Etat = max(15, 0.10/100 * prix_bien)
    formalite_frais_divers = 800 + 400
    prix_notaire = prix_mutation + Etat + formalite_frais_divers

    if prix_bien < 6501:
        prix_notaire += 3.870/100 * prix_bien
    elif prix_bien > 6501 and prix_bien < 17001:
        prix_notaire += 3.870/100 * 6501 + 1.596/100 * (17000 - prix_bien)
    elif prix_bien > 17000 and prix_bien < 60000:
        prix_notaire += 3.870/100 * 6501 + 1.596/100 * (17000 - 6500) + 1.064/100 * (60000 - prix_bien)
    else:
        if remise_emoluments:
            print("INFO : Les frais d'émolument sont réduits")
            if prix_bien > 60000 and prix_bien < 100000:
                prix_notaire += 3.870/100 * 6501 + 1.596/100 * (17000 - 6500) + 1.064/100 * (60000 - 17000) + 0.799/100 * (100000 - prix_bien)
            else:
                prix_notaire += 3.870/100 * 6501 + 1.596/100 * (17000 - 6500) + 1.064/100 * (60000 - 17000) + 0.799/100 * ((100000 - 60000) + 0.80* (prix_bien - 100000))
        else:
            prix_notaire += 3.870/100 * 6501 + 1.596/100 * (17000 - 6500) + 1.064/100 * (60000 - 17000) + 0.799/100 * (prix_bien - 60000)
            print("INFO : Les frais d'émolument ne sont pas réduits")
    print("Prix du bien = ", prix_bien)
    print("Prix notaire = ", prix_notaire)
    print("Pourcentage notaire = ", prix_notaire / prix_bien *100, "%")


### Prix pret

def calcul_du_pret(pret:int = 222859, pret_taux_reduit = 15000, taux_reduit:int = 0.5 / 100, nombre_annees_pret:int = 25, taux_annuel:float = 1.08/100, afficher:bool = False):
    prets = [pret, pret_taux_reduit]
    taux = [taux_annuel, taux_reduit]
    mensualites = []
    prix_totaux = []
    interets = []
    nombre_mois = nombre_annees_pret * 12
    # calcul autour du pret a taux reduit
    taux_mensuel = (1+taux_reduit)**(1/12)-1
    mensualite = (pret_taux_reduit * taux_mensuel * (1 + taux_mensuel)**nombre_mois)/((1 + taux_mensuel)**nombre_mois - 1)
    prix_total = mensualite * nombre_mois
    interet = prix_total - pret_taux_reduit
    mensualites.append(mensualite)
    prix_totaux.append(prix_total)
    interets.append(interet)
    # calcul autour du pret restant
    taux_mensuel = (1+taux_annuel)**(1/12)-1
    mensualite = ((pret - pret_taux_reduit) * taux_mensuel * (1 + taux_mensuel)**nombre_mois)/((1 + taux_mensuel)**nombre_mois - 1)
    prix_total = mensualite * nombre_mois
    interet = prix_total - (pret - pret_taux_reduit)
    mensualites.append(mensualite)
    prix_totaux.append(prix_total)
    interets.append(interet)
    # renvoi des resultats
    if afficher:
        print('Mensualites: ', mensualites)
        print('Prix totaux: ', prix_totaux)
        print('Interets: ', interets)
    return mensualites, prix_totaux, interets


plage_taux = np.linspace(0.5, 2, 501)
plage_interets_reduits = np.array([])
plage_interets_restants = np.array([])
for taux in plage_taux:
    res = calcul_du_pret(taux_annuel = taux)
    plage_interets_reduits = np.append(plage_interets_reduits, res[2][0])
    plage_interets_restants = np.append(plage_interets_restants, res[2][1])

def afficher_taux():
    plt.plot(plage_taux, plage_interets_restants)
    plt.xlabel('Taux annuel')
    plt.ylabel('Interêts restants engendrés')
    # plt.plot([taux_annuel_CIC, taux_annuel_CIC],[])
    # plt.annotate('local max', xy=(taux_annuel_CIC, interet[index(plage_interets_reduits, taux_annuel_CIC, xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()

