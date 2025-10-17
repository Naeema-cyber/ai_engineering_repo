class ProductCategory:
    def __init__(self, category_id, name, description=None, is_active=True):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.is_active = is_active
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]

    def get_products(self):
        return self.products

    def __str__(self):
        return f"{self.name} ({len(self.products)} items)"
    
    

            

class Product:
    def __init__(self, product_id, name, price, quantity, seller_contact, description=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.seller_contact = seller_contact
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.price} NGN ({self.quantity} units)"