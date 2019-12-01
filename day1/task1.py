filepath = 'input-day1.txt'
sumOfFuel = 0;

with open(filepath) as fp:
   line = fp.readline()
   while line:
       sumOfFuel += int(float(line.strip())/3)-2
       line = fp.readline()
print sumOfFuel
