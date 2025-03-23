import csv

def classify_grade(average):
    if average >= 70:
        return '1'
    elif average >= 60:
        return '2:1'
    elif average >= 50:
        return '2:2'
    elif average >= 40:
        return '3'
    else:
        return 'F'

def calculate_student_averages(input_filename):
    output_filename = f"{input_filename}_out.csv"

    with open(input_filename, 'r') as infiloe, open(output_filename, 'w', newline='') as outfile:
        reader = csv.reader(input_filename)
        writer = csv.writer(outfile)

        for row in reader:
            student_id = row[0]
            try:
                grades = [int(grade) for grade in row[1:] if grade. strip().isdigit()]
            except ValueError:
                print(f"Non-numeric data found for student {student_id}, skipping invalid entries.")
                continue

            if grades:
                average_grade = sum(grades) / len(grades)
                classification = classify_grade(average_grade)
                writer.writerow([student_id, f"{average_grade:.2f}", classification])

def main():
    input_filename = input("Enter the filename of the student file: ").strip()
    calculate_student_averages(input_filename)

if __name__ == "__main__":
    main()