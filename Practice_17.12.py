class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        print(val)

    def top(self):
        print(self.__stack[-1])

    def __repr__(self):
        return f'{self.__stack}'


class ShoppingCart:

    def __init__(self):
        self.__cart = {}
        self.__total = 0
        self.__cart_items = self.__cart.keys()

    def add_product(self, name: str, quantity: int, price: int or float):
        if name not in self.__cart_items:
            self.__cart[name] = [quantity, price]
        else:
            self.__cart[name][0] += 1
        self.__total += (quantity*price)

    def remove_product(self, name):
        if name in self.__cart_items:
            to_be_deducted = self.__cart[name][-1]
            if self.__cart[name][0] == 0:
                del self.__cart[name]
            else:
                self.__cart[name][0] -= 1
            self.__total -= to_be_deducted
        else:
            print('Product not found.')

    def calculate_total(self):
        return self.__total

    def view_products(self):
        items = [key for key in self.__cart.keys()]
        print(f'{items}')

    def __repr__(self):
        print_str = ''
        for key in self.__cart.keys():
            print_str += f'product: {key}, quantity:{self.__cart[key][0]}, price: {self.__cart[key][1]}$\n'
        return print_str


if __name__ == '__main__':
    print('Stack')
    print('------------------------------------------------')
    st = Stack()
    print(st)
    st.push(1)
    print(st)
    st.push(2)
    print(st)
    st.push(3)
    print(st)
    st.push(4)
    print(st)
    st.pop()
    st.pop()
    print(st)
    st.top()
    print('Shopping Cart')
    print('------------------------------------------------')
    my_cart = ShoppingCart()
    my_cart.add_product('Eggs', quantity=12, price=1)
    my_cart.add_product('Bread', quantity=2, price=4)
    print(my_cart)
    my_cart.remove_product('Eggs')
    print(my_cart)
    my_cart.remove_product('Eggs')
    print(my_cart)
    print(my_cart.calculate_total())
    my_cart.view_products()





