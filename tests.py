import pytest
from conftest import TestBookFixtures
from main import BooksCollector


class TestBookCollector(TestBookFixtures):
     
     @pytest.mark.parametrize('name, genre',
                             [
                                 ['Сияние', 'Ужасы'],
                                 ['Оно', 'Ужасы'],
                                 ['Дюна', 'Фантастика'],
                                 ['Внутри убийцы', 'Детективы'],
                                 ['Манюня', 'Мультфильмы'],
                                 ['Дневник Бриджит Джонс', 'Комедии']
                             ]
                             )
     def test_set_book_genre(self, collector, name, genre):
        """Проверяет установку жанра книги."""
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre


     