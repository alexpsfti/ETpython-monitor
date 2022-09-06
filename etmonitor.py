#!/usr/bin/env python3
from pyq3serverlist import Server, PyQ3SLError, PyQ3SLTimeoutError

server = Server('localhost', 27960)

try:
    status = server.get_status()
except (PyQ3SLError, PyQ3SLTimeoutError) as e:
    print(e)

maxplayers = status['sv_maxclients']
name = status['sv_hostname']
bots = status['omnibot_playing']
mapname = status['mapname']
players = len(status['players'])
humans = int(players) -int(bots)

line = f"{name} - There are {players}({humans} human(s), {bots} bots) of a max of {maxplayers} players on {mapname}"

print(line)
