from numpy import sqrt

def Quad_Formula(a,b,c):
    delta=sqrt(b**2-4*a*c)
    print((-b+delta)/(2*a))
    print((-b-delta)/(2*a))
    return [(-b+delta)/(2*a),(-b-delta)/(2*a)]
    
def Var_Quad_Formula(a,b,c):
    delta=sqrt(b**2-4*a*c)
    print((2*c)/(-b-delta))
    print((2*c)/(-b+delta))
    return [(2*c)/(-b-delta),(2*c)/(-b+delta)]

print(Quad_Formula(0.001,1000,0.001))    
print(Var_Quad_Formula(0.001,1000,0.001))

