# madlib-cli2
This project is a short game which prompts the user for English words to create a funny story.

## Getting Started
This project assumes that you have poetry and pyenv setup in your environment.

To get started with this project, clone the repository and cd into the folder and run poetry install to setup dependencies. Finally enter the shell and run the application as a python module

```bash
git clone git@github.com:dariothornhill/madlib-cli2.git
cd madlib-cli2
poetry install
poetry shell
python -m madlib_cli/madlib.py
```

## Changelog
- Added parse_template function - https://github.com/dariothornhill/madlib-cli2/pull/5
- Added read_template  - https://github.com/dariothornhill/madlib-cli2/pull/4
- Setup basic tests - https://github.com/dariothornhill/madlib-cli2/pull/3
- Added github actions - https://github.com/dariothornhill/madlib-cli2/pull/2
- First commit - basic project files

## TODO Checklist
- [x] Add unit test setup
- [x] Add github actions
- [ ] Welcome message
- [ ] Prompt user for words
- [ ] Populate template with user responses
- [ ] Print final madlib to user
- [ ] Write final madlib to file (commit this file)
- [x] Madlib template file
- [x] Add small test template
- [x] Tokenize template
- [x] Write a test for read_template which will call the read_template function with the path to our test template and check that the result are a stripped version of the its contents.
- [x] write the read_template function to pass above test
- [x] Write a test for the parse_template function which will call it with an example template string and check that returns the string with the language parts removed and a list of the language parts (list, tuple, dict)
- [x] Write the parse_template function to pas the above tests
- [x] Write a test for the merge function that calls it with a template and a list of strings representing language parts and checks that the returned string inserts those languages parts into the template.
- [x] Write the merge function

Stretch
- [ ] Test that final madlib written correctly to this