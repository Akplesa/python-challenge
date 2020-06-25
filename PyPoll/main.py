import os
import csv

election_csv = os.path.join('Resources','election_data.csv')

#Create lists and set counts at 0
Namelist = ["Khan","Correy","Li","O'Tooley"]
CandidateNames = []
count = 0
totalV= 0
totalV1 = 0
totalV2 = 0
totalV3 = 0
#Open csv file: 
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
#Create ForLoop to count each row
    for line in csvreader:
        count = count + 1
      #Names of candidates:
        if line[2] not in CandidateNames:
            CandidateNames.append(line[2])

# Find rows for percent won per name
        if line[2] = Namelist[0]:
            totalV = totalV + 1
        PW = round((totalV0 / count), 3)
         if line[2] = Namelist[1]:
            totalV1 = totalV1 + 1
        PW1 = round((totalV1 / count), 3)
         if line[2] = Namelist[2]:
            totalV2 = totalV2 + 1
        PW2 = round((totalV2 / count), 3)
        
        if line[2] = NameList[3]:
            totalV3 = totalV3 + 1
        PW3 = round((totalV3 / count), 3)
        
# max votes?????

# print in terminal

print("Election Results")
print("------------------------------------------------")
print("Total Votes:" , str(count) )
print("------------------------------------------------")
print(str(Namelist[0]),str(PW), str(totalV))
print(str(Namelist[1]),str(PW1), str(totalV1))
print(str(Namelist[2]),str(PW2), str(totalV2))
print(str(Namelist[3]),str(PW3), str(totalV3))      
print("------------------------------------------------")                    
print("Winner:" )
print("------------------------------------------------")                 
  
#print to outputfile
output= os.path.join ("Analysis","Pypoll.txt")
counter= "Analysis\n{str(count)}"
with open (output, "w") as outelection_data:
    outelection_data.write(counter)
print("Election Results")
print("------------------------------------------------")
print("Total Votes:" , str(count) )
print("------------------------------------------------")
print(str(Namelist[0]),str(PW), str(totalV))
print(str(Namelist[1]),str(PW1), str(totalV1))
print(str(Namelist[2]),str(PW2), str(totalV2))
print(str(Namelist[3]),str(PW3), str(totalV3))      
print("------------------------------------------------")                    
print("Winner:" )
print("------------------------------------------------")  
