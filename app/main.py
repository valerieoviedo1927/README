from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Servir archivos estáticos desde la carpeta 'static'
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


# Ruta para obtener información de un producto
@app.get("/product/{product_id}")
def read_product(product_id: int):
    return {"product_id": product_id, "name": f"Product {product_id}", "price": 25.99}


@app.get("/ping")
def ping():
    return {"ping": "pong"}


# Ruta para crear un nuevo producto
@app.post("/product/")
def create_product(product: dict):
    return {"message": "Product created", "product": product}


# Ruta para actualizar un producto
@app.put("/product/{product_id}")
def update_product(product_id: int, product: dict):
    return {"message": f"Product {product_id} updated", "product": product}


# Ruta para eliminar un producto
@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    return {"message": f"Product {product_id} deleted"}
