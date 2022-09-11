import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):

        self.song = Song("Black Sabbath", "War Pigs")

    def test_song_has_artist(self):
        self.assertEqual("Black Sabbath", self.song.artist)