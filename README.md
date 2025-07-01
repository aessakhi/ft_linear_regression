# ft_linear_regression

## Goal

Create an univariate linear regression model using gradient descent to predict the price of a car based on its mileage

## Usage

python3 ft_linear_regression.py - Requires a properly formated .csv file with two rows - Will generate a thetas.csv file as a result which will be used by prediction.py

python3 prediction.py - Prints the estimated price of a car based on its mileage. 0 if no thetas.csv file is provided.

## References

Pour les articles qui m'ont le plus servi pour ft_linear_regression

Intro:
- https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent?hl=fr

Gradient descent implementation:
- https://ompramod.medium.com/mastering-gradient-descent-optimizing-neural-networks-with-precision-cbea71d236cf (check the end of the article to avoid a common mistake in the implementation)
- https://medium.com/@lachlanmiller_52885/machine-learning-week-1-cost-function-gradient-descent-and-univariate-linear-regression-8f5fe69815fd
- https://www.geeksforgeeks.org/python/univariate-linear-regression-in-python/
- https://aayushmaan1306.medium.com/univariate-linear-regression-46ece0dfc4e7

Convergence/End of gradient loop:
- https://stackoverflow.com/questions/36805834/what-determines-whether-my-python-gradient-descent-algorithm-converges
- https://medium.com/latinxinai/gradient-decent-ab782c96daeb (Juste la partie "Convergence Stopping Criterion
")

Normalization of data:
- https://developers.google.com/machine-learning/crash-course/numerical-data/normalization?hl=fr
- https://www.geeksforgeeks.org/machine-learning/when-to-normalize-data-in-regression/

Evaluation of the model:
- https://medium.com/@cmukesh8688/evaluation-of-linear-regression-model-6e8edbb068f
