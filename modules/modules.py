from roll import roll
from flip import flip
from menu import menu
from weather import weather, jacket
from random import randint

def thanks(args=[]):
    return ('(y)')

def eatadick(args=[]):
    num = randint(1,3)
    if num is not 1:
        return "r00d"
    return ('fuck u Jess')

def doabarrelroll(args=[]):
    num = randint(1,2)
    if num is 1:
        return "WHEeeEEeeeeEeeEEeEEEeEE"
    else:
        return "fuck u Jerry"

def help_message(args=[]):
    result = "Commands:\n"
    for key,value in modules.items():
        result += "  !%s\n" %(key)
    return result


"""command : function"""
modules = {
    "roll": roll,
    "flip": flip,
    "help": help_message,
    "menu": menu,
    "fud": menu,
    "food": menu,
    "sustenance":menu,
    "thanks": thanks,
    "eatadick": eatadick,
    "weather": weather,
    "jacket": jacket,
    "barrelroll" : doabarrelroll,
    "doabarrelroll": doabarrelroll
    }


