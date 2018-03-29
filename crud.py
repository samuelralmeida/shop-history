# encoding: utf-8

import model


def add_user(name, email):
    user = model.User(
        name=name,
        email=email
    )
    return user.put()


def get_user_by_email(email):
    user = model.User.query(model.User.email == email).get()
    return user


def add_product(email, product, unity):
    user = get_user_by_email(email)
    product = model.Product(
        product=product,
        unity=unity,
        user=user.key
    )
    return product.put()


def get_products_by_user(email):
    user = get_user_by_email(email)
    products = model.Product.query(
        model.Product.user == user.key,
    )
    return products


def add_purchase(user, product, brand, price, quantity):
    purchase = model.Purchase(
        brand=brand,
        price=price,
        quantity=quantity,
        product=product.key,
        user=user.key
    )
    return purchase.put()
