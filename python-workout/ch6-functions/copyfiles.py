from sys import argv

script, filename, *copynames = argv

# Copies one file into multiple new files
def copyfile(infile, *outfiles):
    for files in outfiles:
        with open(infile) as inputf, open(files, 'w') as output:
            for line in inputf:
                output.write(line)
    print("\t\tDONE.")

copyfile(filename, *copynames)
