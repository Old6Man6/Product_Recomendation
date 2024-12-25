import json

class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating


    """ We can add a function to change value formats if we need acctualy in price """
    # def Fix_Price(self, price):
    #     try:
    #       pass
    #         return float(price)
    #     except Exception as e:
    #         return print(f"Error in FixingPrice: {e}")
def read_json(filename):
    products = []
    try:
        with open(filename) as file:
            for p in json.load(file):
                products.append(Product(p['name'], p['price'], p['rating']))
            return products
    except FileNotFoundError as e:
        print(f"Error in reading file: {e}")
        return []



def binary_search(data, target, op):
    try:
        ans = []
        data.sort(key=lambda x: x.price)
        st = 0
        en = len(data) - 1
        while st <= en:
            mid = (en + st) // 2
            if op == "yes":

                if data[mid].price == target:
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
    except Exception as e:
        print(f"Error in binary search: {e}")







if __name__ == '__main__':
    op_low = str(input("OP_LOW (it's sample it must change) type yes: "))
    target = float(input('Enter a number: '))
    data = read_json('products.json')
    binary_search(data=data, target=target, op=op_low)