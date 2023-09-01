def check_user_shopping():
    user_shopping = input('Are you shopping? [y]es/[n]o?: ').lower()
    return True if user_shopping in 'yes' else False

def get_user_input():
    return input('What do you want to do? [a]dd,[d]elete,[s]howJ?: ').lower()
    
def add_to_cart(shopping_cart, item, price, quantity):
    if item not in shopping_cart:
      shopping_cart[item] = {
          'price': price,
          'quantity': quantity
      }
    else:
        shopping_cart[item]['quantity'] += quantity

def del_from_cart(shopping_cart, item):
    if item in shopping_cart:
      del shopping_cart[item]
    else:
        print('Item not in cart')

def display_cart(shopping_cart):
    total_price = 0
    for item, dict in shopping_cart.items():
      print(f'{item}\nquantity: {dict["quantity"]}\nprice: {dict["price"]}')
      total_price += dict["quantity"] * dict["price"]
    print(f'Total Price: {total_price:.2f}')

def driver(shopping_cart):
    while check_user_shopping():
        user_input = get_user_input()
        if user_input == 'a':
            item = input("what are we adding?: ")
            while True:
              try:
                price = float(input('What is price of item?: '))
                break
              except:
                 print("Please enter price in digits. Ex: 10.99")
            while True:
              quantity = input("How many are you adding? ")
              if quantity.isdigit():
                 quantity = int(quantity)
                 break
              else:
                 print("Please enter quantity in digits. Ex: 10")
            add_to_cart(shopping_cart, item, price, quantity)
        elif user_input == 'd':
            user_delete_option = input("what item are you deleting?: ")
            del_from_cart(shopping_cart, user_delete_option)
        elif user_input != 's':
            print('please enter valid option')
        display_cart(shopping_cart)

test_cart = {}
driver(test_cart)