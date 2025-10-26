import unittest
from app import API, ProductIn


class TestApp(unittest.TestCase):
    def test_get(self):
        client = API()
        result = client.get()

        self.assertEqual(result["code"], 200)
        self.assertEqual(len(result["data"]), 1)

    def test_post(self):
        client = API()
        product = ProductIn(
            name="Procut 2",
            price=100,
            category="Category 2",
        )
        result = client.post(product)

        self.assertEqual(result["code"], 201)
        self.assertIsNotNone(result["data"])
        self.assertIsNotNone(result["data"]["id"])

    def test_post_validation_error(self):
        client = API()
        product = ProductIn(
            name="Procut 2",
            price=-1,
            category="Category 2",
        )
        result = client.post(product)

        self.assertEqual(result["code"], 422)
        self.assertIn("Price cannot be less than 0", result["error"])


if __name__ == "__main__":
    unittest.main()
