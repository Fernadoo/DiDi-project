import sqlite3

file = open("gps_20161101")

conn = sqlite3.connect('order.db')
print "Opened database successfully";

cursor = conn.cursor()

# ---------------------data table view-----------------------

cursor = cursor.execute("SELECT customerID, starttime, endtime, start_longitude, start_latitude, end_longitude, end_latitude from cheeseburg")
for row in cursor:
   print "customerID = ", row[0]
   print "starttime = ", row[1]
   print "endtime = ", row[2]
   print "start_longitude = ", row[3]
   print "start_latitude = ", row[4]
   print "end_longitude = ", row[5]
   print "end_latitude = ", row[6],"\n"

print "Operation done successfully";

#----------------------data table delete---------------------

# conn.execute('drop table gps')
# print "Delete table successfully";

#----------------------create and insert-----------------------

# cursor.execute('''CREATE TABLE cheeseburg
#        (driverID    TEXT NOT NULL,
#        customerID    TEXT NOT NULL,
#        t    TEXT NOT NULL,
#        longtitude    TEXT NOT NULL,
#        latitude    TEXT NOT NULL,);''')
# print "Table created successfully";
#
# while 1:
#     line = file.readline()
#     # print line;
#     if not line:
#         break
#     tmp = line.split(',')
#     params = (tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])
#     cursor.execute("INSERT INTO cheeseburg VALUES (?,?,?,?,?)",params);
#
#
# conn.commit()
# print "Records created successfully";
# conn.close()
