# Program to generate python list from a text file containing words

outfile = open("cswarray.txt", "w")
infile = open("csw19.txt", "r")

outfile.write("[")


while True: 
  
    # Get next line from file 
    line = infile.readline()
    line = line[: -1]
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break

    outfile.write("\"{}\",".format(line))

outfile.write("]")