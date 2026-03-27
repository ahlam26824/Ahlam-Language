
import sys
import os

variables = {}
if len(sys.argv) < 2:
    print("Usage: Ahlam <filename.am>")
    exit()

filename = sys.argv[1]
if not os.path.isfile(filename):
    print(f"Error: File '{filename}' not found!")
    exit()
with open(filename, "r") as file:
    code = file.readlines()

if not code:
    print(f"Error: File '{filename}' is empty!")
    exit()
for line_number, line in enumerate(code, start=1):
    line = line.strip()
    if not line:
        continue 
    if line.startswith("st"):
        try:
            start = line.find('"') + 1
            end = line.find('"', start)
            value = line[start:end]

            var_start = line.find("'") + 1
            var_end = line.rfind("'")
            var_name = line[var_start:var_end]

            if not var_name:
                print(f"Error: Variable name missing at line {line_number}")
                continue

            variables[var_name] = value
        except Exception as e:
            print(f"Error parsing STORE command at line {line_number}: {e}") 
    elif line.lower().startswith("display") or line.startswith("displaY"):
        try:
            parts = line.split("::")
            if len(parts) < 2:
                print(f"Error: DISPLAY syntax incorrect at line {line_number}")
                continue

            var_name = parts[1].strip()
            if var_name.startswith('"') and var_name.endswith('"'):
                print(var_name[1:-1])
            elif var_name in variables:
                print(variables[var_name])
            else:
                print(f"Error: Variable '{var_name}' not found at line {line_number}")
        except Exception as e:
            print(f"Error parsing DISPLAY command at line {line_number}: {e}")

    else:
        print(f"Warning: Unknown command at line {line_number}: {line}")