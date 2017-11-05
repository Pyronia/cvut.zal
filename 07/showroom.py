class Node:
    def __init__(self, nextNode, prevNode, car):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.car = car


class LinkedList:
    def __init__(self):
        pass


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars):
    pass


def add(car):
    pass


def updateName(identification, name):
    pass


def updateBrand(identification, brand):
    pass


def activateCar(identification):
    pass


def deactivateCar(identification):
    pass


def getDatabaseHead():
    pass


def getDatabase():
    pass


def calculateCarPrice():
    pass


def clean():
    pass
