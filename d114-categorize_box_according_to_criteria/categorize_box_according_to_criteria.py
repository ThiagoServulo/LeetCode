def categorizeBox(length, width, height, mass):
    n = 0
    if(length >= 10000 or width >= 10000 or height >= 10000 or 
       (length * width * height) >= 1000000000):
        n += 1
    
    if(mass >= 100):
        n += 10
    
    if(n == 1):
        return "Bulky"
    elif (n == 10):
        return "Heavy"
    elif (n == 11):
        return "Both"
    else:
        return "Neither"
    
print(categorizeBox(1000, 35, 700, 300)) # Heavy