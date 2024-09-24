#!/bin/python3

int AgeRange

MathDefined =  13 <= AgeRange <= 21     # Chained comparison: is UserAge between 13 and 21
JavaCDefined = (AgeRange > 13) and (AgeRange < 21)  # Equivalent explicit logical comparison

if MathDefined == JavaCDefined:
    print("Python Can Do Math Both Ways")

print("End of program")
