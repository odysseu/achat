#Prets et Apports
prixAppartement = 250630
tauxBourseAnnuel = 1/100
apport = 100000
pretBancaire = 200000
taux20ans = 1 + 1.10/100
taux25ans = 1 + 1.2/100
salaireMensuel = 2396

#Travaux
prixSol = 3000
prixFenetres = 3*2500
prixCuisine = 5000
prixCanape = 1000
prixLampes = 500
prixEtageres = 500
prixTables = 300
prixMeubles = prixCanape + prixLampes + prixEtageres + prixTables
prixTravaux = prixMeubles + prixSol + prixFenetres + prixCuisine

#Graph
pretMensuelMax = salaireMensuel / 3
pretMax20ans = pretMensuelMax * 12 * 20 / taux20ans
pretMax25ans = pretMensuelMax * 12 * 25 / taux25ans
pieChart = c(prixMeubles, prixSol, prixFenetres, prixCuisine)
pie(pieChart, labels = c('prixMeubles', 'prixSol', 'prixFenetres', 'prixCuisine'), main = c("Répartition des prix en plus de l'achat",as.character(prixTravaux),"EUR"))

