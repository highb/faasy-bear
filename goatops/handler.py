import os
import random

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'goatdata')
    goatdata = list(open(path, "r"))

    return random.choice(goatdata)
