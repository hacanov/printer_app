from pydantic import BaseModel

class ModifyBaseModel(BaseModel):
    id: int = 0
    
class User(BaseModel):
    position: str
    login: str
    password: str
    power_level: int


class Order(BaseModel):
    user_id: int
    order_date: str
    status: str


class Customer(BaseModel):
    customer_name: str 
    contact_info: str 


class Product(BaseModel):
    product_name: str
    price: float 
    stock_quantity: int


class Printer(BaseModel):
    printer_name: str
    printer_type: str


class PrintJob(BaseModel):
    order_id: int
    printer_id: int
    job_status: str 
