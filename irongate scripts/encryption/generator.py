# -*- coding: utf-8 -*-
import os
import base64


class Generator:

    def getNewSalt(self):
        return os.urandom(32)  # return 32 bytes

    def getNewIv(self):
        return os.urandom(16)  # return 16 bytes

    def stringToBinary(self, string):
        return base64.urlsafe_b64decode(string)

    def binaryToString(self, binary):
        return base64.urlsafe_b64encode(binary).decode('utf-8')


