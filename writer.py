# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import logging
import sys
from xdo import Xdo
import json

from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException

reload(sys)  
sys.setdefaultencoding('utf8')

logging.basicConfig()
logger = logging.getLogger("kalliope")
def sendkeys(*keys):
    for k in keys: xdo.send_keysequence_window(0, k.encode())

def type(text):
    xdo.enter_text_window(0, text.encode())
xdo = Xdo()

class Writer (NeuronModule):
    def __init__(self, **kwargs):
        super(Writer, self).__init__(**kwargs)

        message = {}
        for k in kwargs.keys():
            message[k] = kwargs[k]
        inp = json.dumps({'1': message })
        logger.debug("****inp = %s" % inp)
        logger.debug("Repeat: %s" % message)
        strM=inp[17:inp.find('", "')]
        y = strM.decode('unicode-escape')
        logger.debug("current line: %s" % y)
        type(y)
