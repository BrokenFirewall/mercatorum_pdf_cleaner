from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
log = ""

# the settings of this arrays depends on the numbers of page that you want to remove from the single file
not_jump = [46, 50, 51, 52]
jump_1_page = range(1, 55, 1)
jump_2_page = [11, 12, 13, 14, 15, 16, 29, 30, 31, 32, 49, 53]

jump_1_page = [i for i in jump_1_page if i not in jump_2_page]
jump_1_page = [i for i in jump_1_page if i not in not_jump]


for file_number in range(1, 55, 1):
    try:
        infile = PdfFileReader(str(file_number) + '.pdf', 'rb')

        # jump 0 page
        if file_number in not_jump:
            for i in range(0, infile.getNumPages(), 1):
                p = infile.getPage(i)
                output.addPage(p)
        # jump 1 page
        elif file_number in jump_1_page:
            for i in range(1, infile.getNumPages(), 1):
                p = infile.getPage(i)
                output.addPage(p)
        # jump 2 page
        elif file_number in jump_2_page:
            for i in range(2, infile.getNumPages(), 1):
                p = infile.getPage(i)
                output.addPage(p)
        else:
            log += "jumped file " + str(file_number)
    except Exception as e:
        log += "error in " + str(file_number) + ": " + str(e)
        pass

with open('_summarized_.pdf', 'wb') as f:
    output.write(f)

f = open("_script_log.txt", "a")
f.write(log)
f.close()

print("done!")
