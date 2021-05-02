"""
Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

"""


borze_code = input()
 
if "--" in borze_code :
    borze_code = borze_code.replace("--","2")
if "-." in borze_code :
    borze_code = borze_code.replace("-.","1")
if "." in borze_code :
    borze_code = borze_code.replace(".","0")
 
print(borze_code)
