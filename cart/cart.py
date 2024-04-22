from store.models import Product
class Cart():
    def __init__(self,request):
        self.session = request.session

        # Get the current session if it exists
        cart = self.session.get('cart')

        # if the user is new, no cart! create one !
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart



    def add(self, product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        #logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified= True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # get ids from cart
        product_ids = self.cart.keys()
        # use ids to lookup products in dataase model
        products = Product.objects.filter(id__in=product_ids)
       
        # return those looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # get cart
        ourcart = self.cart
        # update dictionaries
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart

        return thing