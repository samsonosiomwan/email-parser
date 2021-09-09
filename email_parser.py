import re
def email_parser(email):
  """email parsing function to extract useful information(username and domain) from email"""
  
  #list holding information to parse and parsed_info variable holding the extracted(splits) info with parsed output
  info_to_parse, parsed_info, = ['username','domain'], re.split(r"@",email)
  
  #variable to cast output to dict data type 
  parsing_output = dict(zip(info_to_parse,parsed_info)) 

  # statement to check if email address follows email pattern
  return parsing_output if re.search(r"^[a-zA-Z][a-zA-Z0-9+]+[a-zA-Z0-9]@[a-z][a-zA-Z0-9]+\.com$",email) else None

#enter email to you want to parse
print(email_parser('amsonos+iomwan@gmail.com'))


