import message.sample_message_pb2 as sample_msg_pb2

simple_message = sample_msg_pb2.SimpleMessage()

# Because of reflection, this won't show up in intellisense.
# Any errors will show up in runtime (not on compile)
simple_message.id = 123
simple_message.is_simple = True  # Setting this to False will take the default assigment and therefore not print it out.
simple_message.name = "This is a simple message"

# Repeated scalar container (acts the same way as a list)
sample_list = simple_message.sample_list
# sample_list = [1,2]
sample_list.append(3)

# print output
print(sample_list)
print(simple_message)

# write message to file
with open("simple.bin", "wb") as f:  # protocol buffer is binary, therefore we use wb (write binary)
    bytesAsString = simple_message.SerializeToString()
    f.write(bytesAsString)

# read message from file
with open("simple.bin", "rb") as f:  # we use rb (read binary)
    my_simple_message = sample_msg_pb2.SimpleMessage().FromString(f.read())
    print(my_simple_message)
