"""
DSC 20 Final Project
Name: Zhenjian Wang
PID:  A15880200
"""
from util import Stack, Queue
from datetime import datetime



def doctest():
    """
    ------------------------ PRODUCT TEST ------------------------

    >>> p1 = Product("iphone",399)
    >>> p2 = Special_Product("macbook air",999)
    >>> p3 = Limited_Product("free iphone", 0, 10)
    >>> p1, p2, p3
    (PRODUCT <0>, PRODUCT <1>, PRODUCT <2>)
    >>> print(p1)
    <0> iphone - 399$
    >>> print(p2)
    <1> macbook air - 999$ (special)
    >>> print(p3)
    <2> free iphone - 0$ (10 left)

    ------------------------ WAREHOUSE TEST ------------------------

    >>> wh = Warehouse()
    >>> st = Store(wh)
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> print(wh)
    Warehouse with 3 products
    >>> print(wh.get_product(1))
    <1> macbook air - 999$ (special)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <0> iphone - 399$
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (10 left)
    ============================
    >>> wh.export_product(3)
    >>> wh.export_product(2)
    PRODUCT <2>
    >>> wh.remove_product(0)
    True
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (9 left)
    ============================
    >>> st.view_products(sort = True)
    ============================
    <ID> Product - Price
    <2> free iphone - 0$ (9 left)
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.remove_product(0)
    False
    >>> [wh.export_product(2) for i in range(9)]
    [PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>,\
 PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>]
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.show_log()
    Product <0> imported - 2020-11-26 07:09:17.709522
    Product <1> imported - 2020-11-26 07:09:17.709584
    Product <2> imported - 2020-11-26 07:09:17.709612
    Product <2> exported - 2020-11-26 07:09:17.709745
    Product <0> removed  - 2020-11-26 07:09:17.709776
    Product <2> exported - 2020-11-26 07:09:17.709886
    Product <2> exported - 2020-11-26 07:09:17.709893
    Product <2> exported - 2020-11-26 07:09:17.709897
    Product <2> exported - 2020-11-26 07:09:17.709901
    Product <2> exported - 2020-11-26 07:09:17.709905
    Product <2> exported - 2020-11-26 07:09:17.709909
    Product <2> exported - 2020-11-26 07:09:17.709913
    Product <2> exported - 2020-11-26 07:09:17.709916
    Product <2> exported - 2020-11-26 07:09:17.709920
    Product <2> removed  - 2020-11-26 07:09:17.709924

    ------------------------ USER TEST ------------------------

    >>> u1 = User( 'Jerry', st)
    >>> u2 = Premium_User( 'FYX', st)
    >>> u1
    USER<0>
    >>> u2
    USER<1>
    >>> print(u1)
    standard user: Jerry - 0$
    >>> u2.add_balance(2000)
    >>> print(u2)
    premium user: FYX - 2000$
    >>> wh.import_product(p1)
    >>> u1 = User("A",st)
    >>> u1.add_cart(0)
    >>> u1.add_cart(0)
    >>> u1.view_cart()
    (front) <0> iphone - 399$ -- <0> iphone - 399$ (rear)
    >>> u1.checkout()
    STORE: Not enough money QQ
    []
    >>> u1.add_balance(1000)
    >>> u1.checkout()
    STORE: A ordered iphone. A has 562$ left.
    STORE: A ordered iphone. A has 124$ left.
    [PRODUCT <0>, PRODUCT <0>]
    >>> p4 = Limited_Product("Ipad", 600, 5)
    >>> wh.import_product(p4)
    >>> u2.buy_all(3)
    STORE: FYX ordered Ipad. FYX has 1400$ left.
    STORE: FYX ordered Ipad. FYX has 800$ left.
    STORE: FYX ordered Ipad. FYX has 200$ left.
    STORE: Not enough money QQ
    [PRODUCT <3>, PRODUCT <3>, PRODUCT <3>]

    ------------------- HISTORY / UNDO TEST -------------------

    >>> u1.view_history()
    (bottom) <0> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903632 -- \
<1> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903658 (top)
    >>> u1.undo_purchase()
    STORE: A refunded iphone. A has 523$ left.


    -------------------------- EC TEST ------------------------
    >>> p1 = Product("A",20)
    >>> p2 = Special_Product("B",7)
    >>> p3 = Limited_Product("C", 1, 2)
    >>> wh = Warehouse()
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> st = Store(wh)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <4> A - 20$
    <5> B - 7$ (special)
    <6> C - 1$ (2 left)
    ============================
    >>> st.so_rich(45)
    1
    >>> st.so_rich(61)
    0
    >>> st.so_rich_recursive(45)
    1
    >>> st.so_rich_recursive(61)
    0
    """
    pass

