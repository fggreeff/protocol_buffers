import complex_message.sample_complex_message_pb2 as complex_msg_pb2

complex_message = complex_msg_pb2.ComplexMessage()


# *********** PART1 - WRONG way of implementing ***********
dummy_message = complex_msg_pb2.DummyMessage()
dummy_message.id = 111
dummy_message.name = 'Test1'
print(dummy_message)

# assignment here doesn't work as you'd expect. The way to set this is shown in part two
# complex-message.one_dummy = dummy_message
print(complex_message)

# *********** PART2 - CORRECT implementation ***********
complex_message.one_dummy.id = 222
complex_message.one_dummy.name = 'Test2'
print(complex_message)


# *********** PART3 - Setting the repeated scalar value (array) ***********
complex_message_collection = complex_message.multiple_dummy.add()  # The .add() returns a dummy_message type
complex_message_collection.id = 333
complex_message_collection.name = 'Test3 - First in array'
print(complex_message_collection)

# *********** PART4 - Setting the repeated scalar value (array) ***********
complex_message.multiple_dummy.add(id=444, name='Test4')
print(complex_message)  # prints all 3 entries in array


# *********** PART5 - Setting the repeated scalar value (array). CAREFUL USING THIS ONE ***********
another_dummy_message = complex_msg_pb2.DummyMessage()
another_dummy_message.id = 555
another_dummy_message.name = 'Test5'
complex_message.multiple_dummy.extend([another_dummy_message]) # IMPORTANT BUG CREEP: a copy is made of the object, not a refrence to the original obj
print(complex_message)
