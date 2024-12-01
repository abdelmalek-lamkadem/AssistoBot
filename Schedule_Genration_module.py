from ortools.sat.python import cp_model
import pandas as pd
import collections
import random
from ortools.sat.python import swig_helper
# Données
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
heures = ["8h-10h", "10h-12h", "12h-14h", "14h-16h", "16h-18h"]

# Professeurs
professeurs = {
    1: {"nom": "Mme HAYAT", "disponibilités": ["Lundi", "Mardi"]},
    2: {"nom": "M. MOHAMED", "disponibilités": ["Mercredi", "Jeudi", "Samedi"]},
    3: {"nom": "M. ZAKARIA", "disponibilités": ["Jeudi", "Vendredi", "Samedi"]},
    4: {"nom": "M. BOUCHICH", "disponibilités": ["Vendredi", "Samedi"]},
    5: {"nom": "M. BOUTOUBA", "disponibilités": ["Mardi", "Jeudi", "Vendredi", "Samedi"]},
    6: {"nom": "M. Naser", "disponibilités": ["Mercredi", "Jeudi", "Vendredi", "Samedi"]},
    7: {"nom": "Mme HAYAT", "disponibilités": ["Mardi", "Jeudi", "Vendredi", "Samedi"]},
}

# Classes
classes = {
    1: {"nom": "IA A"},
    2: {"nom": "IA B"},
    3: {"nom": "ROC A"},
    4: {"nom": "ROC B"},
    5: {"nom": "GINF A"},
    6: {"nom": "GINF B"},
    7: {"nom": "IRSI A"},
    8: {"nom": "IRSI B"},
}

# Matières avec durées (en heures par semaine)
matieres = {
    1: {"nom": "DEV_MOBILE", "professeur_id": 4, "cours": 2, "tp_td": 2},
    2: {"nom": "DEV_WEB", "professeur_id": 3, "cours": 2, "tp_td": 2},
    3: {"nom": "FRANCAIS", "professeur_id": 1, "cours": 2, "tp_td": 0},
    4: {"nom": "ANGLAIS", "professeur_id": 6, "cours": 2, "tp_td": 0},
    5: {"nom": "COUR_SP", "professeur_id": 5, "cours": 2, "tp_td": 2},
    6: {"nom": "GESTION", "professeur_id": 2, "cours": 2, "tp_td": 2},
    7: {"nom": "CURATION", "professeur_id": 7, "cours": 2, "tp_td": 0},
}

# Fonction pour vérifier la disponibilité d'un professeur
def est_prof_disponible(professeur_id, jour):
    return jour in professeurs[professeur_id]["disponibilités"]

# Fonction pour générer l'emploi du temps avec OR-Tools
def generer_emploi_du_temps(classes, jours, heures, matieres):
    # Initialiser le modèle
    model = cp_model.CpModel()

    # Variables
    emploi_du_temps = {}
    for classe_id in classes:
        for matiere_id, matiere in matieres.items():
            for jour in range(len(jours)):
                for heure in range(len(heures)):
                    emploi_du_temps[(classe_id, matiere_id, jour, heure)] = model.NewBoolVar(
                        f"classe_{classe_id}_matiere_{matiere_id}_jour_{jour}_heure_{heure}"
                    )

    # Contraintes
    for classe_id in classes:
        for matiere_id, matiere in matieres.items():
            # Chaque matière doit avoir exactement les heures prévues (cours et TP/TD)
            model.Add(
                sum(
                    emploi_du_temps[(classe_id, matiere_id, jour, heure)]
                    for jour in range(len(jours))
                    for heure in range(len(heures))
                )
                == matiere["cours"] + matiere["tp_td"]
            )

    # Une classe ne peut pas avoir plusieurs matières au même moment
    for jour in range(len(jours)):
        for heure in range(len(heures)):
            for classe_id in classes:
                model.Add(
                    sum(
                        emploi_du_temps[(classe_id, matiere_id, jour, heure)]
                        for matiere_id in matieres
                    )
                    <= 1
                )

    # Disponibilité des professeurs
    for matiere_id, matiere in matieres.items():
        professeur_id = matiere["professeur_id"]
        for jour in range(len(jours)):
            if not est_prof_disponible(professeur_id, jours[jour]):
                for heure in range(len(heures)):
                    for classe_id in classes:
                        model.Add(emploi_du_temps[(classe_id, matiere_id, jour, heure)] == 0)

    # Résolution
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        emplois = collections.defaultdict(lambda: collections.defaultdict(list))
        for classe_id in classes:
            for matiere_id, matiere in matieres.items():
                for jour in range(len(jours)):
                    for heure in range(len(heures)):
                        if solver.Value(emploi_du_temps[(classe_id, matiere_id, jour, heure)]):
                            emplois[classes[classe_id]["nom"]][jours[jour]].append(
                                f"{heures[heure]}: {matiere['nom']}"
                            )
        return emplois
    else:
        print("Aucune solution trouvée.")
        return None

# Générer l'emploi du temps
emploi = generer_emploi_du_temps(classes, jours, heures, matieres)

# Affichage
if emploi:
    for classe, planning in emploi.items():
        print(f"\nEmploi du temps pour la classe {classe}:")
        for jour, activites in planning.items():
            print(f"  {jour}: {', '.join(activites)}")