#######################################################################
#                               PRODUCT                               #
#######################################################################
class Product:
    """ The Product class provides abstraction to 
    the products available in our system.  
    """

    ##### Part 1.1 #####
    product_counter = 0
    def __init__(self, name, price):
        """ a constructor for the Product instance """
        # YOUR CODE GOES HERE #
        self.name = name
        Product.product_counter += 1
        self.price = price
        self.id = Product.product_counter - 1
        
        

    def __str__(self):
        """ this function returns a string representation """
        return '<{}> {} - {}$'.format(self.id, self.name, self.price)

    def __repr__(self):
        """ this function returns another string representation """
        return 'PRODUCT <{}>'.format(self.id)


class Limited_Product(Product):
    """ a subclass of Product, represents product that has limited amount """

    ##### Part 1.2 #####
    def __init__(self, name, price, amount):
        """ a constructor for Limited_Product """
        
        super(Limited_Product, self).__init__(name, price)
        self.amount = amount

    def __str__(self):
        """ the function returns a string representation """
        return '<{}> {} - {}$ ({} left)'.format(self.id, self.name, \
                                                self.price, self.amount)



class Special_Product(Product):
    """ A subclass of Product, represents products that sell to premium users
    only """

    ##### Part 1.3 #####
    def __init__(self, name, price, description="special"):
        """ a constructor for Special_Product """
      
        super(Special_Product, self).__init__(name, price)
        self.description = description

    def __str__(self):
        """ this function returns a string representation """
        return '<{}> {} - {}$ ({})'.format(self.id, self.name, \
                                           self.price, self.description)



#######################################################################
#                              WAREHOUSE                              #
#######################################################################


class Warehouse:
    """ A class that provides abstraction to the warehouses, which stores all
    products for a particular store.  """

    ##### Part 2 #####
    def __init__(self):
        """ A constructor for Warehouse instance """
        self.inventory = {}
        self.log = []

    def __str__(self):
        """ this function returns a string representation """
        return 'Warehouse with {} products'. format(len(self.inventory))


    def get_product(self, product_id):
        """ 
        this function returns the product instance with the given id
        from the inventory 
        """
        if product_id in self.inventory.keys():
            return self.inventory[product_id]
        return None

    def list_products(self):
        """ this function returns a list of all actual product instances 
        stored in the inventory.
        """
        return list(self.inventory.values())

    def remove_product(self, product_id):
        """ this function removes the product instance with the given id  
        from the inventory. 
        """
        if product_id in self.inventory.keys():
            del self.inventory[product_id]
            self.log.append('Product <{}> removed  - {}'.\
                            format(product_id, datetime.now()))
            return True
            
        else:
            return False
            
        
    def import_product(self, product):
        """ the function imports the product to the inventory. """
        if product.id not in self.inventory.keys():
            self.inventory[product.id] = product
            self.log.append('Product <{}> imported - {}'.\
                            format(product.id, datetime.now()))

    def export_product(self, product_id):
        """ the function exports the product instance with the given id
        from the inventory. 
        """
        if product_id in self.inventory.keys():
            
            # if this is a limited product
            if type(self.inventory[product_id]).__name__ == 'Limited_Product':
                self.inventory[product_id].amount -= 1
                self.log.append('Product <{}> exported - {}'.format(product_id, datetime.now()))
                # when the limited product only has 1 or less
                if self.inventory[product_id].amount == 0:
                    self.log.append('Product <{}> removed  - {}'.format\
                            (product_id, datetime.now()))
                        
                    # create a copy of the inventory list and edit on that
                    variable = self.inventory.copy()
                    del self.inventory[product_id]
                    return variable[product_id]
                else:
                    return self.inventory[product_id]  
            else:
                
                # the following code applies to non-limited product
                self.log.append('Product <{}> exported - {}'.format\
                            (product_id, datetime.now()))
                return self.inventory[product_id]
        
        else:
            return None

    def size(self):
        """ the function returns the number of products stored in the 
        inventory.
        """
        return len(self.inventory)

    def show_log(self):
        """ the function prints all log strings in the log. """
        print(*self.log, sep="\n")
            


