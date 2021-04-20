# A while loop allows us to loop through and execute a block of code multiple times.
    # It will continue to execute until a certain condition is false.
i = 1
while i <= 10: # Anything under this line and indented will be looped.
    print(i)
    i = i + 1 # Redefines variable i each loop. Also can be written as i += 1 (shorthand).
print("Done with loop!")

# Python will check the condition (in the "while" line) to ensure it is true before executing the loop code.