import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):

        self.room = Room("Room 1", 6, 0, 10)
        self.room_full = Room("Room 2", 6, 6, 10)

        self.song = Song("Black Sabbath", "Paranoid")

        self.guest_rich = Guest(100)
        self.guest_poor = Guest(5)
        
    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.name)

    def test_add_song_to_room(self):
        self.room.add_song(self.song)
        self.assertEqual([self.song], self.room.songs)

    def test_add_guest_to_room(self):
        self.room.add_guest(self.guest_rich)
        self.assertEqual(1, self.room.guests_in)

    def test_add_guest_room_full(self):
        self.room_full.add_guest(self.guest_rich)
        self.assertEqual(6, 6)

    def test_add_rich_guest(self):
        self.room.add_guest(self.guest_rich)
        self.assertEqual(90, self.guest_rich.cash)

    def test_add_poor_guest(self):
        self.room.add_guest(self.guest_poor)
        self.assertEqual(5, self.guest_poor.cash)
