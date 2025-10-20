import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_length_more_40(self):
        collector = BooksCollector()
        collector.add_new_book('a' * 41)
        assert 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' not in collector.books_genre


    def test_set_book_genere(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.books_genre['Оно'] == 'Ужасы'

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.books_genre['Оно'] = 'Ужасы'
        genre = collector.get_book_genre('Оно')
        assert genre == 'Ужасы'    

    def test_get_books_with_specific(self):
        collector = BooksCollector()
        collector.add_new_book('Девы')
        collector.set_book_genre('Девы', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Девы']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        assert collector.get_books_genre() == {'Ревизор': 'Комедии'}

    def get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Шрэк')
        collector.set_book_genre('Шрэк', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Шрэк' in collector.get_books_for_children()
        assert 'оно' not in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.add_book_in_favorites('Марсианин')
        assert 'Марсианин' in collector.get_list_of_favorites_books()

    def test_add_duplicate_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.add_book_in_favorites('Марсианин')
        collector.add_book_in_favorites('Марсианин')
        assert collector.get_list_of_favorites_books().count('Марсианин') == 1

    def test_delete_book_from_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.add_book_in_favorites('Марсианин')
        collector.delete_book_from_favorites('Марсианин')
        assert 'Гамлет' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('books, genre', [('Марсианин', 'Фантастика'),
                                               ('Оно', 'Ужасы'),
                                               ('Девы', 'Детективы'),
                                               ('Шрэк', 'Мультфильмы'),
                                               ('Ревизор','Комедии')])
    def test_get_list_of_favorites_books(self, books):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.add_book_in_favorites(books)
        favorites = collector.get_list_of_favorites_books()
        assert books in favorites
ды