import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director

from setup_db import db


@pytest.fixture()
def director():
    director_dao = DirectorDAO(db.session)

    taylor = Director(id=1, name='Тейлор Шеридан')
    quentin = Director(id=2, name='Квентин Тарантино')
    vladimir = Director(id=3, name='Владимир Вайншток')

    director_dao.get_one = MagicMock(return_value=taylor)
    director_dao.get_all = MagicMock(return_value=[taylor, quentin, vladimir])
    director_dao.create = MagicMock(return_value=Director(id=1))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao
