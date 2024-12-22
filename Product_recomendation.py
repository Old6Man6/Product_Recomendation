import json

class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating


def read_json(filename):
    products = []
    try:
        with open(filename) as file:
            for p in json.load(file):
                products.append(Product(p['name'], p['price'], p['rating']))
            return products
    except:
        pass



def binary_search(data, target):
    try:
        data.sort(key=lambda x: x.price)
        for product in data:
            print(product.price)
    except:
        pass







if __name__ == '__main__':
    target = input("Enter a Price: ")
    data = read_json('products.json')
    binary_search(data=data, target=target)