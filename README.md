## Notes

The main objective of this problem is to make buying the insurance simpler. In order to do that we need to provide a quote to the customers in an quick and efficient manner.

There are few points important to note
- The problem statement is bit unclear. Initially, I was asked to predict the quote, but then I was asked to predict BMI in the problem objective. There is no need to train any model to determine BMI because it is simply a calculated column. As a reason, I assumed the problem was to predicting the quote.
- However, some business rules are already given to calculate the quote, thus we do not need to train any machine learning model to predict it here. These rules were incorporated a function that was used to find the quote.
- In the notebook I've done a short analysis on the given dataset.


## Setup Instructions

- Make sure you have pyenv & pipenv 
  ```
  brew install pyenv
  pyenv install 3.9.0
  pyenv local 3.9.0
  python3 -m pip install pipenv
  ```

## Run tests

- To run the unittests
  ```
  python -m unittest tests/test_calc_bmi.py
  python -m unittest tests/test_calc_quote.py
  ```
 
 ## Usage

- To run the application
  ```
  python3 scripts/main.py -predict <age> <gender> <height> <weight> <discount>

  Example
  python3 scripts/main.py -predict 34 Male 510 185 10
  ```
 
## Steps to operationalize

As I didn't have much time I skipped these steps

- We can use libraries such as `isort`, `black`, `flake8` to maintain proper python code formatting.
- Write integration tests and also ensure that the test coverage is more than 90%.
- Use docker to build the image.
- Use jenkins to build the CI/CD pipeline.
