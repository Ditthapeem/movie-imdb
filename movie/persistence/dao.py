from abc import ABC
from re import S
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Dao(ABC):

    def __init__(self, session):
        super().__init__()
        self._session = session
        
    @property
    def session(self):
        return self._session