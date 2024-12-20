import os
import re

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

# # html code
# codes = {
#     'file1.html': '''
# <!-- Write your comments here -->
# ''',
#     'file2.html': '''
# <!-- This is a comment -->
# <p>This is a paragraph.</p>
# <!-- Remember to add more information here -->
# ''',
#     'file3.html': '''
# <p>This is a paragraph.</p>
# <!-- <p>This is another paragraph </p> -->
# <p>This is a paragraph too.</p>
# ''',
#     'file4.html': '''
# <p>This is a paragraph.</p>
# <!--
# <p>Look at this cool image:</p>
# <img border="0" src="pic_trulli.jpg" alt="Trulli">
# -->
# <p>This is a paragraph too.</p>
# ''',
#     'file5.html': '''
# <p>This <!-- great text --> is a paragraph.</p>
# '''
# }

# # jsx code
# codes = {
#     'file1.jsx': '''
# function App() {
#   return (
#     <div>
#       {/* This is a single-line comment */}
#       <h1>Hello, World!</h1>
#     </div>
#   );
# }
# ''',
#     'file2.jsx': '''
# function App() {
#   return (
#     <div>
#       {/*
#         This is a multi-line comment
#         explaining the header below
#       */}
#       <h1>Hello, World!</h1>
#     </div>
#   );
# }
# ''',
#     'file3.jsx': '''
# // This is a single-line comment
# const greeting = "Hello, World!";

# /*
#   This is a multi-line comment
#   explaining the App component
# */
# function App() {
#   return (
#     <div>
#       <h1>{greeting}</h1>
#     </div>
#   );
# }
# ''',
#     'file4.jsx': '''
# function App() {
#   return (
#     <div>
#       <h1>
#         Hello, {/* Inline comment inside an element */} World!
#       </h1>
#     </div>
#   );
# }
# ''',
#     'file5.jsx': '''
# function App() {
#   const isLoggedIn = true;

#   return (
#     <div>
#       {
#         isLoggedIn
#         ? <h1>Welcome back!</h1> // User is logged in
#         : <h1>Please log in.</h1> /* User is not logged in */
#       }
#     </div>
#   );
# }
# '''
# }

## css code
# codes = {
#     'file1.css': '''
# /* This is a single-line comment */
# p {
#   color: red;
# }
# ''',
#     'file2.css': '''
# p {
#   color: red;  /* Set text color to red */
# }
# ''',
#     'file3.css': '''
# p {
#   color: /*red*/blue; 
# }
# ''',
#     'file4.css': '''
# /* This is
# a multi-line
# comment */

# p {
#   color: red;
# }
# '''
# }

# .yml / .yaml code
codes = {
    'file1.yml': '''
# This is a single-line comment
name: Verosha
age: 25
''',
    'file2.yml': '''
# Key-value pair example
user:
  name: Verosha
  age: 25
  email: verosha@example.com
''',
    'file3.yml': '''
# List example
fruits:
  - apple
  - banana
  - cherry
''',
    'file4.yaml': '''
# Multi-line value example
description: >
  This is a multi-line
  string value for the
  YAML example.
''',
    'file5.yaml': '''
# Nested structure example
settings:
  database:
    host: localhost
    port: 5432
    username: admin
    password: secret
  features:
    enabled: true
    beta: false
'''
}


remove_comment(codes)
print(codes)
