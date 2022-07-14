import random
class ValueError(Exception):
    pass

class Position:
    def __init__(self,x,y,speed,dx = 0,dy = 0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        if speed >= 0:
            self.speed = speed
        else:    
            raise ValueError
            
    def moveTo(self,x_co,y_co):
        self.dx = x_co
        self.dy = y_co
        
    def tick(self):
        if self.speed < abs(self.x - self.dx):
            self.x += self.speed
        else:
            self.x = self.dx
        if self.speed < abs(self.y - self.dy):
            self.y += self.speed
        else:
            self.y = self.dy
        
    def distance(self,other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

class VirusesInsufficient(Exception):
    pass

class OutOfRange(Exception):
    pass

class Cell(Position):
    def __init__(self,X,Y,colour,attackRange,mood = 'Happy',defense = 10,maxDefense = 10):
        self.colour = colour
        if self.colour == 'None':
            self.viruses = 0
        else:
            self.viruses = 5
        self.attackRange = attackRange
        self.mood = mood
        if mood == 'Happy':
            speed = 0.1
        elif mood == 'Angry':
            speed = 0.2
        elif mood == 'Stoic':
            speed = 0.05
        elif mood == 'Busy':
            speed = 0
        self.defense = defense
        self.maxDefense = maxDefense
        super().__init__(X,Y,speed)
        
    def tick(self):
        super().tick()
        if self.mood == 'Happy':
            self.viruses += 3
        elif mood == 'Busy':
            self.viruses += 8
        elif mood == 'Angry':
            self.viruses += 6
        elif mood == 'Stoic':
            self.viruses += 6
        if self.defense != self.maxDefense:
            self.defense += 1
            
    def changeMood(self,newMood):
        if self.viruses < 20:
            raise VirusesInsufficient
        if newMood in ["Busy", "Stoic", "Angry"]:
            self.viruses -= 20
            self.mood = newMood
            if self.mood == 'Stoic':
                self.maxDefense = 30
            elif self.mood == 'Angry' or self.mood == 'Busy':
                self.maxDefense = 5
        else:
            raise ValueError
        self.speed = speed
        if mood == 'Happy':
            speed = 0.1
        elif mood == 'Angry':
            speed = 0.2
        elif mood == 'Stoic':
            speed = 0.05
        elif mood == 'Busy':
            speed = 0
            
    def attack(self,other):
        d = ((self.X - other.X)**2 + (self.Y - other.Y)**2)**0.5
        if d < attackRange:
            pass
        else:
            raise OutOfRange
        base = self.viruses
        actual = self.viruses-other.defense
        if actual <= 0:
            P.defense -= base
        else:
            P.defense = 0
        if actual < P.viruses:
            P.viruses -= actual
        elif actual > P.viruses:
            P.colour = self.colour
            P.viruses = actual-P.viruses
        else:
            P.colour = 'None'
            self.colour = 'None'
        self.viruses = 0
        
    def __eq__(self,c):
        if self.x == c.x and self.y == c.y and self.viruses == c.viruses and self.mood==c.mood and self.defens == c.defense:
            return True
        else:
            return False


class VirusGame:
    def __init__(self,n):
        self.cells = []
        for i in range(n):
            x = random.uniform(-10,10)
            y = random.uniform(-10,10)
            if i != 0:
                self.cells.append(Cell(x,y,'Blue',3.0))
            else:
                self.cells.append(Cell(x,y,'Red',3.0))
                
    def checkVictory(self):
        colour = ''
        for i in range(len(self.cells)):
            if i != 0:
                if colour!=self.cells[i].colour:
                    return 'None yet...'
            else:
                colour = self.cells[i].colour
        return colour
    
    def action(self,position1,position2):
        c1 = -1
        c2 = -1
        for i in range(len(self.cells)):
            cell = self.cells[i]
            d1 = ((cell.x - position1.x)**2 + (cell.y - position1.y)**2)**0.5
            if d1 <= 1:
                c1 = i
                break
        if c1 == -1:
            return
        for i in range(len(self.cells)):
            cell = self.cells[i]
            d2 = ((cell.x - position2.x)**2 + (cell.y - position2.y)**2)**0.5
            if d2 <= 1:
                c2 = i
                break
        if c2 != -1:
            self.cells[c2].mood = 'Busy'
            self.cells[c1].attack(self.cell[c2])
        else:
            self.cells[c1].moveTo(position2.x,position2.y)
    
    def tick(self):
        for cell in self.cells:
            cell.tick()                
        
        
        
        
        
        
        