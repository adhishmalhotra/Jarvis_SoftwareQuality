from plugin import plugin
from colorama import Fore
import string
import random


@plugin("hackerman")
def fake_hacker(jarvis, s):

    while True:

        rand = ' '.join([random.choice(string.ascii_letters) for x in range(random.randrange(30, 80))])
        jarvis.say(rand, Fore.RED)
