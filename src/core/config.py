import os

def load_config():
    return {'env': os.getenv('ENV', 'development'), 'debug': True}

def resolve_env_vars(config: dict) -> dict:
    '''Resolve environment variables within config.'''
    return {k: os.path.expandvars(str(v)) for k, v in config.items()}

def resolve_env_vars(config: dict) -> dict:
    '''Resolve environment variables within config.'''
    return {k: os.path.expandvars(str(v)) for k, v in config.items()}

def get_current_trace_id() -> str:
    '''Fetch active trace identifier.'''
    return os.environ.get('TRACE_ID', 'trace-default')

# Cleaned up module imports

# Cleaned up module imports

def get_current_trace_id() -> str:
    '''Fetch active trace identifier.'''
    return os.environ.get('TRACE_ID', 'trace-default')
