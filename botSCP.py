import robloxapi
import requests
import time

#identification
username = "CreeperGreg95_2"
password = "gregory2007"

# Connexion
client = robloxapi.client(username, password)

# Identifiant du jeu (trouvé dans l'URL du jeu sur Roblox)
game_id = "2768379856"

# ID du serveur (peut être trouvé dans le lien du serveur)
server_id = "05865218780476668068799829632561"

while True:
    # Obtenir des informations sur le serveur
    server_info = client.get_game_instance(game_id, server_id)

    if server_info['status'] != "OK":
        print(f"Le serveur n'est pas disponible, code de statut : {server_info['status']}")
    else:
        print("Le serveur est en ligne.")
        # Obtenez l'ID du personnage du joueur (assurez-vous d'être dans le jeu)
        player_id = client.get_user_by_username(username)['id']
        
        # ID du personnage (peut être obtenu en explorant le jeu)
        character_id = "ID_DU_PERSONNAGE"

        # Déplacez le personnage vers l'avant (en ajustant les coordonnées)
        move_url = f"https://games.roblox.com/v1/games/{game_id}/servers/{server_id}/move-to"
        data = {
            "position": {"x": 10, "y": 0, "z": 10},  # Ajustez les coordonnées selon vos besoins
            "characterId": character_id,
        }
        response = client.request(move_url, "POST", json=data)
        print(f"Personnage déplacé vers l'avant, réponse : {response.status_code}")

    # Attendez quelques secondes avant de vérifier à nouveau
    time.sleep(60)
