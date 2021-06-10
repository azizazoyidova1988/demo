from django.db import connection
from contextlib import closing

def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from category""")
        categories=dict_fetchall(cursor)
        return categories

def get_categories_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from category""")
        categories_count=dict_fetchall(cursor)
        return categories_count

def get_categories_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  count(product.id),category.name ,product.category_id
        FROM category LEFT JOIN product
		ON product.category_id=category.id
		GROUP BY product.category_id, category.name
        """)
        categories=dict_fetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from product""")
        products=dict_fetchall(cursor)
        return products

def get_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from product""")
        products_count=dict_fetchall(cursor)
        return products_count


def get_chefs():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from chef""")
        chefs=dict_fetchall(cursor)
        return chefs

def get_chefs_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from chef""")
        chefs_count=dict_fetchall(cursor)
        return chefs_count

def get_customer():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from customer""")
        customers=dict_fetchall(cursor)
        return customers

def get_customers_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from customer""")
        customers_count=dict_fetchall(cursor)
        return customers_count

# def get_views():
#     with closing(connection.cursor()) as cursor:
#         cursor.execute("""select name, sum(views) as count from dashboard_category
#         left join dashboard_news on dashboard_category.id=dashboard_news.category_id
#         group by name""")
#         views=dict_fetchall(cursor)
#         return views



def get_subjects_all():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(subject) from mentor_students """)
        subjects = dict_fetchall(cursor)
    return subjects


def get_frontend():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select count(subject) from mentor_students where subject = 'frontend' """)
        front = dict_fetchall(cursor)
    return front

def get_backend():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select count(subject) from mentor_students where subject = 'backend' """)
        front = dict_fetchall(cursor)
    return front

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