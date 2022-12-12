import json
import csv
 
 
f = open('../data/String_data.json')
# returns JSON object as 
# a dictionary
data = f.readlines()
iter = 0
string = ""
for i in data[0:-1]:
    string+=i
    iter += 1
    if iter%100000==0:
        print("Reading Process:", iter/len(data))
string = string[0:-2]
string += "]}"

data = json.loads(string)
["score","ups","created_utc","author_flair_css_class","subreddit","subreddit_id","stickied","link_id","body","controversiality","distinguished","retrieved_on","gilded","id","edited","parent_id","author_flair_text","author"]
print("String loading Finished")
# now we will open a file for writing
data_file = open('../data/RC_2021-10.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0
columns = data['foo'][0].keys()
for emp in data['foo']:
    if count == 0:
 
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        
    count += 1
    if count % 100000 == 0:
        print("Writing Process:", count/len(data))
    # Writing data of CSV file
    csv_writer.writerow([emp.get(col, None) for col in columns])
data_file.close()
