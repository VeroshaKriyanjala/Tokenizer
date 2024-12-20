
# This script is used to index the codebase of a project.
import os
import re

def index_codebase(root_dir, allowed_extensions=None, excluded_dirs=None,excluded_files=None):
    if allowed_extensions is None:
        allowed_extensions = {'.py', '.html', '.css', '.java', '.yml','.yaml' '.js', '.jsx'}
    if excluded_dirs is None:
        excluded_dirs = {'.git', 'venv','.idea','.vsode','node_modules','__pycache__', 'build', 'dist'}
    if excluded_files is None:
        excluded_files = {'.gitignore','.env'}

    codes={}

    def read_the_file(file):
        with open(file, 'r',encoding="utf-8") as f:
            return f.read()
    
    def traverse_directory(current_dir, indent_level=0):
        try:
            entries = sorted(os.listdir(current_dir))
            for entry in entries:
                entry_path = os.path.join(current_dir, entry)
                if os.path.isdir(entry_path):
                    if entry in excluded_dirs:
                        continue
                    print("    " * indent_level + f"|- {entry}/")
                    traverse_directory(entry_path,indent_level+1)
                elif os.path.isfile(entry_path):
                    if entry in excluded_files:
                        continue
                    _, extension = os.path.splitext(entry)
                    if extension in allowed_extensions:
                        file_content=read_the_file(entry_path)
                        codes[entry]=file_content
                        print("    " * indent_level + f"|- {entry}")
        except PermissionError:
            print("    " * indent_level + "|- [Permission Denied]")
    
    traverse_directory(root_dir)

    formatted_code=[f"{file_name}:{{{file_code}}}" for file_name,file_code in codes.items()]

    # print("codes : [")
    # print(",\n".join(formatted_code))
    # print("]")

    return codes

codebase_path = "/home/verosha/Music/csi-sentinel"
code_before_remove_comment=index_codebase(codebase_path)

# The remove_comment function is defined in the remove_comments.py file.
# This setion is used to remove comments from the codebase.
def remove_comment(codes):
    for entry in codes:
        _, extension = os.path.splitext(entry)
        match extension:
            case '.py':
                code = codes[entry]
                code_lines = []
                in_multiline_comment = False
                for line in code.split('\n'):
                    if in_multiline_comment:
                        if '"""' in line or "'''" in line:
                            in_multiline_comment = False
                        continue                  
                    if '"""' in line or "'''" in line:
                        in_multiline_comment = True
                        continue
                    line = re.sub(r'#.*$', '', line).rstrip()
                    if line:
                        code_lines.append(line)
                codes[entry] = '\n'.join(code_lines)
                
            case '.java':
                code = codes[entry]
                in_block_comment = False
                code_lines = []
                for line in code.split('\n'):
                    if in_block_comment:
                        if '*/' in line:
                            in_block_comment = False
                        continue
                    if '/*' in line:
                        in_block_comment = True
                        continue
                    line = re.sub(r'//.*$', '', line).rstrip()
                    if line:
                        code_lines.append(line)
                codes[entry] = '\n'.join(code_lines)

            case '.html':
                code = codes[entry]
                code = re.sub(r'<!--.*?-->', '', code, flags=re.DOTALL)
                code_lines = [line.rstrip() for line in code.split('\n') if line.strip()]
                codes[entry] = '\n'.join(code_lines)

            case '.js':
                code = codes[entry]
                in_block_comment = False
                code_lines = []
                for line in code.split('\n'):
                    if in_block_comment:
                        if '*/' in line:
                            in_block_comment = False
                        continue
                    if '/*' in line:
                        in_block_comment = True
                        continue
                    line = re.sub(r'//.*$', '', line).rstrip()
                    if line:
                        code_lines.append(line)
                codes[entry] = '\n'.join(code_lines)
            
            case '.jsx':
                code = codes[entry]
                code = re.sub(r'\{\s*/\*.*?\*/\s*\}', '', code, flags=re.DOTALL)
                code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
                in_block_comment = False
                code_lines = []
                for line in code.split('\n'):
                    if in_block_comment:
                        if '*/}' in line:
                            in_block_comment = False
                        continue
                    if '{/*' in line:
                        in_block_comment = True
                        continue
                    line = re.sub(r'//.*$', '', line).rstrip()
                    if line:
                        code_lines.append(line)
                codes[entry] = '\n'.join(code_lines)

            case '.css':
                code = codes[entry]
                code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
                in_block_comment = False
                code_lines = []
                for line in code.split('\n'):
                    if in_block_comment:
                        if '*/' in line:
                            in_block_comment = False
                        continue
                    if '/*' in line:
                        in_block_comment = True
                        continue
                    code_lines.append(line)
                codes[entry] = '\n'.join(code_lines)

            case '.yml' | '.yaml':
                code = codes[entry]
                code_lines = []
                for line in code.split('\n'):
                    line = re.sub(r'#.*$', '', line).rstrip()
                    if line.strip():
                        code_lines.append(line)
                codes[entry] = '\n'.join(code_lines)

            case _:
                pass
        
    formatted_code=[f"{file_name}:{{{file_code}}}" for file_name,file_code in codes.items()]

    print("codes : [")
    print(",\n".join(formatted_code))
    print("]")

    return codes

code_after_remove_comment=remove_comment(code_before_remove_comment)
code_after_remove_comment