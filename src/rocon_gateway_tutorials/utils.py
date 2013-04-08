#!/usr/bin/env python
#       
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_multimaster/master/rocon_gateway_tutorials/LICENSE 
#

##############################################################################
# Imports
##############################################################################

import rospy
from gateway_msgs.msg import *

##############################################################################
# Functions
##############################################################################

def createTutorialDictionaries(regex):
    '''
      Creates and returns names and nodes dictionaries for the xxx_tutorials.
      
      @param regex : true if it should test regex patterns instead of strings
      @type bool
      @return names, nodes : two dictionaries with connection type keys and names, node string values
    '''
    names = {}
    nodes = {}
    if regex:
        names = { ConnectionType.PUBLISHER : '.*ter',
                  ConnectionType.SUBSCRIBER : '.*ter',
                  ConnectionType.SERVICE : '/add_two_.*',
                  ConnectionType.ACTION_CLIENT : '/fibonacci/cli.*',
                  ConnectionType.ACTION_SERVER : '/fibonacci/ser.*'
                }
        nodes = { ConnectionType.PUBLISHER : '/t.*er',
                  ConnectionType.SUBSCRIBER : '',
                  ConnectionType.SERVICE : '',
                  ConnectionType.ACTION_CLIENT : '',
                  ConnectionType.ACTION_SERVER : ''
                }
    else:
        names = { ConnectionType.PUBLISHER : '/chatter',
                  ConnectionType.SUBSCRIBER : '/chatter',
                  ConnectionType.SERVICE : '/add_two_ints',
                  ConnectionType.ACTION_CLIENT : '/fibonacci/client',
                  ConnectionType.ACTION_SERVER : '/fibonacci/server'
                }
        nodes = { ConnectionType.PUBLISHER : '',
                  ConnectionType.SUBSCRIBER : '',
                  ConnectionType.SERVICE : '',
                  ConnectionType.ACTION_CLIENT : '',
                  ConnectionType.ACTION_SERVER : ''
                 }
    return names, nodes
