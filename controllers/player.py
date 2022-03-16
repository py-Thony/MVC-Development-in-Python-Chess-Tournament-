from models.player import Player

import views.playerList as PlayerList
import views.addPlayer as AddPlayer


def MainPlayer():

    print("\nMenu")
    print("1 - Afficher les joueurs")
    print("2 - Ajouter un joueur")
    Choice = input("Choix : ")
    
    if Choice == "1":
        PlayerList.ShowAllPlayers()
    elif Choice == "2":
        playerData = AddPlayer.Add()
        Player(playerData[0], playerData[1])
    else:
        Go = False
            