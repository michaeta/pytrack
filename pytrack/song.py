"""
This class is a stripped down version of pyechonest's track obj. It just
holds the relavent data.
"""

import os.path

from pyechonest import track
from pyechonest import config

# we need a key to use this API
config.ECHO_NEST_API_KEY = "R83ZIIKHFOH8ISPW8"


class Song():
    # key data from pyechonest is represented as values from 0 - 11
    _major_key_map = ["1A", "2A", "3A", "4A", "5A", "6A", "7A",
                     "8A", "9A", "10A", "11A", "12A"]
    _minor_key_map = ["1B", "2B", "3B", "4B", "5B", "6B", "7B",
                     "8B", "9B", "10B", "11B", "12B"]
    num_cue_points = 3

    """
    Initializes all attributes to None.

    path: optional path to song to populate data
    """
    def __init__(self, path = None):
        self.title = "unknown"
        self.artist = "unknown"
        self.album = "unknown"
        self.duration = None
        self.bitrate = None
        self.key = None
        self.key_conf = None
        self.mode = None
        self.mode_conf = None
        self.time_sig = None
        self.time_sig_conf = None
        self.tempo = None
        self.tempo_conf = None
        self.loudness = None
        self.end_fade_in = None
        self.start_fade_out = None
        self.energy = None
        self.danceability = None
        self.speechiness = None
        self.cue_points = []

        if path: self.populate(path)


    """
    Populates all attributes with relavent data from t obj. Some
    attributes might not get populated if the parameter inside t
    does not exist.

    path: path to song to populate data
    """
    def populate(self, path):
        if not isinstance(path, str):
            raise TypeError('path must be type string')
        if not os.path.isfile(path): raise ValueError('file does not exist')

        t = track.track_from_filename(path)
        # sometimes tracks don't have data filled in
        try:
            self.title = t.title
            self.artist = t.artist
            self.album = t.release
        except AttributeError: pass

        self.duration = t.duration
        self.bitrate = t.bitrate
        self.key = t.key
        self.key_conf = t.key_confidence
        self.mode = t.mode
        self.mode_conf = t.mode_confidence
        self.time_sig = t.time_signature
        self.time_sig_conf = t.time_signature_confidence
        self.tempo = t.tempo
        self.tempo_conf = t.tempo_confidence
        self.loudness = t.loudness
        self.end_fade_in = t.end_of_fade_in
        self.start_fade_out = t.start_of_fade_out
        self.energy = t.energy
        self.danceability = t.danceability
        self.speechiness = t.speechiness

        # try to get the last sections for cue points
        try:
            for i in range(self.num_cue_points):
                self.cue_points.append(t.sections.pop()['start'])
        # there weren't enough, use what we have
        except IndexError: pass


    """
    Formats all object attributes into a pretty list of strings.

    return: List of strings for writing to file
    """
    def format_str(self):
        fmt_lst = []

        fmt_lst.append("Title        : " + self.title + "\n")
        fmt_lst.append("Artist       : " + self.artist + "\n")
        fmt_lst.append("Album        : " + self.album + "\n")
        fmt_lst.append("Duration     : " + format(self.duration, '.2f') +
                       " sec\n")
        fmt_lst.append("Bitrate      : " + str(self.bitrate) + " kbps\n")
        # key is major
        if self.mode == 0:
            fmt_lst.append("Key          : " + self._major_key_map[self.key] +
                           " with " + format(self.key_conf, '.2%') +
                           " confidence\n")
        # key is minor
        else:
            fmt_lst.append("Key          : " + self._minor_key_map[self.key] +
                           " with " + format(self.key_conf, '.2%') +
                           " confidence\n")
        fmt_lst.append("Time Sig.    : " + str(self.time_sig) + " with " +
                       format(self.time_sig_conf, '.2%') + " confidence\n")
        fmt_lst.append("Tempo        : " + format(self.tempo, '.2f') +
                       " with " + format(self.tempo_conf, '.2%') +
                       " confidence\n")
        fmt_lst.append("Loudness     : " + format(self.loudness, '.2f') +
                       " Db\n")
        fmt_lst.append("Fade In      : " + format(self.end_fade_in, '.2f') +
                       " sec\n")
        fmt_lst.append("Fade Out     : " + format(self.start_fade_out, '.2f') +
                       " sec\n")
        fmt_lst.append("Energy       : " + format(self.energy, '.2%') + "\n")
        fmt_lst.append("Danceability : " + format(self.danceability, '.2%') +
                       "\n")
        fmt_lst.append("Speechiness  : " + format(self.speechiness, '.2%') +
                       "\n")
        temp = ""
        for point in self.cue_points:
            temp += format(point, '.2f') + " sec, "
        fmt_lst.append("Cue Points   : " + temp[:(len(temp)-2)] + "\n")

        return fmt_lst