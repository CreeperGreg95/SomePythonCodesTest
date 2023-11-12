import tkinter as tk
from tkinter import filedialog

def get_executable_name():
    file_path = filedialog.askopenfilename(
        title="Sélectionnez un fichier exécutable",
        filetypes=(("Fichiers MSI", "*.msi"), ("Fichiers ClickOnce", "*.application"), ("Tous les fichiers", "*.*"))
    )
    
    if file_path:
        # Utilisez un autre module pour obtenir le nom de l'exécutable
        import os
        executable_name = os.path.basename(file_path)
        result_label.config(text="Nom de l'exécutable : " + executable_name)
    else:
        result_label.config(text="Aucun fichier sélectionné")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Sélection d'exécutable")

# Bouton pour ouvrir la boîte de dialogue de sélection de fichier
select_button = tk.Button(window, text="Sélectionner un fichier exécutable", command=get_executable_name)
select_button.pack(padx=10, pady=10)

# Étiquette pour afficher le nom de l'exécutable
result_label = tk.Label(window, text="")
result_label.pack(padx=10, pady=10)

# Lancement de la boucle principale
window.mainloop()
