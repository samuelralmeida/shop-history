# encoding: utf-8

from google.appengine.ext import ndb


class User(ndb.Model):
    """Sub model for representing an user."""
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    group = ndb.StringProperty(default='user')


class Product(ndb.Model):
    """Sub model for representing a product."""
    product = ndb.StringProperty()
    unity = ndb.StringProperty()
    user = ndb.KeyProperty(kind=User)


class Purchase(ndb.Model):
    """Sub model for representing a purchase."""
    brand = ndb.StringProperty()
    price = ndb.FloatProperty()
    quantity = ndb.FloatProperty()
    purchase_date = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.KeyProperty(kind=User)
    product = ndb.KeyProperty(kind=Product)
