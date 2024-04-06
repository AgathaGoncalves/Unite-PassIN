# pylint: disable-all
import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="new register on database")
def test_insert_event():
    event={
        "uuid": "meu-primeir-uuidiiii",
        "title": "meu-titulo-teste",
        "slug": "meu-slug-aq-kkkkkkkkkk2",
        "maximum_attendees": 50
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)

    print(response)

@pytest.mark.skip(reason="dont have necessity")
def test_get_event_by_id():
    event_id = 'meu-slug-aq-kkkk'
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',response)