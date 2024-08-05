"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(990)
        assert product.quantity == 10

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 98)
        assert cart.products[product] == 99

    def test_remove_product(self, cart, product):
        cart.add_product(product, 720)
        cart.remove_product(product, 720)
        assert product not in cart.products
        cart.add_product(product, 270)
        cart.remove_product(product, 70)
        assert cart.products[product] == 200
        cart.remove_product(product, 200)
        assert product not in cart.products

    def test_remove_more_product_than_in_cart(self, cart, product):
        cart.add_product(product, 22)
        cart.remove_product(product, 77)
        assert product not in cart.products

    def test_remove_product_entirely(self, cart, product):
        cart.add_product(product, 77)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_products(self, cart, product):
        cart.add_product(product, 22)
        cart.clear()
        assert product not in cart.products

    def test_get_total_price_product(self, cart, product):
        cart.add_product(product, 7)
        assert cart.get_total_price() == 700

    def test_buy(self, product, cart):
        cart.add_product(product, 2)
        cart.buy()
        assert product.quantity == 998

    def test_trying_buy_more_than_possible(self, product, cart):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()
