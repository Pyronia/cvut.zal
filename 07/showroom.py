class Node:
    def __init__(self, car=None, prevNode=None, nextNode=None):
        self.prevNode = prevNode
        self.nextNode = nextNode
        self.car = car


class LinkedList:
    def __init__(self):
        self.head = None


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = int(identification)
        self.name = str(name)
        self.brand = str(brand)
        self.price = int(price)
        self.active = bool(active)


db = LinkedList()


def init(cars):
    clean()
    for car in cars:
        add(car)


def add(car):
    if getDatabaseHead() is None:
        db.head = Node(car)

    else:
        prevItem = db.head
        item = db.head.nextNode
        while True:
            if item is None:
                item = Node(car, prevItem)
                prevItem.nextNode = item
                break

            elif item.car.price > car.price:
                newItem = Node(car, prevItem, item)
                item.prevNode = newItem
                prevItem.nextNode = newItem
                break

            else:
                prevItem = item
                item = item.nextNode


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
    sumPrice = 0
    item = db.head

    while item is not None:
        if item.car.active:
            sumPrice += item.car.price

        item = item.nextNode

    return sumPrice


def clean():
    pass


def printDatabase():
    element = db.head

    if element is None:
        return

    i = 0

    while True:
        i += 1
        print('\nPrinting ' + str(i) + '. car:')

        if element.car is not None:
            print('\tidentification = ' + str(element.car.identification))
            print('\tname = ' + str(element.car.name))
            print('\tbrand = ' + str(element.car.brand))
            print('\tprice = ' + str(element.car.price))
            print('\tactive = ' + str(element.car.active))

        else:
            print('\t' + str(i) + '. car is None')

        if element.nextNode is None:
            break
        else:
            element = element.nextNode


def initDatabase():
    audi = Car(1, 'R8', 'Audi', 200, True)
    volkswagen = Car(3, 'Passat', 'Volkswagen', 300, True)
    ford = Car(2, 'Mustang', 'Ford', 250, True)
    init([audi, volkswagen, ford])


initDatabase()
printDatabase()
print('\nsum = ' + str(calculateCarPrice()))
