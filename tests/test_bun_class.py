import pytest
from practicum.bun import Bun



class TestBun:

    @pytest.fixture
    def bun_sample(self):
        bun = Bun(name='Рисовая', price=0.5)
        return bun

    def test_name_of_bun_true(self, bun_sample):
        assert bun_sample.name == 'Рисовая'

    def test_price_of_bun_true(self, bun_sample):
        assert bun_sample.price == 0.5

    def test_get_name_of_bun_true(self, bun_sample):
        assert bun_sample.get_name() == 'Рисовая'

    def test_get_price_of_bun_true(self, bun_sample):
        assert bun_sample.get_price() == 0.5