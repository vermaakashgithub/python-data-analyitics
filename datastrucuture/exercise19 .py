def cheese_and_crackers(cheese_count, boxes_of_crackers):#define a function cheese_and_crackers 
    print(f"you have {cheese_count} cheese!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party!")
    print("get a blanket.\n")


print("we can just give the function numbers directly:") # define function with number
cheese_and_crackers(20,30)


print("or ,we can use variables from our script:") #define the two variables and assing two number
amount_of_cheese = 10
amount_of_crakers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crakers) #define function with variables


print("we can even do math inside too:") #function and add  the variables or we can do math inside to
cheese_and_crackers(10+20, 5+6)
 

print("and we can combine the two ,variables and math:") #function and calculation  varaiables and number or we can combine the two , variables and math
cheese_and_crackers(amount_of_cheese+100,amount_of_crakers+1000)



