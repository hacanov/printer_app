from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(pydantic_model=pydantic_models.User, database_model=database_models.User, prefix='/users', tags=['Users']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Customer, database_model=database_models.Customer, prefix='/customers', tags=['Customers']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Printer, database_model=database_models.Printer, prefix='/printers', tags=['Printers']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Order, database_model=database_models.Order, prefix='/orders', tags=['Orders']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.PrintJob, database_model=database_models.PrintJob, prefix='/print_jobs', tags=['PrintJobs']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Product, database_model=database_models.Product, prefix='/products', tags=['Products']).fastapi_router
)
