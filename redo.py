
"""
Code to transform manual entry json
"""
with open('produce-codes.json', 'r') as codesfile, open('new-produce-codes.json', 'w') as outfile:
    outfile.write('{\n\t"items":[\n')
    for line in codesfile:
        sep = line.find(":")
        outfile.write('\t{\n')
        outfile.write('\t\t"name":' + line[1:sep] + ',\n')
        outfile.write('\t\t"code":' + line[sep+1:len(line)-2] + '\n')
        outfile.write('\t},\n')
    outfile.write('\n]}')

bloop = open('new-produce-codes.json', 'r')