#######################################################################
#                               HISTORY                               #
#######################################################################
class History:
    """ A class that provides abstraction to the purchase history records """

    ##### Part 3 #####
    history_counter = 0
    def __init__(self, product, user):
        """ A constructor for History instance """
        self.product = product
        self.user = user
        History.history_counter += 1
        self.id = History.history_counter - 1
        self.time = datetime.now()

    def __str__(self):
        """ the function returns a string representation """
        return '<{}> {} bought {} at {}'.\
            format(self.id, self.user.id, self.product, self.time)


    def __repr__(self):
        """ the function returns another string representation """
        return 'HISTORY<{}> - {}'.format(self.id, self.time)
    

#######################################################################
#                                USER                                 #
#######################################################################
class User:
    """ The class provides abstraction to the users. """

    ##### Part 4.1 #####
    user_counter = 0
    def __init__(self, name, store):
        """ A constructor for User instance """

        self.name = name
        self.store = store
        self.balance = 0
        User.user_counter += 1
        self.id = User.user_counter - 1
        self.purchase_history = Stack()
        self.cart = Queue()
        Store.add_user(store, self)



    def __str__(self):
        """ TODO: Complete the docstring. """
        # this function returns a string representation #
        return 'standard user: {} - {}$'.format\
            (self.name, self.balance)

    def __repr__(self):
        """ this function returns a string representation """
        return 'USER<{}>'.format(self.id)
        


    def set_name(self, new_name):
        """ this function sets the name attribute to the new_name """
        self.name = new_name
        

    def get_name(self):
        """ this function gets the name attribute """
        return self.name

    def set_balance(self, amount):
        """ this function sets the balance attribute to the amount. """
        self.balance = amount

    def get_balance(self):
        """ this function gets the balance attribute. """
        return self.balance

    def add_balance(self, amount):
        """ this function increments the balance attribute by the specified 
        amount.
        """
        self.balance += amount

    def last_purchase(self):
        """ this function retrieves the last purchased history instance of 
        this user and return it.  
        """
        return self.purchase_history.pop()

    def view_history(self):
        """ this function prints the purchase history of this user. """
     
        print(str(self.purchase_history))

    def view_cart(self):
        """ this function prints the cart of this user. """
        print(str(self.cart))

    def clear_cart(self):
        """ this function removes all products in the cart """
        self.cart.clear()

    ##### Part 5.2 #####
    def add_cart(self, product_id):
        """ TODO: Complete the docstring. """
        if self.store.get_product(product_id) != None:
            self.cart.enqueue(self.store.get_product(product_id))
            

    def checkout(self):
        """ this function orders every item in the shopping cart from the 
        store and returns a list of purchased products.
        """
        lst = []
     
        while self.cart.peek() != None:
            orders = Store.order(self.store, self.id, self.cart.peek().id)
            # if the user has enough money to buy the product, then order
            if orders == False:
                return lst 
            else: 
                self.purchase_history.push(orders)
                lst.append(self.cart.dequeue())
        return lst
                

    ##### Part 5.3 #####
    def undo_purchase(self):
        """ This function undoes the last purchase of the user. """
        if self.purchase_history.size() == 0:
            print('USER: no purchase history')
        else:
            if Store.undo_order(self.store, self.id, self.purchase_history.peek().product) == True:
                self.purchase_history.pop()

