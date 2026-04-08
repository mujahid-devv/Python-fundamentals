def read_logs(filepath):
    """Generator: yields one line at a time."""
    with open(filepath) as f:
        for raw_line in f:
            yield raw_line.strip()

gen = read_logs("Advance/generators/logs.log")
for entry in gen:
    print(entry)