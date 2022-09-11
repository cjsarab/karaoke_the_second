class Room:
    def __init__(self, name, capacity, guests_in, fee):
        self.name = name
        self.capacity = capacity
        self.guests_in = guests_in
        self.fee = fee
        self.songs = []


    def add_song(self, song):
        self.songs.append(song)

    def add_guest(self, guest):
        if self.capacity > self.guests_in and self.fee <= guest.cash:
            self.guests_in += 1
            guest.cash -= self.fee

