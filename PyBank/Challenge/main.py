import os
import csv
budget_data1 = os.path.join("Resources","budget_data1.csv")

#Creating lists and assigning variables
dates= 0
SumPL= 0
Difference=0
Priorp= 0
Profits_losses = []
G_I= 0
G_D= 0
Average_Change= 0

#Opening csv file
with open(budget_data1, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header= next(csvreader)

  #Creating ForLoop to count each row
    for row in csvreader:
        dates = dates +1 
        SumPL= SumPL + int(row[1])
        Difference= int(row[1])- Priorp
        
#Setting conditionals for greatest increase and greatest decrease in profit. Make sure that the difference calculation doesnt count first value.
        if dates > 1:
            
          if Difference < G_I:
                Date_GI = row[0]
                G_I= Difference
          if Difference < G_D:
                G_D = Difference   
                Date_GD= row[0]
Priorp= int(row[1])

# Defining the Average Change w forloop and .append function  
Profits_losses.append(Difference)
Profits_losses = Profits_losses[1:len(Profits_losses)]
 
# Handling division error by 0 
try:
    Average_Change= ((sum(Profits_losses))/(len(Profits_losses)))

except ZeroDivisionError:
   
    Average_Change = 0
       
#Printing to terminal
print ("-------------------------------")
print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months:", str(dates))
print ("Total: ", "$", str(SumPL))
print ("Average Change: ", "$", int(Average_Change) )
print ("Greatest Increase in Profits: ",str(Date_GI), "$", str(G_I) )
print ("Greatest Decrease in Profits:  ",str(Date_GD), "$", str(G_D))

#Printing to outputfile
output= os.path.join ("Analysis","Pybank.txt")
counter= "Analysis\n{str(count)}"
with open (output, "w") as outbudget_data:
    outbudget_data.write(counter)
print ("-------------------------------")
print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months:", str(dates))
print ("Total: ", "$", str(SumPL))
print ("Average Change: ", "$", int(Average_Change) )
print ("Greatest Increase in Profits: ",str(Date_GI), "$", str(G_I) )
print ("Greatest Decrease in Profits:  ",str(Date_GD), "$", str(G_D))