filepath = 'input-day1.txt'
sumOfFuel = 0

def calculateFuelForFuel(fuel):
    totalNewFuel = 0
    while(fuel > 0):
        newFuel = int(float(fuel/3))-2
        if (newFuel > 0):
            totalNewFuel += newFuel
        fuel = newFuel
    return totalNewFuel


with open(filepath) as fp:
   line = fp.readline()
   while line:
       modelFuel = int(float(line.strip())/3)-2
       sumOfFuel += modelFuel
       sumOfFuel += calculateFuelForFuel(modelFuel)
       line = fp.readline()
print sumOfFuel
