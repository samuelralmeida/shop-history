# encoding: utf-8

from google.appengine.ext import ndb


class User(ndb.Model):
    """Sub model for representing an user."""
    name = ndb.UserProperty()
    email = ndb.StringProperty()


class Purchase(ndb.Model):
    """Sub model for representing a purchase."""
    product = ndb.StringProperty()
    brand = ndb.StringProperty()
    price = ndb.FloatProperty()
    unity = ndb.StringProperty()
    purchase_date = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.StructuredProperty(User)
