"""Project Two starter for the student's text-based adventure game."""


def show_instructions():
    print ("Dragon Adventure Text Game")
    print ("Collect the Bow, Arrow, Sure-Fire Potion, and Fire Resistence Potion to slay the Dragon.")
    print ("Possible Commands: North, East, South, West, Collect Item, Use Item")
    print ("Good Luck!")
    pass


def show_status(current_room, inventory, rooms):
when input == show_status
    print(current_room)
    print(PC_Inventory)
    print(current_room 'item')
    pass


def main():
    """Run the main gameplay loop."""
 rooms = {
     "Grand_Room": {
         "Description": "This massive room has a large hole in the ceiling from where you were dropped. The room lacks any importent items, but has multiple exits.",
         "Exits": {"North": "North_1", "South": "South_1", "East": "East_1", "West", "West_1"}
     },
     "North_1": {
         "Description": "This room is well worn and without repair, but otherwise safe. There is a key sitting on a table in the room, both of which are made of Gold",
         "Exits": {"South": "Grand_Room", "East": "Brass_Room"},
         'item': ['Gold_Key']
     },
     "South_1": {
         "Description": "This room is empty, excluding a single Brass Key on the floor.",
         "Exits": {"North": "Grand_Room"},
         'item': ['Brass_Key']
     },
     "East_1": {
         "Description": "This room is an old armory, but the only weapon remaining is a old, rusty sword."
         "Exits": {"West": "Grand_Room", "North": "Brass_Room"},
         'item': ['Rusty_Sword']
     },
     "Brass_Room": {
         "Description": "This room was locked with a Brass Key, and the inside of this room is filled with Brass goods. On a table sits a potion with a arrow striking an apple on it."
         "Exits": {"South": "East_1", "West": "North_1"},
         'item': ['Potion_Sure_Fire']
     },
     "West_1": {
         "Description": "This room was an old apothicary, and still has one potion remaining, it has a flame with an X over it."
         "Exits": {"East": "Grand_Room", "South": "South_2", "West": "West_2"},
         'item': ['Potion_Resist_Fire']
     },
     "West_2": {
         "Description": "This room is almost compleatly ruined, with rocks strune everywere. To the north stands a massive iron door that you can hear the dragon behind. A few rocks seem useful in this room",
         "Exits": {"North": "Boss_Room", "South": "Silver_Room", "West": "West_3"},
         'item': ['Large_Rock']
     },
     "West_3": {
         "Description": "A bit of rubble from the room to the east fills the enteryway. you can see a large, but unstable chandler hanging, with a Key of Black Iron hanging from one its arms",
         "Exits": {"East": "West_2", "South": "Gold_Room"},
         'item': ['Boss_Key']
     },
     "Gold_Room": {
         "Description": "This room, gold head-to-toe, it is somewhat hard to look at. on a ornate couch sits a Arrow of Dragon's Bone.",
         "Exits": {"North": "West_3"},
         'item': ['Dragon_Bone_Arrow']
     },
     "South_2": {
         "Description": "This room is a ruined library. it has a broken bow sitting in the middle of the room, with its string still intact.",
         "Exits": {"North": "West_2", "West": "Silver_Room"},
         'item': ['Bow_String']
     },
     "Silver_Room": {
         "Description": "This room has many silver statues and a fireplace with a powerful looking bow hanging over it. it is in a display case, but it looks like a sword could break its lock."
         "Exits": {"North": "West_2", "East": "South_2"},
         'item': ['Bow']
     },
     "Boss_Room": {
         "Description": "This room, the clear sleeping place of the dragon, currently has a large, red dragon sleeping in the middle of it. however, there is a perfect place to land an arrow, but you dont want to miss."
         "Exits": {"North": "Room_Exit", "South": "West_2"},
     }
 }
current_room = "Grand_Room"
PC_Inventory = []
if not PC_Inventory:
    print("Got Nothing")

    # TODO: Call the instruction function at the appropriate time.

    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
