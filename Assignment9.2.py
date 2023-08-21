def sum(t1,t2):         
    result = {}
    result["h"] = t1["h"] +t2["h"]
    result["m"] = t1["m"]+t2["m"]
    result["s"] = t1["s"]+t2["s"]
    if result["s"] >= 60:
        result["s"] -= 60
        result["m"] += 1
    if result["m"] >= 60:
        result["m"] -= 60
        result["h"] += 1
    return result
def Tafrigh():
    result={}
    result["h"] = time1["h"] - time2["h"]
    result["m"] = time1["m"] - time2["m"]
    result["s"] = time1["s"] - time2["s"]
    if result["h"] < 0:
        result["h"] = -result["h"]
    if result["m"] < 0:
        result["h"] = result["h"]-1
        result["m"]= 60 + time1["m"] - time2["m"]
    if result["s"] < 0:
        result["m"] = result["m"]-1
        result["s"]= 60 + time1["s"] - time2["s"]
    return result
def show2(result_Tafrigh):
    print("Tafrigh:",f"{result_Tafrigh['h']}:{result_Tafrigh['m']}:{result_Tafrigh['s']}")
def show1(result_sum):
    print("SUM:",f"{result_sum['h']}:{result_sum['m']}:{result_sum['s']}")
time1 = {"h":8,"m":25,"s":35}
time2 = {"h":9,"m":35,"s":20}


result_s = sum(time1,time2)
result_Tafrigh = Tafrigh()

show1(result_s)
show2(result_Tafrigh)