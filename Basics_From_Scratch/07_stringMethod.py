#1
#strip(parameter) ===============> return a copy of string after editing 
#delete right and left of string the input parameter 
# parameter bydefault ==> white space 

string="      I Love Python      "
print(string.strip()) #output: I Love Python

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))#output: I Love Python

#2
#title() ===> return a copy string first char of word is captale 
# capitalize()==title ()
#title =>> word after number captale 

x="12yossef haytham "
print(x.title()) #output: 12Yossef Haytham
print(x.capitalize())#output: 12yossef Haytham

#3
#upper() all word captale  
#lower() all word small 
name="Samy yoSSEf"
print(name.upper()) # output: SAMY YOSSEF
print(name.lower())# output: samy yossef


#4
#len() ==>  return number of item in parameter
#count("sub string ",start,end)==>return number of sub string 

print(name.count("S"))#output: 3

#5
# index("substring",start,end)=====> return index for substring  if not found ##get value error##
# find("substring",start,end) =====> return index for substring  if not found return ##-1##
# find use by string only...............

print(name.index("S"))#output: 0
print(name.find("s"))#output: -1 not found

#6
#split(separtor,maxsplit)   maxsplit= end index -1
#by default when item between (white space) put it in list [  ,  ,  ]

test="yossef haytham mohamed"
print(test.split() )#output: ['yossef', 'haytham', 'mohamed']

#7
#replace(old value,new value,count) =====> how much would i replace it
#used in string only 

print(test.replace(" ","-"))#output: yossef-haytham-mohamed

#8
#"seperator".join(prameter) parameter====> any thing can i loop in it

myList = ["yossef", "Mohamed", "Elsayed"]
print("-".join(myList))#output:yossef-Mohamed-Elsayed

#9
#isalpha()     isalnum()
name="yossef123"
print(name.isalpha()) #output : false 
print(name.isalnum()) #output : true
