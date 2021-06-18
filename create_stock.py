
from models.stock import Stock


def create_stock():
    stock = Stock()
    stock.add("cake", 4.55, 0)
    stock.add("sweet", 14.55, 10)
    stock.add("Carrot cake", 7.55, 50, True)
    stock.add("Choco cream cake", 17.55, 50, True)
    stock.add("Choco cream cake", 17.55, 50, True)
    stock.add("Cigarettes", 1.55, 50, True)
    stock.add("Foster bottle", 4.55, 50, True)
    stock.add("IPA", 4.55, 50, True)
    stock.add("Carrot cake", 4.55, 10, True)
    stock.add("Custard cream", 2.55, 60, True)
    stock.add("Muffin", 6.55, 40)
    stock.add("Mars", 0.55, 10)
    stock.add("Twix", 6.55, 250, True)
    stock.add("Magnum", 6.55, 70, True)
    stock.add("Kit kat", 6.55, 90)
    stock.add("Kit kat", 6.55, 90)
    stock.add("Soda water", 6.55, 150)
    stock.add("Soda water with ginger beer", 6.55, 9, True)
    stock.add("Ginger beer", 6.55, 4, True)
    stock.add("Coke", 6.55, 24)
    stock.add("Fanta", 6.55, 15)
    stock.add("Diet Coke", 6.55, 5)
    stock.add("Gin and tonic", 6.55, 5, True)
    stock.add("Foster", 6.55, 50, True)
    return stock

