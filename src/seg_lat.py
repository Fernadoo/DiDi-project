longitude = [103.969021,104.017431,104.069272,104.122143,104.175702]
latitude = [30.770799,30.722704,30.684329,30.650073,30.625851,30.585663]
pointlist = [[]for i in range(6)]
print("region")
for i in range(6):
    # print('\"',end='')
    for j in range(5):
        temp = []
        temp.append(longitude[j])
        temp.append(latitude[i])
        pointlist[i].append(temp)
        # if j!= 4:
        #     string = "["+ str(temp[0]) + "," + str(temp[1]) + "],"
        # else:
        #     string = "["+ str(temp[0]) + "," + str(temp[1]) + "]"
    #     print(string,end='')
    # print('\"')

for i in range(5):

    for j in range(4):
        print('\"',end='')
        str0 = "["+ str(pointlist[i][j][0]+0.000003) + "," + str(pointlist[i][j][1]-0.000003) + "]"
        str1 = "["+ str(pointlist[i][j+1][0]-0.000003) + "," + str(pointlist[i][j+1][1]-0.00003) + "]"
        str2 = "["+ str(pointlist[i+1][j+1][0]-0.000003) + "," + str(pointlist[i+1][j+1][1]+0.00003) + "]"
        str3 = "["+ str(pointlist[i+1][j][0]+0.000003) + "," + str(pointlist[i+1][j][1]+0.00003) + "]"
        print(str0,str1,str2,str3,sep=',',end='')
        print('\"')
