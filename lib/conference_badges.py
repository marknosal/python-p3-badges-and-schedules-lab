def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_list = [badge_maker(name) for name in names]
    return badge_list

    # badge_list = list([])
    # for thing in names:
    #     badge_list.append(badge_maker(thing))


def assign_rooms(names):
    # new_list = []
    # for index, name in enumerate(names):
    #     new_list.append(f"Hello, {names[index]}! You'll be assigned to room {index + 1}!")
    # new_list = [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name in enumerate(names)]

    # for blob in range(len(names)):
    #     new_list.append(f"Hello, {names[blob]}! You'll be assigned to room {blob + 1}!")
    # new_list = [f"Hello, {names[name]}! You'll be assigned to room {name + 1}!" for name in range(len(names))]

    # index = 0
    # while index < len(names):
    #     new_list.append(f"Hello, {names[index]}! You'll be assigned to room {index + 1}!")
    #     index += 1
    # print(new_list)
    # new_list = [f"Hello, {names[name]}! You'll be assigned to room {name + 1}!" for name in range(len(names))]

    # index = 0
    # for thing in names:
    #     new_list.append(f"Hello, {names[index]}! You'll be assigned to room {index + 1}!")
    #     index += 1
    new_list = [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name  in enumerate(names)]


    return new_list

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
    



# def assign_rooms(names):
#     new_list = [f"Hello, {names[index]}! You'll be assigned to room {index + 1}!" for index in names]
#     return new_list