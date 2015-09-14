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

_MAX_INT = sys.maxint

_jsonf = path.join(path.split(__file__)[0], 'gamecenter-json', '%s.json.gz')
_json_base_url = "http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json"

GameDiff = namedtuple('GameDiff', ['before', 'after', 'plays', 'players'])
"""
Represents the difference between two points in time of the same game
in terms of plays and player statistics.
"""

TeamStats = namedtuple('TeamStats',
                       ['first_downs', 'total_yds', 'passing_yds',
                        'rushing_yds', 'penalty_cnt', 'penalty_yds',
                        'turnovers', 'punt_cnt', 'punt_yds', 'punt_avg',
                        'pos_time'])
"""A collection of team statistics for an entire game."""
