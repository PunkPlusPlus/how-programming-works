class Animal:
    weight: float
    color: str
    pol: str

    def __init__(self, weight, color, pol):
        self.color = color
        self.weight = weight
        self.pol = pol

    def __str__(self):
        return f'Weight: {self.weight}, Color: {self.color}, Pol: {self.pol}'

    def __int__(self):
        return int(self.weight)

    def feed(self, eat):
        pass




class Bear(Animal):

    def feed(self, eat: int):
        if self.weight >= 100:
            if eat >= 10 and eat <= 15:
                print('OK')
                return
            print('NOT OK')
            return
        if self.weight < 100:
            if eat <10:
                print("OK")
                return
            print('NOT OK')
        

    
class Penguin(Animal):

    def feed(self, eat: int):
        if eat != 'fish':
            return False
        return True


# Weight: 80, Color: brown, Pol: male
garphield = Bear(80, 'brown', 'male')


print(int(garphield))

