from typing import List, Literal
list1 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
list2 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
#Worst Method but it had to be done. 
#Tons of open spots in the list to account for anyone putting a lot of terms in their list
checkchoice=False
#SelfExplanatory, checks the choice the user makes on which list to put first in our combinations
#It is used during the If Else at line 47 
x = ""
y = "" #x and y are used to register the stop command when entering terms into the lists 1 and 2 respectively 
#they are used at the while loops at lines 56 and 64 respectively

listsize1=0
listsize2=0 #Each lists' "true" size. len(list) doesnt work in this case because the list is always large
#The while loops at lines 56 and 64 correlate how many words the user enters for each list 
#to these two variables

choiceorder = "" #defined as input("") later on and is 
#almost the same use case as checkchoice but it is a string to make user input for this variable easier
#used in Combine() and lines 50-59

LISTiteration= 0 #Used to switch elements in the lists, increasing one at a time as the user enters words

def Combine():
    list1c = 0 #these are indicators of the number of the element the script is dealing with from each list 
    #and it helps to read the lists easier
    list2c = 0
    if choiceorder=="one":
        while list1c<=listsize1:
            Output1_2=list1[list1c]+" "+list2[list2c]
            if list1c>=listsize1:
                break
            list2c=list2c+1
            print ("https://www.google.com/search?q="+Output1_2.replace(" ","+").replace("/","%2F")
                   .replace('"',"%22").replace("<","%3C").replace(">","%3E").replace("#","%23")
                   .replace("&","%26").replace("%","%25").replace("|","%7C").replace("?","%3F"))
            #^^this encodes the regular phrases such as "foo bar" into "foo+bar", something that can
            #be inserted after https://www.google.com/search?q= without issues with unsafe characters
            
            if list2c==listsize2:
                list2c=0
                list1c=list1c+1
            
    if choiceorder=="two":
        while list2c<=listsize2:
            Output2_1=list2[list2c]+" "+list1[list1c]
            if list2c>=listsize2:
                break
            list1c=list1c+1
            print ("https://www.google.com/search?q="+Output1_2.replace(" ","+").replace("/","%2F")
                   .replace('"',"%22").replace("<","%3C").replace(">","%3E").replace("#","%23")
                   .replace("&","%26").replace("%","%25").replace("|","%7C").replace("?","%3F"))
            
            if list1c==listsize1:
                list1c=0
                list2c=list2c+1
            
print("Input 'one' for ordering List1's terms First or two for ordering List2's terms first")
choiceorder = input("")
if choiceorder == "one" or choiceorder == "two":
    print("Input Accepted")
else:                         #all of this is for choosing which list comes first
    while checkchoice==False:
        print("Please enter 'one' to order list 1 first or 'two' to order list 2 first")
        choiceorder = input("")
        if choiceorder == "one" or choiceorder == "two":
            checkchoice = True
    
print("Enter Each Item for List1 then Hit Enter. To Stop, type stop")
while 10==10:
    x=input()
    if x=="stop":
        break
    listsize1=listsize1+1
    list1[LISTiteration] = x
    LISTiteration = LISTiteration +1
LISTiteration=0
print("Enter Each Item for List2 then Hit Enter. To Stop, type stop")
while 10==10:                          #These two while loops are the logic to entering words into each list
    y=input()
    if y=="stop":
        break
    listsize2=listsize2+1
    list2[LISTiteration] = y
    LISTiteration= LISTiteration + 1
Combine()
    


