

################################
def drawline(lengh,direction):
    if direction=="h":
        sign="-"
        return sign

    elif direction=="v":
        sign="|"
        return sign
################################

########## START script#########
lengh=5
direction="h"

if direction=="v":
    for i in range(lengh):
        print(drawline(lengh,direction))
        i+=1
elif direction=="h":
    print(drawline(lengh,direction)*lengh)

########## END script#########






