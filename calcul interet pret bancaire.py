import numpy as np
import matplotlib.pyplot as plt

prix_bien = 236000

### Prix Notaire

remise_emoluments = False

def calcul_frais_de_notaire(prix_bien : int = 100000, remise_emoluments : bool = False):
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

def calcul_du_pret(prix_bien:int = 230000, pret:int = 207859, nombre_annees_pret:int = 25, taux:float = 1.08/100, afficher:bool = False):
    nombre_mois = nombre_annees_pret*12
    pret_taux_mensuel = pret * taux / 12
    numero_de_mois = np.arange(1, nombre_mois + 1, 1)
    mensualite = np.array([0])
    capital_restant = np.array([pret])
    print('loading...')
    for mois in range(1,nombre_mois):
        nouvelle_annualite = (capital_restant[-1] - mensualite[-1])*taux
        # print('Numero: ', mois+1)
        # print('Derniere mensualite: ', mensualite[-1])
        # print('Nouvelle mensualite: ', (capital_restant[-1] - mensualite[-1])*taux)
        mensualite = np.append(mensualite, nouvelle_annualite/12)
        capital_restant = np.append(capital_restant, capital_restant[-1] - (nouvelle_annualite*11/12))
    print('done')

    print('Interets: ', sum(mensualite))
        
    if afficher:
        fig, axs = plt.subplots(2, sharex=True)
        fig.suptitle('Détails du prêt qu cours des mois')
        axs[0].plot(numero_de_mois, mensualite)
        axs[0].set_title('Mensualité')
        axs[1].plot(numero_de_mois, capital_restant)
        axs[1].set_title('Ce qu\'il reste à payer')
        plt.show()
