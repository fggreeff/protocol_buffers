import enums.sample_enum_pb2 as enum_pb2

day = enum_pb2.EnumMessage()
day.id = 1
day.day_of_the_week = enum_pb2.MONDAY

print(day)

# write to file
with open('enums.bin', 'wb') as f:
    f.write(day.SerializeToString())
    print('wrote to file')

# read from file
with open('enums.bin', 'rb') as f:
    print('read from file')
    my_file_day = enum_pb2.EnumMessage().FromString(f.read())
    print(my_file_day)