# selling-car-price-prediction-model
## WELCOME TO MY MACHINE LEARNING PROJECT 

* This project involves creating a machine learning model to predict the selling price of a second-hand car based on various input features. The project includes both a backend (machine learning model) and a frontend (Graphical User Interface using Tkinter).
* The prediction can be done with the help of multivariate regression model.Multivariate regression tries to find out a formula that can explain how factors in variables respond simultaneously to changes in others.
### library used:
  1. **Pandas**:
     pandas is a powerful data manipulation and analysis library for Python. It provides data structures like DataFrame and Series that are flexible and easy to use.
     
     * Usage in the Project:
     Loading Data: Used to read the CSV file containing the car data.
     Data Manipulation: Used to drop unnecessary columns and manipulate the dataset for machine learning.
     
  3. **Numpy**:
     numpy is a fundamental package for numerical computing in Python. It provides support for arrays, matrices, and many mathematical functions to operate on these data structures.

      * Usage in the Project:
     Data Manipulation: Often used for mathematical operations and handling arrays, although not explicitly used in the provided code, it is typically used alongside pandas and scikit-learn.
     
  5. **scikit-learn** (sklearn):
     scikit-learn is a popular machine learning library in Python. It provides simple and efficient tools for data mining and data analysis.

      Usage in the Project:
      * linear_model.LinearRegression: Used to create and train a linear regression model.
      * preprocessing.LabelEncoder: Used to convert categorical data into numerical format, which is necessary for machine learning models.
     
  7. **Tkinter**:
    tkinter is the standard GUI (Graphical User Interface) library for Python. It provides tools to create and manage GUI applications.
   
      Usage in the Project:
      * tk: Used as the main module to create the GUI application window and widgets.
      * messagebox: Used to show message boxes, which display information or error messages to the user.
      * ttk: Provides themed widgets that offer a more modern look and feel compared to the standard Tkinter widgets.


>[!NOTE]
>Download the dataset <cardata.csv> and code <carprice.py> in the same folder.

  
* Load and Prepare Data: Load the dataset, drop unnecessary columns, encode categorical features, and prepare the final set of features.
* Train the Model: Train a linear regression model using the prepared features and target variable.
* Build the GUI: Create a user interface with labels, entry fields, and buttons using Tkinter. Include functions to display the dataset and predict the selling price.
* Interactive Predictions: Allow users to input car details and get a predicted selling price.


![image](https://github.com/nandanaap/selling-car-price-prediction-model/assets/139910211/51890a84-97d6-420b-8ff6-c358e61b8985)
