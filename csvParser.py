# Import Module
import csv
import os
  
#change the current directory into folder with CSV files
os.chdir("csv_files")
#get list of file names in directory
fileList = os.listdir()
#for every file in directory...
for file in fileList:
    print(file) # print file name
    
    #open the file, indicate ',' as delimiter, and print each row of file
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            #column names
            if line_count == 0:
                for col in row:
                    print("\t", col)
            # if you want to print
            #else:
                #print(row)
            
            line_count += 1

        print("Processed ", line_count, " lines\n")



