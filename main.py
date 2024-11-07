import csv
import traceback

csv_file = input('Enter the name of your input file (q to skip): ')
txt_file = 'test.txt'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ErrorHandling:
    def printTrace():
        print(f'{bcolors.FAIL}{traceback.format_exc()}{bcolors.ENDC}')

    def printErrorMsg(msg):
        print(f'{bcolors.WARNING}{bcolors.BOLD}{msg}{bcolors.ENDC}')

if csv_file.lower() != "q":
    # TODO Need to add file checker if current "test.txt" file already exist or not and to confirm overwrite.
    # TODO Check if "txt_file" ends with.txt or not or has . in the name
    txt_file = input('Enter the name of your output file: ')
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            file = csv.reader(my_input_file)
            next(file)
            for row in file:
                row[0] = row[0][0:10]
                my_output_file.write(";".join(row)+'\n')
        my_output_file.close()
else:
    print(f"{bcolors.OKGREEN}File not created{bcolors.ENDC}")


try:
    with open(txt_file, 'r') as ph:
        list = ph.readlines()

        # print(list[122])
except FileNotFoundError:
    ErrorHandling.printErrorMsg("File not found")
    ErrorHandling.printTrace()
except IndexError:
    ErrorHandling.printErrorMsg(f"Index out of range\nMax index is: {len(list)-1}")
    ErrorHandling.printTrace()
