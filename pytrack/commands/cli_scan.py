"""
The CLI wrapper function for the scan command.
"""

import os

import pytrack.commands.scan


def cli_scan(args):
    songs = pytrack.commands.scan.scan()

    for song in songs:
        print '\n\n'
        string = song.format_str()
        for line in string:
            print line.rstrip()

    return
