def  sum():
   
    result = {}
    result ["s"] = (f1["s"]*f2["m"])+(f2["s"]*f1["m"])
    result ["m"] = f1["m"] *  f2["m"]
    return result
def multiply():
    result = {}
    result["s"] = f1["s"]*f2["s"]
    result["m"] = f1["m"]*f2["m"]
    return result

def Taghsim():
    result1={}
    result2={}
    result1 = {"f1 / f2":""}
    result1["s"] = f1["s"] * f2["m"]
    result1["m"] = f1["m"] * f2["s"]
    result2 = {"f2 / f1":""}
    result2["s"] = f2["s"] *f1["m"]
    result2["m"] = f2["m"] * f1["s"]
    return result1,result2
def Tafrigh():
    result1={}
    result1 = {"f1 - f2":""}
    result1 ["s"] = (f1["s"]*f2["m"])-(f2["s"]*f1["m"])
    result1 ["m"] = f1["m"] *  f2["m"]
    result2={}
    result2 = {"f2 - f1":""}
    result2 ["s"] = (f2["s"]*f1["m"])-(f1["s"]*f2["m"])
    result2 ["m"] = f1["m"] *  f2["m"]
    return result1,result2
f1 = {"s":2,"m":3}
f2 = {"s":5,"m":4}

result_sum = sum()
result_multiply = multiply()
result_Taghsim = Taghsim()

result_Tafrigh = Tafrigh()
print(result_sum)
print(result_multiply)
print(result_Taghsim)
print(result_Tafrigh)

