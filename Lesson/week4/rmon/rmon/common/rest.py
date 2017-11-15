"""
    rmon.common.rest
"""

class RestException(Exception):
    """
    """

    def __init__(self, code, message):

        """init
        
        Args:
            code (int) : http
            message (str):

        """
        self.code = code
        self.message = message 
        super(RestException, self).__init__()


