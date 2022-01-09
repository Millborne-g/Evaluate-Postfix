#Millborne A. Galamiton BS CPE 2B
Entered_Postfix = []
output=[]
Entered_Postfix=input("Enter your postfix expression: ")
for i in range(len(Entered_Postfix)):#process of conversion 
    if(Entered_Postfix[i].isdigit()==True):#if value is a number it will append to the output
        output.append(int(Entered_Postfix[i]))
    elif(Entered_Postfix[i]=='*'): #if value is a "*" it pop the 2 value in front of it
        x=output.pop()
        y=output.pop()
        result = y * x
        output.append(result)
    elif(Entered_Postfix[i]=='+'):#if value is a "+" it pop the 2 value in front of it
        x=output.pop()
        y=output.pop()
        result = y + x
        output.append(result)
    elif(Entered_Postfix[i]=='-'):#if value is a "-" it pop the 2 value in front of it

        x=output.pop()
        y=output.pop()
        result = y - x
        output.append(result)
    elif(Entered_Postfix[i]=='/'):#if value is a "/" it pop the 2 value in front of it
        x=output.pop()
        y=output.pop()
        result=y/x
        output.append(result)
print(Entered_Postfix,"=",output[0])#display the result