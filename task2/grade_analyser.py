'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be acheived by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''


import os
import csv

# Portfolio Task - Grade Analyser

def get_classification(average_grade):
    if average_grade >= 70:
        return '1'
    elif average_grade >= 60:
        return '2:1'
    elif average_grade >= 50:
        return '2:2'
    elif average_grade >= 40:
        return '3'
    else:
        return 'F'

def main():
    # Get the list of all CSV files in the "task2" directory
    task2_directory = "task2"
    bai_mingjiang_directory = os.path.join(task2_directory, "bai_mingjiang_outfiles")

    try:
        files_list = sorted([f for f in os.listdir(task2_directory) if f.endswith('.csv')])
        if not files_list:
            print("No CSV files found in the 'task2' directory.")
            return
    except FileNotFoundError:
        print(f"The directory '{task2_directory}' was not found. Please check the directory name.")
        return

    while True:
        # Display all files and let the user choose by ID
        print("\nAvailable files:")
        for idx, filename in enumerate(files_list):
            print(f"{idx + 1}. {filename}")
        print(f"{len(files_list) + 1}. Exit")

        # Get the file ID from the user
        try:
            file_id = int(input("\nEnter the file ID to select a file (or choose 'Exit' to quit): ")) - 1
            if file_id == len(files_list):
                print("Exiting the program.")
                break
            elif file_id < 0 or file_id >= len(files_list):
                print("Invalid file ID. Please enter a valid number.")
                continue
            file_name = files_list[file_id]
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Construct the full path to the selected file
        file_path = os.path.join(task2_directory, file_name)

        try:
            # Read in the data from the input file
            with open(file_path, 'r', encoding='utf-8') as infile:
                reader = csv.reader(infile)
                student_data = list(reader)
        except FileNotFoundError:
            print("The file was not found. Please check the file name and try again.")
            continue

        # Prepare the output data
        output_data = []
        for row in student_data:
            # Skip the header row if it's present
            if row[0].lower() == 'student_id':
                continue

            student_id = row[0]
            try:
                grades = [int(grade) for grade in row[1:] if grade.strip().isdigit()]
            except ValueError:
                print(f"Invalid data found for student {student_id}, skipping this record.")
                continue

            if grades:
                average_grade = sum(grades) / len(grades)
                classification = get_classification(average_grade)
                output_data.append([student_id, f"{average_grade:.2f}", classification])

        # Write the output data to a new CSV file in the "bai_mingjiang_outfiles" directory
        if not os.path.exists(bai_mingjiang_directory):
            os.makedirs(bai_mingjiang_directory)

        output_file_name = f"{file_name}_out.csv"
        output_file_path = os.path.join(bai_mingjiang_directory, output_file_name)

        try:
            with open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(output_data)
            print(f"The analysis has been saved to '{output_file_path}'")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    main()




