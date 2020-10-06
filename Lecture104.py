class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to Cart to",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "Kittikorn"
customer1.lastname = "P"
customer1.addCart()

customer2 = Customer()
customer2.name = "Warin"
customer2.lastname = "L"
customer2.addCart()

customer3 = Customer()
customer3.name = "Taweep"
customer3.lastname = "S"
customer3.addCart()

customer4 = Customer()
customer4.name = "Nattapol"
customer4.lastname = "C"
customer4.addCart()