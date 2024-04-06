# pylint: disable-all
from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import IntegrityError,NoResultFound


class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                event = Events(
                    id=eventsInfo.get("uuid"),
                    title=eventsInfo.get("title"),
                    details=eventsInfo.get("details"),
                    slug=eventsInfo.get("slug"),
                    maximum_attendees=eventsInfo.get("maximum_attendees"),
                )
                database.session.add(event)
                database.session.commit()

                return eventsInfo
            
            except IntegrityError:
                raise Exception('Evento já cadastrado 🙂🥱')
            
            except Exception as exception:
                database.session.rollback()
                raise exception('Houve um erro inesperado😵🤯')
 
    def get_event_by_id(self, event_id: str) -> Events:

        with db_connection_handler as database:
            try:
               event = database.session.query(Events).filter(Events.id == event_id).one()

            except NoResultFound:
                raise Exception('Este evento não existe em nosso banco de dados 🤨🤔')
            
            except Exception as exception:
                database.session.rollback()
                raise exception('Houve um erro inesperado😵🤯')

        return event
    
    def count_event_attendees(self, event_id: str) -> Dict :
        with db_connection_handler as database:
            event_count = (
                database.session
                .query(Events)
                .join(Attendees, Events.id == Attendees.event_id)
                .filter(Attendees.event_id == event_id)
                .with_entities(
                    Events.maximum_attendees,
                    Attendees.id
                    )
                .all()
            )
            if not len(event_count):
                return {
                    "maximum_attendees": 0,
                    "attendees_amount": 0
                }
            
            return {
                "maximum_attendees": event_count[0].maximum_attendees,
                "attendees_amount": len(event_count)
            }
