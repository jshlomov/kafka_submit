import app.repository.postgres_repository.person_repository as person_rep

def get_person_messages_by_email(email):
    return person_rep.get_person_by_email(email)