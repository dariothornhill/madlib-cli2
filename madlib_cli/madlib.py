import re

def read_template(path):
    with open(path, 'r') as file:
        raw_contents = file.read()
    return raw_contents

def parse_template(template):
    pattern = r"{(.*?)}"
    parts = re.findall(pattern, template)
    stripped = re.sub(pattern, "{}", template)
    return [stripped, parts]

def merge():
    pass