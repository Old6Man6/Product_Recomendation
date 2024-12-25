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



def binary_search(data, target, op):
    target = float(target)
    try:
        ans = []
        data.sort(key=lambda x: x.price)
        st = 0
        en = len(data) - 1
        while st <= en:
            mid = (en + st) // 2
            if op == "yes":

                if data[mid].price >= target:
                    ans2 = []
                    for i in range(0, mid):
                        ans2.append({
                            "name": data[i].name,
                            "rating": data[i].rating,
                            "price": data[i].price
                        })

                    return print(ans2)
            if data[mid].price == target:
                ans.append({
                    "name": data[mid].name,
                    "rating": data[mid].rating,
                    "price": data[mid].price
                })
                return print(ans)
            elif data[mid].price < target:
                st = mid + 1
            else:
                en = mid - 1
        return None
    except:
        pass







if __name__ == '__main__':
    op_low = str(input("OP_LOW (it's sample it must change) type yes: "))
    target = int(input('Enter a number: '))
    data = read_json('products.json')
    binary_search(data=data, target=target, op=op_low)