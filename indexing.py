# This script is used to index the codebase of a project.

import os
import re

def indexing_codebase(root_dir, allowed_extensions=None, excluded_dirs=None,excluded_files=None):
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

    # formatted_code=[f"{file_name}:{{{file_code}}}" for file_name,file_code in codes.items()]
    # print("Codes before remove comment : [")
    # print(",\n".join(formatted_code))
    # print("]")

    print(codes)
    return codes