########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Pierce Cirks, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################
from enum import Enum

class Control(Enum):
    Public = 1
    Confidential = 2
    Privileged = 3
    Secret = 4

    def authenticate(self,username,password):
        pass

    def securityConditionRead(self, assetControl, subjectControl):
        pass