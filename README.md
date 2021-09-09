

## Working With Regular Expression

### Overview

This task deals with implementing functionalities for parsing email addresses. Parsing in this context simply means looking through email address strings to pick out important and useful information.

### Parsing Email Addresses

Email addresses are usually in the format: `username@domain`. Ex. `johndoe@gmail.com`, `jane+doe@yahoo.com`, etc. This means that there are two(2) useful information we will need out of email addresses, namely `username` and `domain`

Given the email address (`johndoe@gmail.com`), we will have the dictionary below as the output of the parsing

```python

{
  'username': 'johndoe',
  'domain': 'gmail.com'
}

```

Also, given the email address (`jane+doe@yahoo.com`), we will have the dictionary below as the output of the parsing

```python

{
  'username': 'jane+doe',
  'domain': 'yahoo.com'
}

```

When writing the logic for parsing email addresses, below are CONSTRAINTS i  put into consideration

- Usernames will be made up of alphabets or alphanumerics. Ex. `john`, `johndoe`, `john123`. Note that usernames cannot start with a number
- Usernames should also support only the `+` character in between as in example 2 above
- Domains will always end in `.com`, Ex. `gmail.com`, `yahoo.com`, `bz2.com`, etc.
- The part before `.com` in domains will be made up of alphabets or alphanumerics, Ex. `gmail`, `bz2`, `dom555`, etc. Note that domains cannot start with a number

To complete the implementation of the `email_parser` function defined in the `email_parser.py` module, i needed to

1. Provide a regex pattern 
2. Complete the implementation to do the expected parsing
3. Return `None` for emails that do not match the regex pattern

## how to use this app
- open email_parser.py file an enter the email you want to parse
- and the run by pressing the play button or using the command+R on mac
