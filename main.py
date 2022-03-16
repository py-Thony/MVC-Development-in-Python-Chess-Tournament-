# -*-coding: utf-8 -*-

from models.player import Player

import controllers.player as PlayerController

import views.playerList as PlayerList


def main():
    newPlayer = PlayerList
    
    print()
    
    Go = True
    while Go:
        
        PlayerController.MainPlayer()
            
    print("\nAu revoir")
      


if __name__ == "__main__":
    main()