#Body Shop
import datetime
from random_pass import random_pass_generator

help_commands = {
    'signup': 'Sign up as a new user.',
    'guest': 'Continue as a guest without logging in.',
    'logon': 'Log in if you are an existing user.',
    '/help': 'Display this help message.',
    '/main': 'Go back to the main menu.'

     #{command: discribtion, ... }
}
baskets = {} #{user: [product_id], ....}
current_user = dict()
product_catalog = {
    1: {
        'name': 'Heart',
        'description': 'A fully functional human heart, capable of sustaining life.',
        'price': 50000,  
        'availability': True,
        'category': 'Organs',
        'condition': 'New',
        'weight': '0.3kg'
    },
    2: {
        'name': 'Liver',
        'description': 'A healthy liver with excellent regenerative capabilities.',
        'price': 45000,
        'availability': True,
        'category': 'Organs',
        'condition': 'New',
        'weight': '1.5kg'
    },
    3: {
        'name': 'Kidney',
        'description': 'A pair of kidneys that function optimally with the ability to filter waste.',
        'price': 30000,
        'availability': True,
        'category': 'Organs',
        'condition': 'New',
        'weight': '0.5kg each'
    },
    4: {
        'name': 'Arm (Left)',
        'description': 'A fully functional human arm with muscle and bone structure.',
        'price': 25000,
        'availability': True,
        'category': 'Limbs',
        'condition': 'Used (Good condition)',
        'weight': '5kg'
    },
    5: {
        'name': 'Eye (Right)',
        'description': 'A pristine human eye with normal vision capacity.',
        'price': 10000,
        'availability': True,
        'category': 'Sensory Organs',
        'condition': 'New',
        'weight': '0.02kg'
    },
    6: {
        'name': 'Skin (Full Body)',
        'description': 'Full body skin transplant, ensuring natural look and texture.',
        'price': 20000,
        'availability': False,  
        'category': 'Skin Transplants',
        'condition': 'New',
        'weight': '5kg'
    },
    7: {
        'name': 'Lungs',
        'description': 'A set of healthy lungs, perfect for anyone needing respiratory support.',
        'price': 35000,
        'availability': True,
        'category': 'Organs',
        'condition': 'New',
        'weight': '1.0kg'
    },
    8: {
        'name': 'Spine',
        'description': 'A healthy spine with no fractures, maintaining the full range of motion.',
        'price': 15000,
        'availability': True,
        'category': 'Skeleton',
        'condition': 'Used (Excellent condition)',
        'weight': '3kg'
    },
    9: {
        'name': 'Brain',
        'description': 'A human brain with full cognitive function, ideal for advanced neurological applications.',
        'price': 100000,
        'availability': False,  # Temporarily unavailable
        'category': 'Organs',
        'condition': 'New',
        'weight': '1.3kg'
    },
    10: {
        'name': 'Spleen',
        'description': 'A healthy spleen to support immune system functionality and filtration.',
        'price': 25000,
        'availability': True,
        'category': 'Organs',
        'condition': 'New',
        'weight': '0.3kg'
    }
}

adminData = {'AdminSina':"0025991450"} 
userData = {1:{'sina':'sina885'}} #{code:{user: username, pass : password}, ... }
def entrence():

    print("-"*77)
    print(f"""|{"WELCOME TO BODYPART SHOP":^75}|""")
    print(f"""|{"hi this is a bodyshop where you can buy":^75}|""")
    print(f"""|{"differnt kinds of organs of Human!":^75}|""")
    print(f"""|{"if you are new please INSERT 'SIGNUP' OR 'GUEST' to continue as a guest":^75}|""")
    print(f"""|{"and if you are a memeber please INSERT 'LOGON'":^75}|""")
    print(f"""|{"if you want more information INSERT '/main'":^75}|""")
    print(f"""|{"if you want help INSERT '/help'":^75}|""")
    print(f"""|{"if you want to see the body organs INSERT '/products'":^75}|""")
    print(f"""|{"SIGNUP LOGON /help  /main /products":^75}|""")
    if logon():
        print(f"""|{"State : Logon":^75}|""")
    else:
        print(f"""|{"State : None":^75}|""")

    while True:
            command = input(""" WATING FOR YOU TO INSERT: """).lower().strip()
            if command == 'signup':
                signup()
            elif command == 'guest':
                pass
            elif command == 'logon':
                logon()
            elif command == '/help':
                help()
            elif command == '/main':
                entrence()
            else:
                print("plear enter a command")
                help()
