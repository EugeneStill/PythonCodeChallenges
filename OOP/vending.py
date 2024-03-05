import unittest
from unittest.mock import patch
from io import StringIO


class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.restock_message = f"Restocked {self.name}.  {self.quantity} now available."

    def get_quantity(self):
        return self.quantity
    def decrease_quantity(self):
        if self.get_quantity() > 0:
            self.quantity -= 1
            return True
        return False

    def increase_quantity(self, quantity):
        self.quantity += quantity
        print(self.restock_message)


class VendingMachine():

    def __init__(self):
        self.products = {}
        self.balance = 0
        self.insufficient_funds_msg = "Insufficient funds to buy product"
        self.product_does_not_exist_msg = "{} does not exist in this vending machine"
        self.out_of_stock_msg = "{} is out of stock"
        self.purchase_msg = "Here is your {}"

    def add_product(self, product):
        self.products[product.name] = product

    def insert_coin(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def display_products(self):
        for product_name in self.products:
            product = self.products.get(product_name)
            print(f"{product.name}, Price: {product.price}, Qty: {product.quantity}")

    def get_product(self, product_name):
        product = self.products.get(product_name)
        if not product:
            print(self.product_does_not_exist_msg.format(product_name))
            return
        if product.price > self.balance:
            print(self.insufficient_funds_msg)
        elif product.decrease_quantity():
            print(self.purchase_msg(product_name))
        else:
            print(self.out_of_stock_msg.format(product_name))


class VendingTests(unittest.TestCase):
    def test_product_init(self):
        name, price, quantity = "Coke", 10, 5
        new_product = Product(name, price, quantity)
        self.assertEqual((new_product.name, new_product.price, new_product.quantity), (name, price, quantity),
            f"Expected Product Name {name} Price {price} Qty {quantity} but got {new_product.name}, {new_product.price},"
            f" {new_product.price}")

    def test_product_valid_decrease(self):
        name, price, quantity = "Coke", 10, 1
        new_product = Product(name, price, quantity)
        new_product.decrease_quantity()
        self.assertEqual(new_product.quantity, 0,
            f"Expected 0 instances of {new_product.name} but found {new_product.quantity}")

    def test_product_invalid_decrease(self):
        name, price, quantity = "Coke", 10, 0
        new_product = Product(name, price, quantity)
        self.assertFalse(new_product.decrease_quantity(),
            f"Expected decrease of product with 0 quantity to fail, but decrease did not fail. "
            f"Updated qty = {new_product}")

    def test_vending_init(self):
        vm = VendingMachine()
        self.assertEqual(vm.get_balance(), 0, f"Expected new vending machine to have 0 balance, but found "
            f"{vm.balance}")

    def test_vending_add_proucts(self):
        vm = VendingMachine()
        vm.add_product(Product("Chips", 15, 3))
        vm.add_product(Product("Cookies", 20, 7))
        self.assertEqual(len(vm.products), 2, f"Expected new vending machine to have 2 products, "
            f"but found {len(vm.products)}")

    @patch('sys.stdout', new_callable=StringIO)
    def test_get_invalid_product(self, mock_stdout):
        vm = VendingMachine()
        vm.add_product(Product("Chips", 15, 3))
        vm.get_product("Cake")
        printed_output = mock_stdout.getvalue().strip()
        self.assertEqual(printed_output, vm.product_does_not_exist_msg.format("Cake"),
            "Attempt to get non-existent product did not fail")

    def get_new_frame(self, og_frame):
        new_frame: pd.DataFrame = og_frame.apply(update_frame, axis=1, result_type="expand").dropna(axis=0, how="all")
        if not new_frame.empty:
            return 1
        else:
            return 0
    @patch('sys.stdout', new_callable=StringIO)
    def test_insufficient_funds(self, mock_stdout):
        vm = VendingMachine()
        vm.add_product(Product("Chips", 1, 3))
        vm.get_product("Chips")
        printed_output = mock_stdout.getvalue().strip()
        self.assertEqual(printed_output, vm.insufficient_funds_msg,
            "Able to purchase item with insufficient funds")

    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_purchase(self, mock_stdout):
        vm = VendingMachine()
        vm.insert_coin(25)
        vm.add_product(Product("Coke", 25, 3))
        vm.get_product("Coke")
        printed_output = mock_stdout.getvalue().strip()
        self.assertEqual(printed_output, vm.purchase_msg.format("Coke"),
            "Not able to purchase item with sufficient funds")

    @patch('sys.stdout', new_callable=StringIO)
    def test_out_of_stock(self, mock_stdout):
        vm = VendingMachine()
        vm.insert_coin(25)
        vm.add_product(Product("Coke", 25, 0))
        vm.get_product("Coke")
        printed_output = mock_stdout.getvalue().strip()
        self.assertEqual(printed_output, vm.out_of_stock_msg.format("Coke"),
            "Able to pay for item that was out of stock")