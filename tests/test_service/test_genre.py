import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture()
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        director = self.genre_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.genre_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": "Ivan",
        }
        director = self.genre_service.create(director_d)

        assert director.id is not None

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "Ivan",
            "age": 39,
        }
        self.genre_service.update(director_d)

    def test_delete(self):
        self.genre_service.delete(1)
