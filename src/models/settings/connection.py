from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "():///()".format(
            "sqlite"
            "storage.db"
        )

        self.__engine = None
        self.__session = None

        def connect_to_db(self)-> None:
            self.__engine = create_engine(self.__connection_string)

        def get_engine(self):
            return self.__engine
        
    def __enter__(self):
        sessionmaker = sessionmaker()
        self.__session = sessionmaker(bind=self.__engine)
        return self 

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
        