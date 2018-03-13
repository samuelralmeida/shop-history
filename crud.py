# encoding: utf-8

import model


def add_user(name, email):
    user = model.User(
        name=name,
        email=email
    )
    user.put()


def add_product(name, email, product, brand, price, unity):
    purchase = model.Purchase(
        product=product,
        brand=brand,
        price=price,
        unity=unity
    )
    purchase.user = model.User(
        name=name,
        email=email
    )
    purchase.put()
