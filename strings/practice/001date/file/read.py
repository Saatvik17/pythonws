stream = open('./trial.txt' , 'rt')

print(" is this readable?\n " + str(stream.readable()))

print("Read everything related to trial:\n" + str(stream.readlines()) )