class Node:
    def __init__(self, prevNode=None, nextNode=None, car=None):
        self.prevNode = prevNode
        self.nextNode = nextNode
        self.car = car


class LinkedList:
    def __init__(self):
        self.head = None


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars):
    clean()
    for car in cars:
        add(car)


# def isCarValid(car):
#     if car.identification is None or car.name is None or car.brand is None or car.price is None or car.active is None:
#         return False
#     else:
#         return True


def add(car):
    item = getDatabaseHead()
    previousItem = None

    if item is None:
        item = Node()
        item.car = car
        if previousItem is not None:
            item.prevNode = previousItem


def updateName(identification, name):
    pass


def updateBrand(identification, brand):
    pass


def activateCar(identification):
    pass


def deactivateCar(identification):
    pass


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    pass


def clean():
    pass
