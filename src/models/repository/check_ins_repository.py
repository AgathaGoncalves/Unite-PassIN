# pylint: disable-all
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from src.erros.erros_types.http_conflict import HttpConflictserror


class CheckInRepository:
    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(attendeeId=attendee_id)
                )

                database.session.add(check_in)
                database.session.commit()
                return attendee_id

            except IntegrityError:
                raise HttpConflictserror('Esse CheckIn já foi realizado 🙂🥱')

            except Exception as exception:
                database.session.rollback()
                raise exception('Houve um erro inesperado😵🤯')
