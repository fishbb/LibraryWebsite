"""
Python script developed by Dan Lou (http://fishbb.github.io)

The script can convert text file to csv file. 

Also, it can convert jhove(https://github.com/openpreserve/jhove) TIFF validation output text file to csv file with columns of your selection.
"""

#!/usr/local/bin/python
import re

def open_text(fname):
    """
    open and read a text file line by line.
    convert to and return the list
    parameters: 
    fname: string, full path to the file
    """
    with open(fname, 'rb') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 
    return content
    
def lines_to_list(list, columns, delimiter):
    """
    convert a list of lines read from a file to a list of list by specify the number of columns and the delimiter
    parameters:
    list: list, lines returned by open_text()
    columns: integer, number of columns.
    delimiter: the delimiter to split a line
    """
    new_list = [list[i:i+columns] for i  in range(0, len(list), columns)]
#     new_list = zip(*[iter(list)]*columns) 
    header = []  
    for h in new_list[0]:
        header.append(str(h.decode()).split(delimiter)[0])
    content = [header]
    for l in new_list:
        line = []
        for c in l:
            line.append(''.join(str(c).split(delimiter)[1:]))
        content.append(line)
    return content        
   
def list_to_csv(list, file_name):
    """
    convert a list of list to a csv file
    parameters:
    list: list, list of list, returned by lines_to_list() or from elsewhere
    file_name: string, output csv file name, the delimiter is ^
    """
    csv_file = open(file_name, 'w')
    for l in list:
        line = '^'.join(l) + '\n'
        csv_file.write(line)
    csv_file.close()
    
# lines = open_text('output.txt')[2:]        
# list = lines_to_list(lines, 9, ':')
# list_to_csv(list, 'result.txt')

def jhove_to_csv(input_file, output_file, columns, start_column=None):
    """
    convert jhove TIFF output file to a csv file. First line of the file give total number of files validated and how many errors found.
    for errors, it also generates a separate file named "errors_"+output_file
    parameters:
    input_file: string, full path to jhove TIFF output file
    output_file: string, full path of the csv file
    columns: list, list of column names. Each column name should come from the start of certain lines in the jhove output file
    start_column: string, name of the first column. If leaves as blank, will use columns[0] instead.
    """
    log = open_text(input_file)[2:]
    result = []
    header = columns
    header.append('Full Details')
    temp = []
    start = start_column if start_column is not None else columns[0]
    for l in log:
        l = str(l.decode()).strip()
        if re.search('^'+start+':', l):
            if len(temp)>0:
                result.append(temp)
                temp=[]
                temp.append(l) 
            else:
                temp.append(l)
        else:
            temp.append(l)
    csv_list=[]     
    csv_list.append(header)   
    for r in result:
        record = [''] * len(header)
        for l in r:
            l=l.replace('\n', '\t')
            for i in range(len(columns)):
                c=columns[i]
                if re.search('^'+c+':', l):
                    record[i] = ''.join(l.split(c+":")[1:])
            record[-1] += '\t'+l
        csv_list.append(record)    
    errors = []
    if 'Status' in columns:
        i = columns.index('Status')
        for c in csv_list[1:]:
            if "Well-Formed" not in c[i]:
                errors.append(c)
    log = "Total files checked: %d Error files: %d" %(len(csv_list[1:]), len(errors[1:]))
    csv_list = [[log]] + csv_list             
    list_to_csv(errors, "errors_"+output_file)   
    list_to_csv(csv_list, output_file) 
    print(log)
    return csv_list


            
### example to convert jhove output file to csv, csv delimiter is ^
    
jhove_to_csv("output1.txt","output1.csv" ,["RepresentationInformation", "Format", "Status"])


