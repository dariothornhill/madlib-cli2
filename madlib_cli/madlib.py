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

def merge(stripped, input):
    complete = stripped.format(*input)
    return complete


# External dependencies
# Mocking

def write_madlib(path, madlib):
     with open(path, 'w') as file:
        file.write(madlib)

def prompt_user(parts):
    # inputs = []
    # for part in parts:
    #     inputs.append(input(f"Enter a/n {part}: "))  
    return [ input(f"Enter a {part}: ") for part in parts]

def welcome():
    print("Welcome! Let's have some fun :D. You will be prompted to enter a list of parts of speech. Once we do i'll create a fun story for you.")
    # print('Type q to quit')

if __name__ == "__main__":
    path='assets/madlib.txt'
    welcome()
    template = read_template('assets/make_me_a_game.txt')
    stripped, parts = parse_template(template)
    inputs = prompt_user(parts)
    madlib = merge(stripped, inputs)
    print(madlib)
    write_madlib(path, madlib)

