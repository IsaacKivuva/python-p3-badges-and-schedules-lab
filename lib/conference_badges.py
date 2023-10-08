def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badge = []
    for name in names:
        badge.append(f"Hello, my name is {name}.")
    
    return badge

def assign_rooms(names):
    rooms = []
    for x, name in enumerate(names, start= 1):
        rooms.append(f"Hello, {name}! You'll be assigned to room {x}!")
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print (badge)

    rooms = assign_rooms(names)
    for room in rooms:
        print(room)

