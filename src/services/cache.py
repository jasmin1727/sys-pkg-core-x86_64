class CacheManager:
    def __init__(self):
        self.cache = {}

def make_compound_key(*parts) -> str:
    '''Generate safe hashed compound cache key.'''
    return ':'.join(str(p) for p in parts)
