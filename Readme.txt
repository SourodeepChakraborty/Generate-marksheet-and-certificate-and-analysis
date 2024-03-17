# MarkSheetGenerator

MarkSheetGenerator is a Python class that helps in generating individual mark sheets, analyzing results, and generating certificates for students based on their marks.

## Features

- Reads data from an input file containing students' marks.
- Generates individual mark sheets for each student.
- Analyzes results to find the top scorer, top scorer for each subject, and more.
- Generates certificates for students based on their performance.

## Usage

1. Prepare an input file containing students' marks. Each line should contain a student's name, subject, and score separated by spaces.
   Example:
Ayan        Networking        50
Nil             Networking        60
Trisha      Networking        70
Snigdha  Networking        67
Ayan        OS                         55
Nil             OS                         62
Trisha      OS                         90
Snigdha  OS                         76
Ayan        AI/ML                  50
Nil             AI/ML                 86
Trisha      AI/ML                 77
Snigdha  AI/ML                 46
Ayan        Project               55
Nil             Project                36
Trisha      Project                40
Snigdha  Project                36

2. Instantiate the MarkSheetGenerator object with the input file path.
	
	input_file = "input"
	generator = MarkSheetGenerator(input_file)

i.  Call the write_results_to_file method to generate a results file containing the analysis.

	output_file = "results.txt"
	generator.write_results_to_file(output_file)

ii. Call the generate_individual_certificates method to generate individual certificates for each student.

	generator.generate_individual_certificates()


SAMPLE OUTPUT
-------------
A results file (results.txt) containing the analysis of the students' marks.
Individual mark sheet files for each student (e.g., Ayan_marksheet.txt, Nil_marksheet.txt).
Individual certificate files for each student (e.g., Ayan_certificate.txt, Nil_certificate.txt).
