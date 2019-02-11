from decimal import Decimal
import os

def GetTokenArray(expression):
    tokens=[];
    token="";
    for char in expression:
        if char in "/*-+":
            tokens.append(token);
            tokens.append(str(char));
            token="";
        else:
            token+=str(char);
    tokens.append(token);
    return tokens;

def Calculate(tokens):
    while "/" in tokens:
        index=tokens.index("/");
        dividend=tokens.pop(index-1);
        tokens.pop(index-1);
        divider=tokens.pop(index-1);
        quotient=float(dividend)/float(divider);
        tokens.insert(index-1,str(quotient));
        pass
    while "*" in tokens:
        index=tokens.index("*");
        operand1=tokens.pop(index-1);
        tokens.pop(index-1);
        operand2=tokens.pop(index-1);
        result=float(operand1)*float(operand2);
        tokens.insert(index-1,str(result));
        pass
    while "-" in tokens:
        index=tokens.index("-");
        operand1=tokens.pop(index-1);
        tokens.pop(index-1);
        operand2=tokens.pop(index-1);
        result=float(operand1)-float(operand2);
        tokens.insert(index-1,str(result));
        pass
    while "+" in tokens:
        index=tokens.index("+")
        operand1=tokens.pop(index-1);
        tokens.pop(index-1)
        operand2=tokens.pop(index-1);
        result=float(operand1)+float(operand2);
        tokens.insert(index-1,str(result));
        pass
    return tokens;


IsContinue = True;
while(IsContinue):
	expressionInput=input("Input an arithmatic expression (x+y-z/a*b):");
	tokens=GetTokenArray(expressionInput);
	tokens=Calculate(tokens)
	print("The result is : "+tokens[0]);
	IsContinue=input("Do you want to continue (Y/N)?:")=="Y";
	if os.name=="nt":
		os.system('cls')
	else:
		os.system('clear')
