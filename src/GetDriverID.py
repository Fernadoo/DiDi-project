import sqlite3
import pandas as pd

conn = sqlite3.connect('gps.db')
print "Opened database successfully";

cursor = conn.cursor()

# ---------------------GetDriver-----------------------

# record the driver's ID
driverID = []
# longitute and latitude, record the locations
location_pack = []
# record the last driverID/customerID
lastd = ""
lastc = ""
# stick the locations together
path = ""

cursor = cursor.execute("SELECT driverID, customerID, t, longtitude, latitude from cheese")

# count the number of the drivers
i = 0
# count the delay
j = 0

for row in cursor:
    # # --------------count drivers-------------
    # if row[0] != lastd:
    #     i += 1
    # lastd = row[0]
    if i == 3000:
        break
    if row[0] != lastd:
        i += 1
        lastd = row[0]
        if i < 2250:
            continue
        if i != 1:
            # remove the last comma
            path = path[:len(path)-1]
            # path += "\""
            location_pack.append(path)
        # path = "\""
        path = ""
        driverID.append(row[0])
    else:
        if i < 2250:
            continue
        if row[1] == lastc:
            j += 1
            if j < 3:
                pass
            else:
                path = path + "[" + row[3] + "," + row[4][:len(row[4])-2] + "],"
                j = 0
        else:
            path = path + "[" + row[3] + "," + row[4][:len(row[4])-2] + "],"
        lastc = row[1]

driverID = driverID[1:]
location_pack = location_pack[1:]
# driverID.pop()
# print i;
# # print driverID;
# # print location_pack;
dataframe = pd.DataFrame({'driverID':driverID,'path':location_pack})
dataframe.to_csv("DriverPath2250-3000.csv",index=False,sep=',')
print "Operation done successfully";
