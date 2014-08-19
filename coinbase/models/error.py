# ----- Author ---------------------------------------------------------------

__author__ = 'Michael Montero <mike@resy.com>'

# ----- Public Classes --------------------------------------------------------

class CoinbaseError(Exception):

    def __init__(self, errorList):
        self.error = errorList
