import requests

API_BASE = "https://fortnite-api.com/v2"
API_KEY = "366fa857-3cef-4657-b011-4293a8adf656"  # Remplacez par votre clé d'API depuis le site Fortnite-API

def get_player_stats(player_name):
    url = f"{API_BASE}/stats/br/v2?name={player_name}"
    headers = {"Authorization": API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

def get_cosmetic_info(cosmetic_name):
    url = f"{API_BASE}/cosmetics/br/search?name={cosmetic_name}"
    headers = {"Authorization": API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    choix = input("1. Stats joueur\n2. Infos cosmétique\nChoisissez une option : ")
    if choix == "1":
        joueur = input("Entrez le nom du joueur : ")
        stats = get_player_stats(joueur)
        print(stats)
    elif choix == "2":
        cosmetic = input("Entrez le nom du cosmétique : ")
        info = get_cosmetic_info(cosmetic)
        print(info)
    else:
        print("Choix invalide")
