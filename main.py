import os
from indexing import indexing_codebase 
from remove_comments import remove_comments

def save_to_file(codes,output_path):
    try:
        with open(output_path, "w", encoding="utf-8") as f1:
            for file_name, content in codes.items():
                f1.write(f"--- {file_name} ---\n")
                f1.write(content)
                f1.write("\n\n")
            print(f"Code before removing comments saved to {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    codebase_path = "/home/verosha/Music/csi-sentinel"

    code_before_remove_comment = indexing_codebase(codebase_path)
    save_to_file(code_before_remove_comment,"outputs/code_before_remove_comment.txt")

    cleaned_codes = remove_comments(code_before_remove_comment)
    save_to_file(cleaned_codes,"outputs/cleaned_codes.txt")

if __name__ == "__main__":
    main()
