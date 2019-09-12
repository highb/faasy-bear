import random from random

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    goatdata = list(open("goatdata", "r"))

    return random.choice(goatdata)
