import pytest
from unittest.mock import Mock
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:

    @pytest.fixture
    def ingredient_list(self):
        cheese = Mock()
        cheese.configure_mock(ingredient_type=INGREDIENT_TYPE_FILLING, name='Сыр', price=100)
        cheese.get_price.return_value = 100
        cheese.get_name.return_value = 'Сыр'
        cheese.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger = Mock()
        burger.configure_mock(ingredient_type=INGREDIENT_TYPE_FILLING, name='Котлета', price=200)
        burger.get_price.return_value = 200
        burger.get_name.return_value = 'Котлета'
        burger.get_type.return_value = INGREDIENT_TYPE_FILLING

        ketchup = Mock()
        ketchup.configure_mock(ingredient_type=INGREDIENT_TYPE_SAUCE, name='Кетчуп', price=50)
        ketchup.get_price.return_value = 50
        ketchup.get_name.return_value = 'Кетчуп'
        ketchup.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient_list = [cheese, burger, ketchup]
        return  ingredient_list

    @pytest.fixture
    def hamburger_sample(self, ingredient_list):
        hamburger = Burger()

        bun = Mock()
        bun.configure_mock(name='Кунжутная булочка',price = 100)
        bun.get_price.return_value=100
        bun.get_name.return_value = 'Кунжутная булочка'

        hamburger.bun=bun
        hamburger.ingredients=ingredient_list
        return hamburger

    def test_bun_name_in_hamburger_true(self, hamburger_sample):
        assert hamburger_sample.bun.name == 'Кунжутная булочка'

    def test_bun_price_in_hamburger_true(self, hamburger_sample):
        assert hamburger_sample.bun.price == 100

    def test_ingredients_in_hamburger_true(self, hamburger_sample, ingredient_list):
        assert hamburger_sample.ingredients == ingredient_list

    def test_set_buns_true(self):
        hamburger = Burger()
        bun = Mock()
        bun.configure_mock(name='Кунжутная булочка', price=100)
        hamburger.set_buns(bun)
        assert hamburger.bun == bun

    def test_add_ingredient_true(self, hamburger_sample):
        pineapple = Mock()
        pineapple.configure_mock(ingredient_type=INGREDIENT_TYPE_FILLING, name='Ананас', price=1.25)
        hamburger_sample.add_ingredient(pineapple)
        assert hamburger_sample.ingredients[-1] == pineapple

    def test_del_ingredient_true(self, hamburger_sample, ingredient_list):
        hamburger_sample.remove_ingredient(-1)
        ingredient_list.pop(-1)
        assert hamburger_sample.ingredients==ingredient_list

    def test_move_ingredient_true(self, hamburger_sample, ingredient_list):
        hamburger_sample.move_ingredient(-1,0)
        ingredient_list.insert(0,ingredient_list.pop(-1))
        assert hamburger_sample.ingredients==ingredient_list

    def test_get_price_true(self, hamburger_sample):
        assert hamburger_sample.get_price() == 550

    def test_get_receipt_true(self, hamburger_sample):
        receipt = ('(==== Кунжутная булочка ====)\n'
 '= filling Сыр =\n'
 '= filling Котлета =\n'
 '= sauce Кетчуп =\n'
 '(==== Кунжутная булочка ====)\n'
 '\n'
 'Price: 550')
        assert hamburger_sample.get_receipt() == receipt