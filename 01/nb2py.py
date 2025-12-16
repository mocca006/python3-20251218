import time, os, sys, pathlib, shutil,json

def get_file_list_include_subfolder(path1='.', filter_name='ipynb', absolute_path=False):
    '''
    purpose:
        get file list from the specified folder and its sub folders
    argument：
        path1：the specified folder
    '''
    file_list = []
    for dirPath, dirNames, fileNames in os.walk(path1):
        for x in fileNames:
            if isinstance(filter_name, list):
                if x.split('.')[-1] in filter_name:
                    if absolute_path:
                        file_list.append(os.path.join(path1, dirPath, x))
                    else:
                        file_list.append(os.path.join(dirPath, x))
            else:
                if x.split('.')[-1] == filter_name:
                    if absolute_path:
                        file_list.append(os.path.join(path1, dirPath, x))
                    else:
                        file_list.append(os.path.join(dirPath, x))
    return file_list

def convert_nb(input_file_name):
    print(input_file_name)
    input_file = open(input_file_name, 'r', encoding='utf8') 
    out_file_name = input_file_name.replace('.ipynb', '.py').replace('\\', '/') #.split('/')[-1]
    out_file = open(out_file_name, 'w', encoding='utf8') 
    input_json = json.load(input_file)
    for i,cell in enumerate(input_json["cells"]):
        # out_file.write("#cell "+str(i)+"\n")
        for line in cell["source"]:
            if cell["cell_type"] != 'code' and not line.startswith('#'):
                out_file.write('### ')
            elif cell["cell_type"] == 'code' and line.startswith('!'):
                out_file.write('# ')

            out_file.write(line)
        if cell["cell_type"] == 'code':
            out_file.write('\n\n')
        else:
            out_file.write('\n')
        
    out_file.close()    
    
if __name__ == '__main__' :
    input_file_name = sys.argv[1] 
    if os.path.isdir(input_file_name):
        file_list = get_file_list_include_subfolder(input_file_name)
        for file_name in file_list: # os.listdir(input_file_name):
            if not file_name.endswith('.ipynb') or \
                '.ipynb_checkpoints' in file_name : continue
            # convert_nb(os.path.join(input_file_name, file_name))
            convert_nb(file_name)
    else:    
        convert_nb(input_file_name)    