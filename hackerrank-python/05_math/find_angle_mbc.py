

import math

side_ab = int(input())

side_bc = int(input())

radian = math.atan(side_ab/side_bc)
degrees = round(math.degrees(radian))

print(f"{degrees}\u00B0")



