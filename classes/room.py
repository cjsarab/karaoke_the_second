class Room:
    def __init__(self, name, capacity, guests_in):
        self.name = name
        self.capacity = capacity
        self.guests_in = guests_in
        self.songs = []


    def add_song(self, song):
        self.songs.append(song)

    def add_guest(self, guest):
        if self.capacity > self.guests_in:
            self.guests_in += 1

