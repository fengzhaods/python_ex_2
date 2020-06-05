def is_valid_email_address(s):
    
    # How many @s ?
    num_at = s.count("@")
    if num_at != 1: return 1, "Must have exactly one @!"

    # How many chars pre @ i.e. in username ? All alfanum?
    l = s.split("@")
    username, domainname = l[0], l[1] 
    if len(username) not in range(3, 17): 
        return 2, "username must contain 3 - 16 alfanum chars"
    elif username.isalnum() == False:
        return 3, "username must only contain alfanum chars"

    # how many dots in domain name?
    if domainname.count(".") != 1:
        return 4, "domain name must have exactly one dot!"
    
    # split domain name into server and extension 
    server, extension = domainname.split(".")

    # how many chars in server? All alfanum?
    if len(server) not in range(2, 9):
        return 5, "server part (after @ and before .) must contain 2 - 8 alfanum chars"
    elif server.isalnum() == False:
        return 6, "server part (after @ and before .) must only contain alfanum chars"

    # is extension legit?
    if extension not in ["com", "edu", "org", "gov"]: 
        return 7, "extention invalid, must be from: com, edu, org, gov"

    return None, "Seems legit"
