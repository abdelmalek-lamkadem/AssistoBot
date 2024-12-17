import pandas as pd
import random

# Fonction pour saisir les données de l'utilisateur
def saisir_professeurs():
    professeurs = {}
    n = int(input("Combien de professeurs voulez-vous saisir ? "))
    for i in range(1, n + 1):
        nom = input(f"Nom du professeur {i} : ")
        disponibilites = input(f"Disponibilités pour {nom} (séparées par des virgules) : ").split(",")
        disponibilites = [d.strip() for d in disponibilites]
        professeurs[i] = {"nom": nom, "disponibilités": disponibilites}
    return professeurs

def saisir_classes():
    classes = {}
    n = int(input("Combien de classes voulez-vous saisir ? "))
    for i in range(1, n + 1):
        nom = input(f"Nom de la classe {i} : ")
        classes[i] = {"nom": nom}
    return classes

def saisir_matieres(professeurs):
    matieres = {}
    n = int(input("Combien de matières voulez-vous saisir ? "))
    for i in range(1, n + 1):
        nom = input(f"Nom de la matière {i} : ")
        professeur_id = int(input(f"ID du professeur pour {nom} (1-{len(professeurs)}) : "))
        cours = int(input(f"Nombre d'heures de cours pour {nom} : "))
        tp_td = int(input(f"Nombre d'heures de TP/TD pour {nom} : "))
        matieres[i] = {
            "nom": nom,
            "professeur_id": professeur_id,
            "cours": cours,
            "tp_td": tp_td
        }
    return matieres

# Fonction pour générer un emploi du temps unique pour chaque classe
def generer_emploi_du_temps_unique(classes, jours, heures, matieres, professeurs):
    emplois_du_temps = {}

    for classe_id, classe in classes.items():
        emploi_classe = pd.DataFrame(index=jours, columns=heures)
        matieres_disponibles = list(matieres.values())
        random.shuffle(matieres_disponibles)

        for matiere in matieres_disponibles:
            professeur_nom = professeurs[matiere['professeur_id']]['nom']
            heures_disponibles = list(heures)
            random.shuffle(heures_disponibles)
            jours_disponibles = list(jours)

            # Ajouter les cours (2 heures) une fois par semaine
            for _ in range(1):  # Limite à une occurrence par semaine
                if not heures_disponibles or not jours_disponibles:
                    break
                heure = heures_disponibles.pop()
                jour = random.choice(jours_disponibles)

                while not pd.isna(emploi_classe.at[jour, heure]):
                    if not heures_disponibles:
                        break
                    heure = heures_disponibles.pop()

                if pd.isna(emploi_classe.at[jour, heure]):
                    emploi_classe.at[jour, heure] = f"{matiere['nom']} ({professeur_nom}, Cours)"
                    jours_disponibles.remove(jour)

            # Ajouter TP/TD (2 heures) si nécessaire, une fois par semaine
            if matiere["tp_td"] > 0:
                for _ in range(1):  # Limite à une occurrence par semaine
                    if not heures_disponibles or not jours_disponibles:
                        break
                    heure = heures_disponibles.pop()
                    jour = random.choice(jours_disponibles)

                    while not pd.isna(emploi_classe.at[jour, heure]):
                        if not heures_disponibles:
                            break
                        heure = heures_disponibles.pop()

                    if pd.isna(emploi_classe.at[jour, heure]):
                        emploi_classe.at[jour, heure] = f"{matiere['nom']} ({professeur_nom}, TP/TD)"
                        jours_disponibles.remove(jour)

        emplois_du_temps[classe["nom"]] = emploi_classe

    return emplois_du_temps

# Fonction pour enregistrer et afficher les emplois du temps dans un fichier CSV
def sauvegarder_emplois_csv(emplois):
    for classe, planning in emplois.items():
        fichier_csv = f"emploi_du_temps_{classe}.csv"
        planning.to_csv(fichier_csv, index=True)
        print(f"Emploi du temps pour la classe {classe} enregistré dans {fichier_csv}.")

# Main
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
heures = ["8:30h-10:00h", "10:15h-12:15h", "14:30h-16:00h", "16:15h-18:15h"]

print("Saisir les données pour les professeurs, classes et matières :")
professeurs = saisir_professeurs()
classes = saisir_classes()
matieres = saisir_matieres(professeurs)

emplois = generer_emploi_du_temps_unique(classes, jours, heures, matieres, professeurs)

if emplois:
    for classe, planning in emplois.items():
        print(f"\nEmploi du temps pour la classe {classe}:")
        print(planning.to_string(index=True))
    sauvegarder_emplois_csv(emplois)
LUNDI,MARDI,MERCREDI,JEUDI,VENDREDI,SAMEDI
