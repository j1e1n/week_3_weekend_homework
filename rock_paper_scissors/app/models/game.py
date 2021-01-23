class Game:

    
    def get_winner(p1, p2):
        if p1.choice == p2.choice:
            return None

        if p1.choice == "rock":
            if p2.choice == "scissors":
                return p1
            else:
                return p2

        elif p1.choice == "paper":
            if p2.choice == "rock":
                return p1
            else:
                return p2

        elif p1.choice == "scissors":
            if p2.choice == "paper":
                return p1
            else:
                return p2



      
    


