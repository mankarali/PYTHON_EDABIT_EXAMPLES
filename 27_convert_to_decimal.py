"""
Convert to Decimal Notation
Create a function to convert a list of percentages to their decimal equivalents.

Examples
convert_to_decimal(["1%", "2%", "3%"]) ➞ [0.01, 0.02, 0.03]

convert_to_decimal(["45%", "32%", "97%", "33%"]) ➞ [0.45, 0.32, 0.97, 0.33]

convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]) ➞ [0.33, 0.981, 0.5644, 1]

"""
def convert_to_decimal(perc):
    
    a = [] 
    
    for i in perc:
        a.append(float(i[:-1])/100)
        
    for i in a:
        if str(i) == "1.0":
            a.remove(1.0)
            a.append(1)
    return(a)
    
    
    
    
convert_to_decimal(["33%", "98.1%", "56.44%", "100%"])   
