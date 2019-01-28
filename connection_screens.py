# -*- coding: utf-8 -*-
"""
Connection screen

Texts written here will be shown to user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets. UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = """
|b==============================================================|n
 WINTERMUTE
 
 With offputting frankness he told me -all in game- about a group 
 he had co-founded in 2002, back in his “anarchist days” - 
 an internet-based collective centered on user anonymity, security through obscurity -- 
 and cannabis growth and  distribution....

 If you have an existing account, connect to it by typing:
      |wconnect <username> <password>|n
 If you need to create an account, type (without the <>'s):
      |wcreate <username> <password>|n

 If you have spaces in your username, enclose it in quotes.
 Enter |whelp|n for more info. |wlook|n will re-show this screen.
|b==============================================================|n""" \
    .format(settings.SERVERNAME, utils.get_evennia_version())
