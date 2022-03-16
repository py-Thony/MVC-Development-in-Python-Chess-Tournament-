from models.player import Player

def Add():
        
    print("\nAjouter un nouveau joueur\n")
        
    firstName = input("Prénom : ")
    lastName = input("Nom : ")
    
    return (firstName, lastName)
