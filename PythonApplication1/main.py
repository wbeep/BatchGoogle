from typing import List, Literal
list1 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
list2 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
checkchoice=False
x = ""
y = ""
listsize1=0
listsize2=0
choiceorder = ""
LISTiteration= 0
def EncodeURL(input1):
    print ("https://www.google.com/search?q="+input1.replace(" ","+").replace("/","%2F").replace('"',"%22"
    .replace("<","%3C").replace(">","%3E").replace("#","%23").replace("&","%26").replace("%","%25").replace("|","%7C").replace("?","%3F")))

def Combine():
    list1c = 0
    list2c = 0
    if choiceorder=="one":
        while list1c<=listsize1:
            Output1_2=list1[list1c]+" "+list2[list2c]
            if list1c>=listsize1:
                break
            list2c=list2c+1
            print ("https://www.google.com/search?q="+Output1_2.replace(" ","+").replace("/","%2F").replace('"',"%22")
    .replace("<","%3C").replace(">","%3E").replace("#","%23").replace("&","%26").replace("%","%25").replace("|","%7C").replace("?","%3F"))
            
            if list2c==listsize2:
                list2c=0
                list1c=list1c+1
            
    if choiceorder=="two":
        while list2c<=listsize2:
            print(list2[list2c]+" "+list1[list1c])
            list1c=list1c+1
            if list2c==listsize2-1:
                break
            if list1c==listsize1:
                list2c=0
                list2c=list2c+1
print("Input 'one' for ordering List1's terms First or two for ordering List2's terms first")
choiceorder = input("")
if choiceorder == "one" or choiceorder == "two":
    print("Input Accepted")
else:
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
while 10==10:
    y=input()
    if y=="stop":
        break
    listsize2=listsize2+1
    list2[LISTiteration] = y
    LISTiteration= LISTiteration + 1
Combine()
    


