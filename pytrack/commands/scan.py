"""
The API scan command.
"""

from __future__ import with_statement
import os
import glob

import pytrack.song

audio_encodings = ['.mp3', '.ogg', '.wav']


def scan():
    analysis_file = 'analysis.pyta'
    songs = []

    # get all the songs in the directory
    for infile in os.listdir(os.getcwd()):
        if not os.path.splitext(infile)[1] in audio_encodings: continue
        songs.append(pytrack.song.Song(infile))

    # write scan data to file
    with open(os.path.join(os.getcwd(), analysis_file), 'w') as fd:
        for song in songs:
            fd.writelines(song.format_str())
            fd.write('\n\n')

    return songs
