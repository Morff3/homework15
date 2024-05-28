class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        numberOfFloors = floors
        print(f'В доме этажей стало: {numberOfFloors}')


home = House()
home.setNewNumberOfFloors(4)
home.setNewNumberOfFloors(7)
home.setNewNumberOfFloors(11)
home.setNewNumberOfFloors(55)
