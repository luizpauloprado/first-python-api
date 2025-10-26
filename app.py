from dataclasses import dataclass, asdict


@dataclass
class ProductOut:
    id: int
    name: str
    price: float
    category: str


@dataclass
class ProductIn:
    name: str
    price: float
    category: str

    def validate(self):
        errors: list[str] = []

        if not self.name or not self.name.strip():
            errors.append("Name cannot be empty")

        if not self.price or self.price < 0:
            errors.append("Price cannot be less than 0")

        if not self.category or not self.category.strip():
            errors.append("Category cannot be empty")

        if errors:
            raise ValueError(", ".join(errors))


db: dict[int, ProductOut] = {
    1: ProductOut(id=1, name="Product A", price=10, category="Category A"),
}


class API:
    def __init__(self):
        self.db: dict[int, ProductOut] = {
            1: ProductOut(id=1, name="Product A", price=10, category="Category A"),
        }

    def get(self):
        try:
            products = [asdict(product) for product in self.db.values()]
            return {
                "code": 200,
                "data": products,
            }
        except Exception as exception:
            return {
                "code": 500,
                "error": str(exception),
            }

    def post(self, product: ProductIn):
        try:
            product.validate()

            next_id = max(self.db.keys(), default=0) + 1
            new_product = ProductOut(
                id=next_id,
                name=product.name,
                price=product.price,
                category=product.category,
            )

            db[next_id] = new_product

            return {
                "code": 201,
                "data": asdict(db[next_id]),
            }
        except (ValueError, TypeError) as validationError:
            return {
                "code": 422,
                "error": str(validationError),
            }
        except Exception as exception:
            return {
                "code": 500,
                "error": str(exception),
            }
