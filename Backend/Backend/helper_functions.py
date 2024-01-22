import uuid


def parse_uuid(string):
    try:
        return uuid.UUID(string)
    except ValueError:
        raise ValueError("The UUID is not valid")
