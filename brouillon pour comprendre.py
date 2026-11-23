import tkinter as tk

# -----------------------------------------
# FONCTION POUR PASSER À L'ÉTAPE SUIVANTE
# -----------------------------------------

def continuer():
    # Récupère le revenu entré par l'utilisateur.
    montant = revenu.get()

    # Vérifie que l'utilisateur a bien entré un montant.
    if montant == "":
        erreur.config(text="Veuillez entrer votre revenu.")
        return

    # Supprime tous les éléments de la fenêtre.
    for widget in fenetre.winfo_children():
        widget.destroy()

    # Affiche le nouveau titre.
    titre = tk.Label(
        fenetre,
        text="Entrez vos dépenses mensuelles",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="black"
    )
    titre.pack(pady=30)

    # Liste des différentes catégories de dépenses.
    categories = [
        "Logement (loyer, charges...)",
        "Alimentation",
        "Transport",
        "Loisirs",
        "Santé",
        "Abonnements",
        "Shopping",
        "Autres dépenses"
    ]

    # Crée une case pour chaque catégorie.
    global depenses
    depenses = {}

    for categorie in categories:

        # Affiche le nom de la catégorie.
        label = tk.Label(
            fenetre,
            text=categorie,
            font=("Arial", 13),
            bg="lightblue"
        )
        label.pack(pady=5)

        # Crée une case pour entrer le montant.
        entree = tk.Entry(
            fenetre,
            font=("Arial", 13),
            width=20
        )
        entree.pack(pady=2)

        # Enregistre la case dans le dictionnaire.
        depenses[categorie] = entree


# -----------------------------------------
# FONCTION DU BOUTON COMMENCER
# -----------------------------------------

def commencer():

    for widget in fenetre.winfo_children():
        widget.destroy()

    titre = tk.Label(
        fenetre,
        text="Pour commencer, entrez votre revenu total mensuel",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="black",
        wraplength=600
    )
    titre.pack(pady=80)

    global revenu

    revenu = tk.Entry(
        fenetre,
        font=("Arial", 16),
        width=20
    )
    revenu.pack(pady=20)

    # Crée un message d'erreur.
    global erreur

    erreur = tk.Label(
        fenetre,
        text="",
        font=("Arial", 12),
        fg="red",
        bg="lightblue"
    )
    erreur.pack()

    # Crée le bouton Continuer.
    bouton_continuer = tk.Button(
        fenetre,
        text="Continuer",
        font=("Arial", 18),
        bg="green",
        fg="white",
        command=continuer
    )
    bouton_continuer.pack(pady=20)


# -----------------------------------------
# CRÉATION DE LA FENÊTRE PRINCIPALE
# -----------------------------------------

fenetre = tk.Tk()

fenetre.title("My Budget")
fenetre.geometry("700x650")
fenetre.configure(bg="lightblue")


# -----------------------------------------
# TEXTE DE PRÉSENTATION
# -----------------------------------------

titre = tk.Label(
    fenetre,
    text="Bonjour et bienvenue dans My Budget, le logiciel de gestion de budget personnel préféré des adultes. En entrant vos revenus, dépenses, etc. ce logiciel vous permettra d'avoir une vision claire sur la gestion de votre argent et vous aidera à définir des objectifs d'épargne.",
    font=("Arial", 15),
    bg="lightblue",
    fg="black",
    wraplength=600,
    justify="center"
)

titre.pack(pady=50, padx=30)


# -----------------------------------------
# BOUTON COMMENCER
# -----------------------------------------

bouton = tk.Button(
    fenetre,
    text="Commencer !",
    font=("Arial", 18),
    bg="green",
    fg="white",
    command=commencer
)

bouton.pack(pady=20)


# -----------------------------------------
# LANCEMENT DU PROGRAMME
# -----------------------------------------

fenetre.mainloop()
