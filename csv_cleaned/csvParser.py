# Import Module
import csv
import os
import pandas as pd

def saveCSV(dataFrame):
    os.chdir("../csv_cleaned")
    dataFrame.to_csv('Person.csv', index=False)

def clean_people(files):
    file = 'People.csv'
    df = pd.read_csv(file, delimiter=',')

    df_clean = df[['playerID', 'nameFirst', 'nameLast', 'birthYear','birthMonth','birthDay','birthCountry','birthState','birthCity', 'deathYear','deathMonth','deathDay','deathCountry','deathState','deathCity','weight','height']]

    saveCSV(df_clean)

def main():
    #change the current directory into folder with CSV files
    os.chdir("./csv_files")
    #get list of file names in directory
    fileList = os.listdir()

    print(os.listdir())

    clean_people(fileList)

        # with open(file) as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=',')
        #     line_count = 0
        #     for row in csv_reader:
        #         #column names
        #         if line_count == 0:
        #             for col in row:
        #                 print("\t", col)
        #         # if you want to print
        #         #else:
        #             #print(row)
        #
        #         line_count += 1
        #
        #     print("Processed ", line_count, " lines\n")

if __name__ == "__main__":
    main()