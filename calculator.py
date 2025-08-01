class calculator:
    def add(self,a,b):
        return a + b 
    
    def sub(self,a,b):
        return a - b 
    
    def div(self,a,b):
        return a % b 
    
    def multi(self,a,b):
        return a * b 
    
cal = calculator()


num1 = float(input("Enter Your First Number : "))
num2 = float(input("Enter Your Second Number : "))
op = input("+ , - , * , % : ")


if op == "+":
    result = cal.add(num1,num2)
elif op == "-":
    result = cal.sub(num1,num2)
elif op == "*":
    result = cal.multi(num1,num2)
elif op == "%":
    result = cal.div(num1,num2)
else:
    result = "Error"


print("Result: ", result)