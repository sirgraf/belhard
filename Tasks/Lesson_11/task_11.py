from datetime import date
from csv import reader, DictReader, writer, DictWriter
import psycopg2
from pathlib import Path
import pandas as pd

class Base(object):
    conn = psycopg2.connect(dbname='belhard', user='db_test_user', password='123', host='localhost')
    conn.autocommit = True
    cur = conn.cursor()


class DB_work(Base):
    ROOT_PATH = Path(__file__).resolve().parent.parent.parent
    obj_type_list = ['T', 'C']
    table_col_type = ["int", "bool", "char", "date", "varchar"]


    @classmethod
    def init(cls):
        cls.cur.execute("CREATE SCHEMA IF NOT EXISTS dbo AUTHORIZATION db_test_user")

    @classmethod
    def create(cls, obj_type: str, obj_name: str, col_list: list = None) -> None:
        if obj_type not in cls.obj_type_list:
            return
        if obj_type == 'T':
            if not isinstance(obj_name, str):
                raise TypeError('Table name should be `str` type')

            dml_command = f"CREATE TABLE IF NOT EXISTS dbo.{obj_name} "

            for index, col_dict in enumerate(col_list):
                if not isinstance(col_dict, dict):
                    raise TypeError('Every column definition should be `dict` structure')

                if col_dict.get('name') is None:
                    raise ValueError('Column definition should have `name` dict key')
                if col_dict.get('type') is None:
                    raise ValueError('Column definition should have `type` dict key')
                if col_dict.get('type') not in cls.table_col_type:
                    raise ValueError('Wrong column type ')

                col_name = col_dict.get('name')
                col_type = col_dict.get('type')
                col_len = col_dict.get('len')

                if index == 0:
                    dml_command += f"({col_name} {col_type} {'(' + str(col_len) + ')' if col_len is not None else ''}" \
                                   f" {');' if index + 1 == len(col_list) else ', '}"
                else:
                    dml_command += f"{col_name} {col_type} {'(' + str(col_len) + ')' if col_len is not None else ''}" \
                                   f" {');' if index + 1 == len(col_list) else ', '}"

            cls.cur.execute(dml_command)
            # cls.conn.commit()

    @classmethod
    def manager_populate(cls, name: str, surname: str, is_active: bool = True):
        cls.cur.execute(f'''
            INSERT INTO dbo.manager (name, surname, is_active, date_add)
            VALUES(%s, %s, %s, %s);
        ''', (name, surname, is_active, date.today()))

    @classmethod
    def prod_cat_populate(cls, name: str, is_active: bool = True):
        cls.cur.execute(f'''
                    INSERT INTO dbo.productCategory (name, is_active)
                    VALUES(%s, %s);
                ''', (name, is_active))

    @classmethod
    def product_populate(cls, name: str, cost: float, prod_cat_id: int, is_active: bool = True, weight: int = None):
        cls.cur.execute(f'''
            INSERT INTO dbo.product (productCategoryId, name, cost, is_active, date_add, weight)
            VALUES(%s, %s, %s, %s, %s, %s);
        ''', (prod_cat_id, name, cost, is_active, date.today(), weight))

    @classmethod
    def sales_populate(cls, quantity: int, prod_id: int, manager_id: int):
        cls.cur.execute(f'''
               INSERT INTO dbo.sales (productId, managerId, quantity, date_sale)
               VALUES(%s, %s, %s, %s);
           ''', (prod_id, manager_id, quantity, date.today()))


    @classmethod
    def get_sales(cls, name: str, surname: str) -> tuple:
        cls.cur.execute('''
            SELECT concat(m.name, ' ', m.surname) as Manager, pc.name as "Product category", p.name as Product
                    , sum(p.cost * s.quantity) as "Sales volume" 
            FROM dbo.sales s 
                join dbo.manager m on s.managerId = m.id
                join dbo.product p on s.productId = p.id
                join dbo.productCategory pc on p.productCategoryId = pc.id
            where m.surname = %s and m.name = %s
            group by concat(m.name, ' ', m.surname), pc.name, p.name
        ''', (surname, name))
        obj = cls.cur.fetchall()
        return obj #cls.cur.fetchone()


    @classmethod
    def __get_prod_cat_id(cls, name: str) -> int:
        cls.cur.execute('''
            SELECT id
            FROM dbo.productcategory
            WHERE name = %s
        ''', (name, ))
        # obj = cls.cur.fetchone()
        return cls.cur.fetchone()

    @classmethod
    def csv_2_db(cls, csv_name: str):
        with open(cls.ROOT_PATH.joinpath(csv_name), 'r', encoding='utf-8') as file:
            r = DictReader(file)
            for product in r:
                prod_cat_id = cls.__get_prod_cat_id(product.get('category'))
                if prod_cat_id is None:
                    continue
                cls.product_populate(product.get('name'), product.get('cost'), prod_cat_id[0], True
                                     , None if product.get('weight') == '' else product.get('weight'))


    @classmethod
    def db_2_csv(cls, csv_name: str, table_name: str = None):
        column_names = []
        formatted_data = []

        table_data = cls.get_sales('John', 'Kerry')
        column_names = [desc[0] for desc in cls.cur.description]
        formatted_data = [list(elem) for elem in table_data]
        df = pd.DataFrame(formatted_data, columns=column_names)
        with open(cls.ROOT_PATH.joinpath(csv_name), 'a', encoding='utf-8') as file:
            df.to_csv(file, index=False, lineterminator='\n')





