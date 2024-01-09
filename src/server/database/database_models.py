from peewee import *
import peewee
import settings


db = peewee.SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    position = CharField(default='')
    login = CharField(unique=True, default='')
    password = CharField(default='')
    power_level = IntegerField(default=0)


class Order(BaseModel):
    user_id = ForeignKeyField(User, backref='orders', default=0)
    order_date = DateTimeField(default='')
    status = CharField(default='')


class Customer(BaseModel):
    customer_name = CharField(default='')
    contact_info = CharField(default='')


class Product(BaseModel):
    product_name = CharField(default='')
    price = DecimalField(default=0)
    stock_quantity = IntegerField(default=0)


class Printer(BaseModel):
    printer_name = CharField(default='')
    printer_type = CharField(default='')


class PrintJob(BaseModel):
    order_id = ForeignKeyField(Order, backref='print_jobs', default=0)
    printer_id = ForeignKeyField(Printer, backref='print_jobs', default=0)
    job_status = CharField(default='')


db.create_tables([User, Order, Customer, Product, Printer, PrintJob])