def signup():
    code = len(userData)
    print('''hey there i hope you find the best out of our shop ''')
    print("""If you do not have a strong password, just type 'random' and we will generate one for you.""")
    user  = input('username : ').strip()
    password = input('password : ').strip()
    if password == 'random':
         password = random_pass_generator()
         print(f"Your new random password is: {password}")
         print('make sure to save this password unless you wont be able to enter the store')
    for users in userData[code].keys():
        if user == users:
            print(f"the username : {user}is taken")
            signup_again()
        return True
    if userData:
            userData[code] = {user:password}
            print(f"Welcome {user}, you've successfully signed up!")
    else:
        print(f'the username: {user} is already taken')

def signup_again():
    print("Please try again.")
    signup()
def logon():
    username = input('Enter your username: ').strip()
    password = input('Enter your password: ').strip()
    if username == 'AdminLog':
        admin_username = input("what is your username ")
        admin_password = input("what is your password")
        if admin_username in adminData and adminData[admin_username] == admin_password: 
            print("you have loged as admin succesfully")
            main()
            return True
    if username in userData and userData[username] == password:
        print("Login successful! Welcome back!")
        main()
        return True
    print("Invalid username or password.")
    main()
    return False
    
def help():
    print("Welcome to the Body Part Shop! Here are the available commands:")
    for command, description in help_commands.items():
        print(f"- {command}: {description}")
        main()
def main():
    entrence()


help_buy_product = {
    '/by_name'   : 'tell me the name and i chack the is we have it or not',
    '/by_id'     : 'you choose an ID then you see the info',
    '/see_all'   :'ypu will see the whle products again'
}


def buy_enternce():
    while True:
        print("write /help for further information")
        command = input("what do you want to do: ")
        if command == 'add_product':
            pass
        if command == "buy_product":
            buy_product()
        if command == "remove_product":
            pass
def buy_product():
    print('which products you want to buy.  WRITE HELP AND BACK TO GET THE MAIN MENU FOR INFO ')
    while True:
        command = input("what do you want to buy ").lower().strip()
        if command == 'back':
            buy_enternce()
        if command == '/buy_id' or 'buy_id':
            by_id()
        if command == '/buy_name' or 'by_name':
           by_name()
        if command == '/see_all':
            list_all_products()
        if command == 'help':
            print(help_buy_product)
            buy_product()
        else:
            print("make sure that your putting the corct command")
            buy_product()
def by_id():
    product_id = input("Enter the product ID you want to see: ").strip()
    if product_id.isdigit() and int(product_id) in product_catalog:
        product_id = int(product_id)
        print(f"Product Info: {product_catalog[product_id]}")
        add_to_basket(product_id)
    else:
        print("Specified ID not found or invalid format.")

def add_to_basket(product_id):
    if current_user not in baskets:
        print("You need to be logged in to add items to the basket.")
        return

    product = product_catalog.get(product_id)
    if product and product['availability']:
        baskets[current_user].append(product_id)
        print(f"Added {product['name']} to your basket.")
    else:
        print("The product is not available.")

def by_name():
    product_name = input("Enter the product name you want to view: ").strip().lower()
    found = False
    for product in product_catalog.values():
        if product_name in product['name'].lower():
            print(f"Product Info: {product}")
            found = True
            break
    if not found:
        print("Product not found with the given name.")

def list_all_products():
    print("Listing all available products:")
    for product_id, product in product_catalog.items():
        print(f"ID: {product_id}, Name: {product['name']}, Price: ${product['price']}, Available: {'Yes' if product['availability'] else 'No'}")
    
if __name__ == "__main__":
    entrence()
    print(userData)