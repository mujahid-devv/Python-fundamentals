import sys

if len(sys.argv) < 2:
    print("Usage: python count_lines.py <filename>")
    sys.exit(1)
file_name = sys.argv[1]

with open(file_name) as f:
    lines = f.readlines()
print(f"line count in {file_name} is {len(lines)}")