class Premium_User(User):
    """ a subclass of User which have two extra functionalities. """
    

    ##### Part 4.2 #####
    def __str__(self):
        """ the function returns a string representation. """
        return 'premium user: {} - {}$'.format(self.name, self.balance)


    ##### Part 5.4 #####
    def buy_all(self, product_id):
        """ 
        this function repeatedly orders this product until the product 
        has no more offerings or the balance is exhausted.  
        """
        lst = []
        if type(self.store.get_product(product_id)).\
            __name__ != 'Limited_Product':
            print('USER: not a limited product')
            return []
        else:
            while True:
                orders = Store.order(self.store, self.id, product_id)
                if orders == False:
                    return lst 
                else:
                    lst.append(orders.product)
                    self.purchase_history.push(orders)
            return lst
                
                

    def undo_all(self):
        """ A function that iteratively cancels the last purchases until the 
        user does not have any records in purchase history, or the last 
        purchase is a limited product.
        """
        while True:
            if type(self.purchase_history.peek().product).__name__ !='Limited_Product' \
            and self.purchase_history.size() != 0:
                User.undo_purchase(self)
            else:
                break
       


#######################################################################
#                               STORE                                 #
#######################################################################
class Store:
    """ A class that provides abstractions to the stores. """

    ##### Part 4.3 #####
    def __init__(self, warehouse):
        """ a constructor for Store instance. """
        self.users = {}
        self.warehouse = warehouse
    
    
    def __str__(self):
        """ the function returns a string representation """
        return "STORE: store with {} users and {} products"\
            .format(len(self.users), len(self.warehouse.list_products()))

    def get_product(self, product_id):
        """ the function looks up a product instance with the provided 
        product_id from the warehouse and returns this product. 
        """
        return self.warehouse.get_product(product_id)

    def view_products(self, sort=False):
        """ the function prints all products in the inventory. """
        
        # when we do not require sort
        if sort == False:
            print('============================')
            print('<ID> Product - Price')
            print(*self.warehouse.list_products(), sep="\n")
            print('============================')
            
        # when we require sort
        else:
            print('============================')
            print('<ID> Product - Price')
            
            # sort the elements and append them to the empty_lst
            empty_lst = []
            origin = [j for j in self.warehouse.list_products()]
            while origin:
                min_ele = origin[0]
                for i in origin:
                    if i.price < min_ele.price:
                        min_ele = i
                empty_lst.append(min_ele)
                origin.remove(min_ele)
            print(*empty_lst, sep = '\n')
            print('============================')

    ##### Part 5.1 #####
    def add_user(self, user):
        """ A function that takes a user instance and records this instance 
        to the users dictionary. 
        """
        if user in self.users:
            print('STORE: User already exists')
            return False
        else:
            self.users[user.id] = user
            return True
        
   
    ##### Part 5.2 #####
    def order(self, user_id, product_id):
        """ 
        This function checks if the user could handle the order. If so, it
        deducts the payment from the user's balance, and exports the ordered
        product from the warehouse and prints a message.
        """
        
        # The product is not available in the store.
        if Store.get_product(self, product_id) == None:
            print('STORE: Product not found')
            return False
        
        # The user is not a premium user and could not order special product
        if type(self.users[user_id]).__name__ != 'Premium_User' and \
            type(self.warehouse.inventory[product_id]) == Special_Product:
            print('STORE: Special product is limited to premium user')
            return False
        
        # for premium users
        if type(self.users[user_id]).__name__ == 'Premium_User':
            
            # check the balance and make sure that user could afford the price
            if self.users[user_id].balance >= \
                self.warehouse.inventory[product_id].price:
                self.users[user_id].balance -= self.warehouse.\
                    inventory[product_id].price
                    
                # export the product from warehouse, print the message
                a = self.warehouse.export_product(product_id)
                print('STORE: {} ordered {}. {} has {}$ left.'\
                      .format(self.users[user_id].name,a.name, \
                                  self.users[user_id].name, \
                                      self.users[user_id].balance)) 
                item_1 = History(a, self.users[user_id])
                return item_1
            else:
                print('STORE: Not enough money QQ')
                return False
            
        # for the users that are not premium users
        else:
            
            # make sure that the user could afford the extra fee and price
            coef = 1.1
            if self.users[user_id].balance >= \
                (self.warehouse.inventory[product_id].price) * coef:
                self.users[user_id].balance -= int(self.warehouse.\
                    inventory[product_id].price * coef)
                    
                # export the product from warehouse and print a message
                a = self.warehouse.export_product(product_id)
                print('STORE: {} ordered {}. {} has {}$ left.'\
                      .format(self.users[user_id].name, a.name, \
                                  self.users[user_id].name, \
                                      self.users[user_id].balance)) 
                item_0 = History(a, self.users[user_id])
                return item_0
            else:
                print('STORE: Not enough money QQ')
                return False
            

    ##### Part 5.3 #####
    def undo_order(self, user_id, product):
        """ the function preceeds the refund process. """
        if type(product).__name__ == 'Limited_Product':
            print("STORE: can't refund Limited_Product")
            return False
        else:
            self.users[user_id].balance += product.price
            print('STORE: {} refunded {}. {} has {}$ left.'.format\
                  (self.users[user_id].name, product.name, \
                                  self.users[user_id].name, \
                                      self.users[user_id].balance))
            return True
        
    ##### Part 6 #####
    def so_rich(self, money):
        """ 
        this function returns what is the least amount of money left 
        after purchasing every possible item.
        """
 
        left = set([money])

        # get products
        lst = self.warehouse.list_products()
        
        # sort the items by their price
        empty_lst = []
        origin = [j for j in lst]
        while origin:
            min_ele = origin[0]
            for i in origin:
                if i.price < min_ele.price:
                    min_ele = i
            empty_lst.append(min_ele)
            origin.remove(min_ele)
        
        tmp_left = set()
        
        # the for loop will loop through the items which have the highest 
        # price to the items that have lowest price.
        for product in empty_lst[::-1]:   
            for m in left:
                # update tmp_left
                if type(product) != Limited_Product:
                    new_left = m
                    while new_left >= product.price:
                        new_left = new_left - product.price
                        tmp_left.add(new_left)
   
                else:
                    amount_0 = product.amount
                    # handle limited product
                    new_set = tmp_left.copy()
                    left_1 = min(new_set)
                    while left_1 >= product.price and amount_0 > 0:
                        left_1 = left_1 - product.price
                        tmp_left.add(left_1)
                        amount_0 -= 1
                   
                        
                        
        left = tmp_left

        return min(left)

    def so_rich_recursive(self, money):
        """ 
        This function does the same thing as so_rich but in a recursive
        way.
        """

        # get products
        lst = self.warehouse.list_products()
        

        def helper(lst, money):
            # base case
            if len(lst) == 0:
                return money

            cur_min = money
            product = lst[0]
            if type(product) != Limited_Product:
                tmp = money
                
                # find the mininum number
                while tmp >= 0:
                    cur_min = min(cur_min, helper(lst[1:], tmp))
                    tmp -= product.price
            else:
                tmp = money
                num = product.amount
                while tmp >= 0 and num >= 0:
                    cur_min = min(cur_min, helper(lst[1:], tmp))
                    tmp -= product.price
                    num -= 1
            return cur_min

        return helper(lst, money)



