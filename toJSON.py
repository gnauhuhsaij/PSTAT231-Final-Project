# Opening JSON file and loading the data
# into the variable data
f = open('../data/RC_2021-10.json')
# returns JSON object as 
# a dictionary
data = f.readlines()
iter = 0
string = "{ \"foo\":["
for i in data:
    string+=i
    iter += 1
    if iter%100000==0:
        print("Reading Process:", iter/len(data))


print(string[1892300:1892600])
print(string[-20:])
string = string.replace("}", "},")
string = string.replace("},,", "},")
string += "]}"
string = string.replace("},]","}]")
string = string.replace("\'", "")
string = string.replace("},},},},}", "}}}}}")
string = string.replace("},},},}", "}}}}")
string = string.replace("},},}", "}}}")
string = string.replace("},}", "}}")
print("String Replacement Finished")

newFile = open('../data/String_data.json', 'w')
newFile.write(string)
newFile.close()