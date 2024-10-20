from sqlalchemy.exc import IntegrityError
from database.declarative_base import open_session
from models.models import BlacklistedEmail


class BlacklistedEmailService:

    @staticmethod
    def create_email_blacklisting(data):
        with open_session() as session:
            try:
                blacklisted_email = BlacklistedEmail(
                    email=data['email'],
                    app_uuid=data['appUuid'],
                    blocked_reason=data['blockedReason'],
                    request_ip=data['requestIp']
                )
                session.add(blacklisted_email)
                session.commit()
            except IntegrityError:
                return '', 400
        return '', 200

    @staticmethod
    def is_blacklisted(email):
        with open_session() as session:
            result = session.query(BlacklistedEmail).filter(BlacklistedEmail.email == email).first()

        if not result:
            return 'false', 200
        else:
            return 'true', 200
