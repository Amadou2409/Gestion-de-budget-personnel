import tkinter as tk
# Importe tkinter pour pouvoir créer une interface graphique.
# "tk" est un raccourci pour écrire tkinter.


# -----------------------------------------
# FONCTION DU BOUTON COMMENCER
# -----------------------------------------

def commencer():
    # Cette fonction se déclenche quand on clique sur "Commencer !"

    for widget in fenetre.winfo_children():
        # Récupère tous les éléments présents dans la fenêtre.
        widget.destroy()
        # Supprime chaque élément de la fenêtre.

    # Affiche le nouveau texte après avoir cliqué.
    titre = tk.Label(
        fenetre,
        text="Pour commencer, entrez votre revenu total",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="black",
        wraplength=600
    )
    titre.pack(pady=80)

    # Crée une case pour que l'utilisateur puisse entrer son revenu.
    revenu = tk.Entry(
        fenetre,
        font=("Arial", 16),
        width=20
    )
    revenu.pack(pady=20)


# -----------------------------------------
# CRÉATION DE LA FENÊTRE PRINCIPALE
# -----------------------------------------

fenetre = tk.Tk()
# Crée la fenêtre.

fenetre.title("My Budget")
# Donne un titre à la fenêtre.

fenetre.geometry("700x500")
# Définit la taille de la fenêtre (largeur x hauteur).

fenetre.configure(bg="lightblue")
# Définit la couleur de fond.


# -----------------------------------------
# TEXTE DE PRÉSENTATION
# -----------------------------------------

titre = tk.Label(
    fenetre,
    # Indique dans quelle fenêtre afficher le texte.

    text="Bonjour et bienvenue dans My Budget, le logiciel de gestion de budget personnel préféré des adultes. En entrant vos revenus, dépenses, etc ce logiciel vous permettra d'avoir une vision claire sur la gestion de votre argent, et vous aidera à definir des objectifs d'épargne.",
    # Définit le texte qui sera affiché.

    font=("Arial", 15),
    # Définit la police et la taille.

    bg="lightblue",
    # Couleur de fond.

    fg="black",
    # Couleur du texte.

    wraplength=600,
    # Permet au texte de revenir à la ligne.

    justify="center"
    # Centre le texte.
)

titre.pack(pady=50, padx=30)
# Affiche le texte dans la fenêtre.
# pady = espace vertical.
# padx = espace horizontal.


# -----------------------------------------
# BOUTON COMMENCER
# -----------------------------------------

bouton = tk.Button(
    fenetre,
    text="Commencer !",
    # Texte écrit sur le bouton.

    font=("Arial", 18),
    # Taille du texte.

    bg="green",
    # Couleur du bouton.

    fg="white",
    # Couleur de l'écriture.

    command=commencer
    # Lance la fonction commencer() quand on clique.
)

bouton.pack(pady=20)
# Affiche le bouton dans la fenêtre.


# -----------------------------------------
# LANCEMENT DU PROGRAMME
# -----------------------------------------

fenetre.mainloop()
# Permet à la fenêtre de rester ouverte et interactive.