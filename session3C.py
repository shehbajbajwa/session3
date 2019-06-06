#logical operators
physics = 70
chemistry = 90
maths = 80

print("can student be an engineer?", (maths>physics and maths>chemistry))
print("can student be an  physist?", (physics>maths  or  physics>chemistry))