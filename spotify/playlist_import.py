import sys
import spotipy

import spotipy.util as util

scope = 'playlist-modify-private'
task = ''
playlist = ''
usr = ''
sp = spotipy.Spotify()

# Command Structure python spt task playlist ...
if len(sys.argv) > 2:
    task = argv[1]
    playlist = argv[2]
else:
    print 'Incorrect Usage, See Documetnation'

def auth:
    usr = raw_imput("Please enter your username for Spotify") 
    return util.prompt_for_user_token(usr, scope)

def getSong(q):
    results = sp.search(q)
    #Need to print this out to see the format it returns



def createPlaylist():
    

    

