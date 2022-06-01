from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director():
    director_dao = DirectorDAO(None)

    taylor = Director(id=1, name='Тейлор Шеридан')
    quentin = Director(id=2, name='Квентин Тарантино')
    vladimir = Director(id=3, name='Владимир Вайншток')

    director_dao.get_one = MagicMock(return_value=taylor)
    director_dao.get_all = MagicMock(return_value=[taylor, quentin, vladimir])
    director_dao.create = MagicMock(return_value=Director(id=1))
    director_dao.partially_update = MagicMock(eturn_value=Director(id=2))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director):
        self.director_service = DirectorService(dao=director)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "id": 2,
            "name": "Lily",
        }
        director = self.director_service.create(director_d)

        assert director.id is not None

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "Ivan",
            "age": 39,
        }
        self.director_service.update(director_d)

    def test_delete(self):
        self.director_service.delete(1)
