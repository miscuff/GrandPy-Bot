class ZeroResultsException(Exception):
    """Raised when the request returns zero values"""
    pass


class NoResponseException(Exception):
    """Raised when there is no response for the api"""
    pass
