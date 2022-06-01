from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from setup_db import db


@pytest.fixture()
def genre():
    genre_dao = GenreDAO(db.session)

    comedy = Genre(id=1, name='comedy')
    drama = Genre(id=2, name='drama')
    horror = Genre(id=3, name='horror')

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, drama, horror])
    genre_dao.create = MagicMock(return_value=Genre(id=1))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao
