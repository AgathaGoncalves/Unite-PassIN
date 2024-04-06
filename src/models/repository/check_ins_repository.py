# pylint: disable-all
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError,NoResultFound

class CheckInRepository:
    def insert_check_in(self, atendee_id) -> str :
        with db_connection_handler as database:
            try:
                check_in = CheckIns(
                    CheckIns(attendee_id=atendee_id)
                )
                database.session.add(check_in)
                database.session.commit()
                return atendee_id
            
            except IntegrityError:
                raise Exception('Esse CheckIn já foi realizado 🙂🥱')
            
            except Exception as exception:
                database.session.rollback()
                raise exception('Houve um erro inesperado😵🤯')