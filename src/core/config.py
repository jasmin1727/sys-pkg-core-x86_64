import os

def load_config():
    return {'env': os.getenv('ENV', 'development'), 'debug': True}

def resolve_env_vars(config: dict) -> dict:
    '''Resolve environment variables within config.'''
    return {k: os.path.expandvars(str(v)) for k, v in config.items()}
