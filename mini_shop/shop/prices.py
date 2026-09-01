from .utils import format_price

def add_tax(price, tax):
    return price*(1+tax)




def discount(price, percent):
    return price*percent