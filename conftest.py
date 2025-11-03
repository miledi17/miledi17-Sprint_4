import pytest
from main import BooksCollector


class TestBookFixtures:

    @pytest.fixture
    def collector(self):
        return BooksCollector()


