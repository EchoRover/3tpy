


class TTT:
    def __init__(self):
        self.BLANK = " "
        self.X = "X"
        self.O = "O"
        self.board = [[self.BLANK for _ in range(3)] for __ in range(3)]

        self.game()
    
    def game(self,start = 0):
        self.move = start
        while not self.gameover():
            self.display()
            self.char = self.X if self.move % 2 == 0 else self.O

            if self.move % 2 == 0:
                # player
                x,y = self.getplayermove()
                self.game = self.move(x,y,self.char)
            else:
                x,y, = self.getcomputermove()
                self.game = self.move(x,y,self.char)

            

        
    

    def display(self):
        print("---------")
        for row in self.board:
            print(" |".join(row))
            print("---------")
    
    def copy(self):
        cp = [row.copy() for row in self.board]
        return cp
    
    def move(self,x,y,char):
        cp = self.copy()
        cp[y][x] = char
        return cp
    def gameover(self):
        new = self.board[0] + self.board[1] + self.board[2]
        if any(new):
            ...

    
    def getplayermove(self):
        ans = input("move (x,y):")
        print(ans)
    
    

        
    


if __name__ == "__main__":
    a = TTT()
    a.display()