DB_work.init()
# DB_work.csv_2_db('products.csv')
DB_work.db_2_csv('sales.csv')
# print(DB_work.get_sales('John', 'Kerry'))
# DB_work.manager_populate('John', 'Kerry')
# DB_work.manager_populate('Mary', 'Johnson')
# DB_work.prod_cat_populate('clothes')
# DB_work.prod_cat_populate('car')
# DB_work.prod_cat_populate('food')
# DB_work.product_populate('Jeans', 13.4, 1)
# DB_work.product_populate('Audi A4', 50450, 2)
# DB_work.product_populate('Juice', 2, 3)
# DB_work.sales_populate(3, 1, 1)
# DB_work.sales_populate(1, 2, 2)
# DB_work.sales_populate(11, 3, 1)

columns = [
    {
        "name": "col1",
        "type": "int"
    },
    {
        "name": "col2",
        "type": "varchar",
        "len": 10
    }
]
DB_work.create('T', 'TestTable', columns)
DB_work.cur.execute('''
    CREATE TABLE IF NOT EXISTS dbo.productCategory(
        id serial PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        is_active BOOL NOT NULL DEFAULT TRUE
        )
        '''
                    )

DB_work.cur.execute('''
    CREATE TABLE IF NOT EXISTS dbo.product(
        id serial PRIMARY KEY,
        productCategoryId INT NOT NULL,
        name VARCHAR(50) UNIQUE NOT NULL,
        cost DECIMAL(12,2) NOT NULL,
        is_active BOOL NOT NULL DEFAULT TRUE,
        date_add DATE NOT NULL,
        date_end DATE,
        weight INT,
        FOREIGN KEY (productCategoryId) REFERENCES dbo.productCategory(id)
    )
''')

DB_work.cur.execute('''
    CREATE TABLE IF NOT EXISTS dbo.manager(
        id serial PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        is_active BOOL NOT NULL DEFAULT TRUE,
        date_add DATE NOT NULL,
        date_modified DATE
    )
''')

DB_work.cur.execute('''
    CREATE TABLE IF NOT EXISTS dbo.sales(
        id serial PRIMARY KEY,
        productId INT NOT NULL,
        managerId INT NOT NULL,
        quantity INT NOT NULL,
        date_sale DATE NOT NULL,
        FOREIGN KEY (productId) REFERENCES dbo.product(id),
        FOREIGN KEY (managerId) REFERENCES dbo.manager(id)
    )
''')