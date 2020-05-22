stream = open("./output.txt" , "wt")

print("is this writable?\n" + str(stream.writable()))

stream.writelines(["Welcome", " ","to"," ","the"," ","trial"])
stream.write("\n")

trial = ["Harvey" , "Specter"]

stream.writelines("\n" .join(trial))
stream.close()