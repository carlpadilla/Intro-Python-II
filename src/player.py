# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    '''
    defining the initial class of Player with player name and room where they start
    '''

    def __init__(self, name, room):
        self.name = name
        self.current_room = room
    # How the player moves

    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(f"You are currently in: \n{self.current_room}")
        else:
            print("You can't go in that direction.")
