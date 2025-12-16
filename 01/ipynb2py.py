import sys,json

input = open(sys.argv[1], 'r', encoding='utf8') #input.ipynb
input_json = json.load(input)
out_file = open(sys.argv[1].replace('.ipynb', '.py'), 'w', encoding='utf8') 

for i,cell in enumerate(input_json["cells"]):
    # out_file.write("#cell "+str(i)+"\n")
    for line in cell["source"]:
        if cell["cell_type"] != 'code' and not line.startswith('#'):
            out_file.write('### ')
        out_file.write(line)
    if cell["cell_type"] == 'code':
        out_file.write('\n\n')
    else:
        out_file.write('\n')
    
out_file.close()    