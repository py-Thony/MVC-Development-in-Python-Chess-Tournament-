class Player():

    Players = []

    def __init__(self, firstName, lastName) -> None:
        self.id = len(Player.Players) + 1
        self.firstName = firstName
        self.lastName = lastName
        
        Player.Players.append(self)
        
        
    def __str__(self):
        return f"({self.id}) {self.firstName} {self.lastName}"