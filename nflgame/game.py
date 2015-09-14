from collections import namedtuple
import os
import os.path as path
import gzip
import json
import socket
import sys
import urllib2

from nflgame import OrderedDict
import nflgame.player
import nflgame.sched
import nflgame.seq
import nflgame.statmap
