import os
import csv
results={}
bank = os.path.join("..", "PyRoll", "Resources", "election_data.csv")
with open(bank, encoding="utf-8") as file:
    reader=csv.DictReader(file, delimiter=",")
    print("")
    print('Election Results')
    print("---------------------------------------")
    current=''
    for row in reader:
          if row["Candidate"] in results.keys():
            results[row["Candidate"]] +=1        
          if row["Candidate"] not in results.keys():
           current=row["Candidate"]
           results[current]=1
    max_voters=max(results.values())           
    print(f'Total Voters: {reader.line_num-1}')
    print("---------------------------------------")
    print('')
    for key, value in results.items():
     print(f'{key}: {round(float(value*100/(reader.line_num-1)), ndigits=3)}% ({value})')
     print('---------------------------------------')
    print('')
    inv_results={value: key for key, value in results.items()}
    winner=inv_results[max_voters]
    #print(winner)
    print(f'Winner: {inv_results[max_voters]}')
    print('---------------------------------------')
    
    fu=open('analysis\election.txt', 'w') 
    with open('analysis\election.txt', 'w') as file:
     fu.write('' '\n')
     fu.write('Election Results'+ '\n')
     fu.write('---------------------------------------'+ '\n')
     fu.write(f'Total Voters: {reader.line_num-1}'+ '\n')
     fu.write("---------------------------------------"+ '\n')
     fu.write(''+ '\n')
     for key, value in results.items():
      zu=reader.line_num-1
      vo=round(value*100/zu, ndigits=3)
      fu.write(f'{key} {vo}%')
      fu.write(f' ({value}) \n')
     #fu.write(f'{key} {round(float(value*100/(reader.line_num-1)), ndigits=3)}% ({value}) \n')
     fu.write("---------------------------------------"+ '\n')
     fu.write(''+ '\n')
     fu.write(f'Winner: {winner}'+ '\n')
    fu.close()
