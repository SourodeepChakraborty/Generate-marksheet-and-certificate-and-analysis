'''
Program Name: Marksheet & Certificate Generator and analysis
Dev Name: Sourodeep Chakraborty
Last Edited: 17/03/2024 -- 07:59 pm
Input in my Data Structure: <<student name>> <<subject name>> <<marks obtained>>
Output Data Structure: <<Topper>> <<Topper For Each Subject>> <<List of Student in alphabetical
order>> <<List Of student in total mark obtain list>>
Input Function: <<read_data>>
Output Function: <<generate_individual_marksheets>> <<write_results_to_file>>
<<generate_individual_certificates>>
'''

import datetime
class MarkSheetGenerator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.students_marks = {}
        self.read_data()
        self.generate_individual_marksheets()

    def read_data(self):
        with open(self.input_file, 'r') as f:
            data = f.readlines()

        for line in data:
            student, subject, score = line.split()
            if student not in self.students_marks:
                self.students_marks[student] = {}
            self.students_marks[student][subject] = int(score)

    def generate_individual_marksheets(self):
        for student, subjects in self.students_marks.items():
            output_file = f"{student}_marksheet.txt"
            with open(output_file, 'w') as f:
                f.write(f"Student: {student}\n")
                f.write("Subject\t\tMarks\n")
                f.write("-------------------\n")
                total_marks = 0
                for subject, score in subjects.items():
                    f.write(f"{subject}\t\t{score}\n")
                    total_marks += score
                f.write("-------------------\n")
                f.write(f"Total\t\t{total_marks}\n")
                f.write("-------------------\n")

    def get_topper(self):
        topper = max(self.students_marks.items(), key=lambda x: sum(x[1].values()))
        return topper[0], sum(topper[1].values())

    def get_topper_for_each_subject(self):
        toppers = {}
        for subject in next(iter(self.students_marks.values())).keys():
            topper = max(self.students_marks.items(), key=lambda x: x[1].get(subject, 0))
            toppers[subject] = (topper[0], topper[1].get(subject, 0))
        return toppers

    def get_students_alphabetic(self):
        students_sorted = sorted(self.students_marks.items())
        students_data = []
        for student, subjects in students_sorted:
            final_marks = sum(subjects.values())
            students_data.append((student, subjects, final_marks))
        return students_data

    def get_students_total_marks(self):
        students_sorted = sorted(self.students_marks.items(), key=lambda x: sum(x[1].values()), reverse=True)
        students_data = []
        for student, subjects in students_sorted:
            total_marks = sum(subjects.values())
            students_data.append((student, total_marks))
        return students_data

    def get_students_percentage(self):
        students_data = []
        for student, subjects in self.students_marks.items():
            total_marks = sum(subjects.values())
            percentage = (total_marks / 400) * 100
            students_data.append((student, percentage))
        return students_data

    def write_results_to_file(self, output_file):
        with open(output_file, 'w') as f:
            f.write("A. Topper:\n")
            topper = self.get_topper()
            f.write(f"Student: {topper[0]}, Total Marks: {topper[1]}\n\n")

            f.write("B. Topper for Each Subject:\n")
            toppers = self.get_topper_for_each_subject()
            for subject, topper_info in toppers.items():
                f.write(f"Subject: {subject}, Topper: {topper_info[0]}, Marks: {topper_info[1]}\n")
            f.write("\n")

            f.write("C. List of Students in Alphabetical Order with All Marks Plus Final Marks:\n")
            students = self.get_students_alphabetic()
            for student_info in students:
                f.write(f"Student: {student_info[0]}, Marks: {student_info[1]}, Total Marks: {student_info[2]}\n")
            f.write("\n")

            f.write("D. List of Students in Total Marks Obtained List:\n")
            students = self.get_students_total_marks()
            for student_info in students:
                f.write(f"Student: {student_info[0]}, Total Marks: {student_info[1]}\n")
            f.write("\n")

    def generate_certificate(self, student_name, percentage):
        certificate = f"Certificate of Achievement\n\n"
        certificate += f"This is to certify that {student_name} has successfully completed the course with a percentage of {percentage:.2f}%.\n"
        if percentage >= 80:
            certificate += "Congratulations on your outstanding performance!\n"
        elif percentage >= 60:
            certificate += "Well done on your good performance!\n"
        else:
            certificate += "Keep up the good work!\n"
        certificate += f"\nDate: {datetime.datetime.now().strftime('%Y-%m-%d')}\n\nSignature:\nDr. Anirban Mukherjee\n"
        return certificate

    def generate_individual_certificates(self):
        for student, percentage in self.get_students_percentage():
            certificate = self.generate_certificate(student, percentage)
            output_file = f"{student}_certificate.txt"
            with open(output_file, 'w') as f:
                f.write(certificate)


input_file = "input"
output_file = "results.txt"
generator = MarkSheetGenerator(input_file)
generator.write_results_to_file(output_file)
generator.generate_individual_certificates()
