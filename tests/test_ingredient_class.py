import pytest
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.fixture
    def ingredient_sample(self):
        ingredient = Ingredient(ingredient_type='', name='Сыр', price=0.8)
        return ingredient

    @pytest.mark.parametrize('type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_type_of_ingredient_true(self, ingredient_sample, type):
        ingredient_sample.type=type
        assert ingredient_sample.type == type

    def test_name_of_ingredient_true(self, ingredient_sample):
        assert ingredient_sample.name == 'Сыр'

    def test_price_of_ingredient_true(self, ingredient_sample):
        assert ingredient_sample.price == 0.8

    @pytest.mark.parametrize('type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_of_ingredient_true(self, ingredient_sample, type):
        ingredient_sample.type = type
        assert ingredient_sample.get_type() == type

    def test_get_name_of_ingredient_true(self, ingredient_sample):
        assert ingredient_sample.get_name() == 'Сыр'

    def test_get_price_of_ingredient_true(self, ingredient_sample):
        assert ingredient_sample.get_price() == 0.8