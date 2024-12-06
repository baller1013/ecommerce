from .cart import Cart

#create context processor so it can work on all pages
def cart(request):
    return {'cart': Cart(request)}