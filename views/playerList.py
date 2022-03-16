from models.player import Player

def ShowAllPlayers():
        
    print("\nListe de tous les joueurs\n")
        
    for myPlayer in Player.Players:
        print(myPlayer)
