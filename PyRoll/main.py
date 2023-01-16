import os
import csv
results={}
differ={}
bank = os.path.join("..", "PyRoll", "Resources", "election_data.csv")
with open(bank, encoding="utf-8") as file:
    reader=csv.DictReader(file, delimiter=",")
    print("")
    print('Election Results')
    print("---------------------------------------")
    p=0
    max=0
    min=0
    sum=0
    results[0]=0
    for row in reader:
         results[p+1]=row["Profit/Losses"]
         delta=float(results[p+1])-float(results[p])
         if delta > max:
          max=delta
          pmax=row["Date"]
         if delta < min:
          min=delta
          pmin=row["Date"] 
         sum+=int(row["Profit/Losses"])
         p+=1
    dif=round((float(results[p])-float(results[1]))/(p-1),ndigits=2)
    print("")   
    print(f'Total Voters: {reader.line_num-1}')
    print("---------------------------------------")
    print(f'Total Amount: ${sum}')
    print(f'Average Change: ${dif}')
    print(f'Greatest Increase Change: {pmax} (${max})')
    print(f'Greatest Decrease Change: {pmin} (${min})')
        

fu=open('analysis\pybank.txt', 'w')
fu.write('Financial Analysis'+ '\n')
fu.write("---------------------------------------"+ '\n')
fu.write(f'Total Months: {reader.line_num-1}'+ '\n')
fu.write(f'Total Amount: ${sum}'+ '\n')
fu.write(f'Average Change: ${dif}'+ '\n')
fu.write(f'Greatest Increase Change: {pmax} (${max})'+ '\n')
fu.write(f'Greatest Decrease Change: {pmin} (${min})'+ '\n')
fu.close()
