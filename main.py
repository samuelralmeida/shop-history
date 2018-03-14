# encoding: utf-8

import random
import string

from google.appengine.api import users

from flask import Flask, render_template, request
from flask import session as login_session

app = Flask(__name__)


def get_user():
    users.get_current_user()


@app.route('/')
@app.route('/login')
def show_login():
    # state = ''.join(random.choice(string.ascii_uppercase + string.digits)
    #                 for x in xrange(32))
    # login_session['state'] = state
    # return render_template('login.html', STATE=state)
    return 'pagina inicial e login'


@app.route('/logout')
def logout():
    return 'logout'


@app.route('/prepare')
def prepare_list():
    return 'preparar lista'


@app.route('/market')
def market():
    return 'mercado'


@app.route('/create/product')
def create_product():
    return 'criar produto'


@app.route('/edit/product')
def edit_product():
    return 'editar produto'


@app.route('/delete/product')
def delete_product():
    return 'deletar produto'


@app.route('/make/purchase')
def make_purchase():
    return 'fazer purchase'


@app.route('/edit/purchase')
def edit_purchase():
    return 'editar purchase'


@app.route('/delete/purchase')
def delete_purchase():
    return 'deletar purchase'


"""
@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
"""
