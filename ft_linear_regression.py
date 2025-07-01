import csv
import sys
import os.path as path
import matplotlib.pyplot as plt

class LinearRegression:
  def __init__(self, data, learning_rate = 0.1, tolerance = 0.0000001, max_iter = 1000):
    self.learning_rate = learning_rate
    self.tolerance = tolerance
    self.max_iter = max_iter
    self.theta_0 = 0.0
    self.theta_1 = 0.0
    self.normalize_values(data)
    self.mse = self.get_mean_squared_error(self.normalized_values)

  def get_predicted_estimatePrice(self, mileage):
    return (self.theta_0 + (self.theta_1 * mileage))

  def get_mean_squared_error(self, data):
    n = 0
    total = 0
    for row in data:
      y_predicted = self.get_predicted_estimatePrice(row[0])
      diff = y_predicted - row[1]
      diff *= diff
      total += diff
      n += 1
    return (total / (n))

  def normalize_values(self, data):
    tmp_mileage = [row[0] for row in data]
    tmp_price = [row[1] for row in data]

    self.min_x = min(tmp_mileage)
    self.max_x = max(tmp_mileage)
    self.min_y = min(tmp_price)
    self.max_y = max(tmp_price)

    self.normalized_values = []
    for row in data:
      x = (row[0] - self.min_x) / (self.max_x - self.min_x)
      y = (row[1] - self.min_y) / (self.max_y - self.min_y)

      self.normalized_values.append([x, y])

  def get_gradient_0(self, data):
    n = 0
    total = 0

    for row in data:
      total += self.get_predicted_estimatePrice(row[0]) - row[1]
      n += 1
    return (self.learning_rate * (total / n))

  def get_gradient_1(self, data):
    n = 0
    total = 0

    for row in data:
      total += ((self.get_predicted_estimatePrice(row[0]) - row[1]) * row[0])
      n += 1
    return (self.learning_rate * (total / n))

  def linear_regression(self):
    n = 0
    delta_mse = self.mse

    while n < self.max_iter and delta_mse > self.tolerance:
      gradient0 = self.get_gradient_0(self.normalized_values)
      gradient1 = self.get_gradient_1(self.normalized_values)
      self.theta_0 -= gradient0
      self.theta_1 -= gradient1
      previous_mse = self.mse
      self.mse = self.get_mean_squared_error(self.normalized_values)
      delta_mse = abs(self.mse - previous_mse)
      n += 1
    self.theta_1 = (self.max_y - self.min_y) * self.theta_1 / \
            (self.max_x - self.min_x)
    self.theta_0 = self.min_y + ((self.max_y - self.min_y) * \
            self.theta_0) + self.theta_1 * (1 - self.min_x)
    self.save_thetas()

  def save_thetas(self):
    try:
      with open("thetas.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["theta_0", "theta_1"])
        writer.writerow([self.theta_0, self.theta_1])
    except Exception as e:
      sys.exit(f"Error: {e}")

  def evaluate_model(self, data):
    n = len(data)
    mse = 0
    mae = 0
    ss_total = 0
    ss_regression = 0

    tmp_y = [row[1] for row in data]
    y_mean = sum(tmp_y) / n

    for row in data:
      x = row[0]
      y = row[1]
      y_predicted = self.theta_0 + (self.theta_1 * x)
      error = y_predicted - y
      mse += error ** 2
      mae += abs(error)
      ss_total += (y - y_mean) ** 2
      ss_regression += error ** 2

    mse = mse / n
    mae = mae / n
    rmse = mse ** 0.5
    r_squared = 1 - (ss_regression / ss_total)
    rmse_ratio = rmse / y_mean

    print(f"Mean squared error: {mse} (lower is better)")
    print(f"Root Mean Squared Error: {rmse} (lower is better)")
    print(f"RMSE is {rmse_ratio * 100:.2f}% of the mean actual value (<20% is ideal)")
    print(f"Mean Absolute Error: {mae} (lower is better)")
    print(f"R²: {r_squared} (closer to 1 is better)")

def get_data_from_file(filename):
  data = []
  try:
    if not path.isfile(filename):
      raise Exception(f"File not found: {filename}")
    if not filename.lower().endswith('.csv'):
      raise Exception("File must be a .csv")
    with open(filename, 'r') as file:
      reader = csv.reader(file)
      next(reader)
      for row in reader:
        if (len(row) != 2):
          raise Exception(f"{filename} is not properly formatted")
        data.append([float(row[0]), float(row[1])])
      if (len(data) == 0):
        raise Exception("dataset is empty")
      if (len(data) == 1):
        raise Exception("dataset contains only a pair of values")
  except Exception as e:
    sys.exit(f"Error: {e}")
  return data

def plot_data_and_regression_line(self, data):
    x_vals = [row[0] for row in data]
    y_vals = [row[1] for row in data]

    min_x = min(x_vals)
    max_x = max(x_vals)

    line_x = [min_x, max_x]
    line_y = [self.theta_0 + self.theta_1 * min_x,
              self.theta_0 + self.theta_1 * max_x]

    plt.scatter(x_vals, y_vals, color='blue', label='Data points')
    plt.plot(line_x, line_y, color='red', label='Regression line')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Linear Regression Result')
    plt.legend()
    plt.show()

def main():
  if (len(sys.argv) < 2):
    filename = input("Enter the filename of the dataset used for training: ")
  else:
    filename = sys.argv[1]
  data = get_data_from_file(filename)
  model = LinearRegression(data)
  model.linear_regression()
  model.evaluate_model(data)
  plot_data_and_regression_line(model, data)


if __name__ == "__main__":
  main()
