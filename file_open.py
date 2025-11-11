# with open('mydata.txt', 'w') as md:
#     for num in range(10):
#         md.write(str(num))
#         md.write('\n')
# # continue on with other code

olympians=[("Johnalaber",31,"Cross country skiing"),
           ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]
outfile=open("reduced_olympics.csv",'w')
outfile.write('Name,age,sport')
outfile.write('\n')
for olympian in olympians:
    row_string='{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()    