lenght_room = int(input("Length = "))
width_room = int(input("Width = "))
side_ward = int(input("Side of the wardrobe = "))

room_area = (lenght_room * 100) * (width_room * 100)
bench = room_area / 10
ward_area = (side_ward * 100) * (side_ward * 100)
space = room_area - (ward_area + bench)
space_dancer = (40 + 7000)
dancers = space / space_dancer

print(round(dancers))