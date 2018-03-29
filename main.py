# encoding: utf-8

# import random
# import string
import crud

from google.appengine.api import users

from flask import Flask, render_template, request, jsonify
# from flask import session as login_session
from flask_jsglue import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)


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


@app.route('/create/product', methods=['GET', 'POST'])
def create_product():
    data = request.json
    if request.method == 'POST':
        product_name = data.get('name').lower().capitalize()
        unity = data.get('unity').lower()
        crud.add_product('samuel@gmail.com', product_name, unity)
        return 'produto criado'
    else:
        return 'criar produto'


@app.route('/products')
def products():
    text = 'pagina de produtos'
    return render_template('products.html', text=text)


@app.route('/edit/product')
def edit_product():
    return 'editar produto'


@app.route('/delete/product')
def delete_product():
    return 'deletar produto'


@app.route('/get/products')
def get_products():
    email = request.args.get('email')
    products_query = crud.get_products_by_user(email)
    list_of_products = []
    for product in products_query:
        prod = {
            'name': product.product,
            'unity': product.unity,
            'key': str(product.key.id())
                }
        list_of_products.append(prod)
    return jsonify(list_of_products)


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
