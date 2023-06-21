"""Given a string, find all the possible subsequences of the string"""

def subs(s):
    if len(s)==0:
        output=[]
        output.append[""]
        return output
    
    ss=s[1:]
    so=subs(ss)
    
    output=[]
    for sub in so:
        output.append(sub)
        output.append(s[0] + sub)
    return output    
