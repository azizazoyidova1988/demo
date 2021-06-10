from django.db import connection
from contextlib import closing





def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from category""")
        categories = dict_fetchall(cursor)
        return categories

def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as c_name from product inner join category on 
        product.category_id=category.id """)
        products = dict_fetchall(cursor)
        return products

def get_chefs():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from chef""")
        chefs = dict_fetchall(cursor)
        return chefs

def get_customer():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from customer""")
        customers = dict_fetchall(cursor)
        return customers

def get_blog():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from blog""")
        blogs = dict_fetchall(cursor)
        return blogs

def get_blog_single(blog_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from blog where blog.id = %s""",[blog_id])
        blog = dict_fetchone(cursor)
        return blog


def get_categories_product_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  count(product.id),category.name ,product.category_id 
        FROM category LEFT JOIN product
		ON product.category_id=category.id
		GROUP BY product.category_id,category.name """)
        product_count = dict_fetchall(cursor)
        return product_count


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))