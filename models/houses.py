from sqlmodel import Field, SQLModel 

class House_A:
    def __init__(self, room: Room, num_of_rooms: int,is_valid=True):
        self.room = room
        self.num_of_rooms = 10

class House_B:
    def __init__(self, room: Room, num_of_rooms: int, is_valid=True):
        self.room = room
        self.num_of_rooms = 10


class Room:
    def __init__(self, max_soldiers_in_room: int,is_valid=True):
        self.max_soldiers_in_room = 8




    