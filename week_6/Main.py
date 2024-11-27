from Math_operations.Basic_operations import arithmetic
from Math_operations.Geometry import area
       #Basic operations

print("Arithmetic Operations:")
print("5 + 3=", arithmetic.add(5, 3))
print("10 - 7=", arithmetic.substract(10, 7))
print("5 * 3=", arithmetic.multiply(5, 3))
print("8 / 2=", arithmetic.divide(8, 2))
print("8 / 0=", arithmetic.divide(8, 0)) # Test division by zero

    # Area calculations
print("\nArea Calculations:")
print("Rectangle (length=5, width=3):", area.rectangle_area(5,3))
print("Circle (radius=7):", area.circle_area(7))
print("Triangle (base=4, height=5):", area.rectangle_area(4,5))
