from products import dao


class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost * 2
        self.qty = qty * 2

    @staticmethod
    def load(data: dict) -> 'Product':
        """Create a Product instance from a dictionary."""
        return Product(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data['qty']
        )


def list_products() -> list[Product]:
    """Retrieve and load all products from the DAO."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Retrieve a single product by ID from the DAO."""
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} does not exist.")
    return Product.load(product_data)


def add_product(product: dict):
    """Add a new product to the DAO."""
    required_keys = {'id', 'name', 'description', 'cost', 'qty'}
    if not required_keys.issubset(product):
        raise KeyError(f"Missing required product keys: {required_keys - product.keys()}")
    product['cost'] *= 2
    product['qty'] *= 2
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Update the quantity of a product by ID."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    if not dao.get_product(product_id):
        raise ValueError(f"Product with ID {product_id} does not exist.")
    dao.update_qty(product_id, qty * 2)