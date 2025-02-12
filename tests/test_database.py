import pytest

from practicum.database import Database

class TestDataBase:
    @pytest.fixture
    def db_sample(self):
        db=Database()
        return db

    def test_bun_list_len(self, db_sample):
        assert len(db_sample.buns) == 3

    def test_ingredients_list_len(self, db_sample):
        assert len(db_sample.ingredients) == 6

    def test_available_buns_len(self, db_sample):
        assert len(db_sample.available_buns()) == 3

    def test_available_ingredients_len(self, db_sample):
        assert len(db_sample.available_ingredients()) == 6