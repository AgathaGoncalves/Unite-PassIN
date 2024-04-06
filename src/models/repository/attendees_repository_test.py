# pylint: disable-all
import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason= "New register in database")
def test_insert_attendee():
    event_id='meu-primeir-uuidiiii'
    attendees_info = {
        "uuid": "My first attendee",
        "name": "Name test",
        "email": "test@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print('Teste de resposta do primeiro convidado', response)


@pytest.mark.skip(reason= "Dont have neccessity")
def test_get_attendee_badge_by_id():
    attendee_id = "My first attendeeeeeeeeeeeeeee"
    attendees_repository = AttendeesRepository()
    atendee = attendees_repository.get_attendee_badge_by_id(attendee_id)
    print(atendee)

