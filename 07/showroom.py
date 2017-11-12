class Node:
    def __init__(self, car=None, prevNode=None, nextNode=None):
        self.prevNode = prevNode
        self.nextNode = nextNode
        self.data = car


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


def clean():
    db.head = None


def init(cars):
    clean()
    for car in cars:
        add(car)


def add(car):
    if getDatabaseHead() is None:
        db.head = Node(car)

    else:
        prevItem = None
        item = db.head
        while True:
            if item is None:
                item = Node(car, prevItem)
                prevItem.nextNode = item
                break

            elif item.data.price > car.price:
                newItem = Node(car, prevItem, item)
                item.prevNode = newItem
                if prevItem is not None:
                    prevItem.nextNode = newItem
                else:
                    db.head = newItem
                break

            else:
                prevItem = item
                item = item.nextNode


def updateName(identification, name):
    item = db.head
    while True:
        if item is None:
            return None
        elif item.data.identification == identification:
            item.data.name = name
            return
        else:
            item = item.nextNode


def updateBrand(identification, brand):
    item = db.head
    while True:
        if item is None:
            return None
        elif item.data.identification == identification:
            item.data.brand = brand
            return
        else:
            item = item.nextNode


def activateCar(identification):
    item = db.head
    while True:
        if item is None:
            return None
        elif item.data.identification == identification:
            item.data.active = True
            return
        else:
            item = item.nextNode


def deactivateCar(identification):
    item = db.head
    while True:
        if item is None:
            return None
        elif item.data.identification == identification:
            item.data.active = False
            return
        else:
            item = item.nextNode


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    sumPrice = 0
    item = db.head

    while item is not None:
        if item.data.active:
            sumPrice += item.data.price

        item = item.nextNode

    return sumPrice


def printDatabase():
    element = db.head

    if element is None:
        return

    i = 0

    while True:
        i += 1
        print('\nPrinting ' + str(i) + '. car:')

        if element.data is not None:
            print('\tidentification = ' + str(element.data.identification))
            print('\tname = ' + str(element.data.name))
            print('\tbrand = ' + str(element.data.brand))
            print('\tprice = ' + str(element.data.price))
            print('\tactive = ' + str(element.data.active))

        else:
            print('\t' + str(i) + '. car is None')

        if element.nextNode is None:
            break
        else:
            element = element.nextNode


def initDatabase():
    # audi = Car(1, 'R8', 'Audi', 200, True)
    # volkswagen = Car(3, 'Passat', 'Volkswagen', 300, True)
    # ford = Car(2, 'Mustang', 'Ford', 250, True)
    # init([audi, volkswagen, ford])
    first = Car(1, 'Octavia', 'Skoda', 123000, True)
    second = Car(23, 'Felicia', 'Skoda', 5000, True)
    third = Car(11, 'Superb', 'Skoda', 54000, True)
    init([first, second, third])


initDatabase()
printDatabase()
print('\nsum = ' + str(calculateCarPrice()))
