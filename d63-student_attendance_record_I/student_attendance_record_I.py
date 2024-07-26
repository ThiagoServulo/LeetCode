def checkRecord(s):
   
    for i in range(0, len(s) - 2):
        if (s[i:i+3].count('L') == 3):
            return False
    
    if(s.count('A') >= 2):
        return False

    return True
    
print(checkRecord("PPALLL")) # False
print(checkRecord("PPALLP")) # True