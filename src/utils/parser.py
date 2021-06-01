import json

def parse_input(data: str) -> dict:
    return json.loads(data) if data else {}

def validate_event_schema(event: dict) -> bool:
    '''Check event against defined schema.'''
    return 'id' in event and 'type' in event

def parse_stream_safe(stream):
    '''Parse stream with graceful EOF handling.'''
    try:
        return stream.read()
    except EOFError:
        return None
