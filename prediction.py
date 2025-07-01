import csv
import sys
import os.path as path

theta0 = 0
theta1 = 0
if path.isfile('thetas.csv'):
  try:
    with open('thetas.csv', 'r') as file:
      reader = csv.reader(file)
      next(reader)
      row = next(reader)
      theta0 = float(row[0])
      theta1 = float(row[1])
  except Exception as e:
    sys.exit(f"Error: {e}")
mileageInput = input("Enter the car's mileage: ")
try:
  mileage = float(mileageInput)
  if mileage < 0:
    raise Exception("mileage cannot be negative")
except ValueError:
  sys.exit("Error: mileage must a number")
except Exception as e:
  sys.exit(f"Error: {e}")
print("Estimated price:", theta0 + (theta1 * mileage))
