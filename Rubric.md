# Labs Prototype DS API: Rubrics

## Database Interface Rubric

The provided rubric outlines the criteria that could be used to evaluate a database interface for a
MongoDB database using the PyMongo library. The criteria includes functionality such as connecting
to the database, inserting, retrieving, updating, and deleting documents, as well as code quality,
documentation, and error handling.

1. Connecting to the database:
    - Can the interface connect to a MongoDB database using the PyMongo library and a connection string?
    - Does the interface use environment variables to store the connection string?
    - Stretch: Does the interface provide options for authentication when connecting to the database?
2. Inserting documents:
    - Can the interface insert new documents into a MongoDB collection using the insert_one method?
    - Does the interface handle errors and exceptions when inserting documents?
    - Stretch: Can the interface insert multiple documents at once using the insert_many method?
3. Retrieving documents:
    - Can the interface retrieve documents from a MongoDB collection using the find method and a query?
    - Does the interface handle errors and exceptions when retrieving documents?
    - Stretch: Can the interface retrieve documents using projection to specify which fields to include in the returned documents?
4. Updating documents:
    - Can the interface update an existing document in a MongoDB collection using the update_one method and a query?
    - Does the interface handle errors and exceptions when updating documents?
    - Stretch: Can the interface update multiple documents at once using the update_many method?
5. Deleting documents:
    - Can the interface delete a document from a MongoDB collection using the delete_one method and a query?
    - Does the interface handle errors and exceptions when deleting documents?
    - Stretch: Can the interface delete multiple documents at once using the delete_many method?
6. Code quality:
    - Does the code follow good programming practices?
    - Is the code Pythonic: idiomatic, maintainable, extensible and readable?
    - Stretch: Does the code follow SOLID principles for software engineering?
7. Documentation:
    - Does the interface provide clear and thorough documentation for its code?
    - Does the documentation include descriptions of the methods and variables, as well as examples of how to use the code?
    - Stretch: Does the documentation include information on how to install and set up the interface?
8. Error Handling:
    - Does the interface handle errors in a Pythonic manner?
    - Does the interface fail gracefully and provide the caller with information to avoid such failure in the future?
    - Stretch: Does the interface provide appropriate error messages that are clear and informative for the user?


## Machine Learning Interface Rubric

This rubric provides guidelines for writing a machine learning interface that can be used to train and deploy a machine learning model. The interface should accept input data, create and fit a model to that data, and provide methods for making predictions and saving and loading the trained model. The interface should also include appropriate documentation, error handling, and code quality practices. By following this rubric, students can ensure that their machine learning interface is well-organized, efficient, and easy to use.

1. Data input:
   - The interface should accept a DataFrame of features and a list of targets as input. 
   - The input data should be properly validated, for example by checking that the input is not empty or that the features and targets have the same length. 
   - The input data should be stored as instance variables, so that it can be used by other methods of the interface.
2. Model creation:
   - The interface should initialize a machine learning model and fit it to the input data. 
   - The model should be initialized with appropriate hyperparameters, chosen based on the characteristics of the input data and the desired model performance. 
   - The model should be trained using the fit method of the chosen machine learning library. 
   - The trained model should be stored as an instance variable, so that it can be used by other methods of the interface.
3. Prediction:
   - The interface should have a method for making predictions on new data, using the trained model. 
   - The method should accept a DataFrame of features as input and return a list of predictions. 
   - The predictions should be made using the predict method of the chosen machine learning library.
4. Saving and loading:
   - The interface should have methods for serializing and deserializing (saving and loading) the trained model to and from a file. 
   - The saving method should accept a filepath as input and use the dump function of the joblib library to serialize the model. 
   - The loading method should accept a filepath as input and use the load function of the joblib library to deserialize the model. 
   - The saving and loading methods should return the model, so that they can be used in a pipeline.
5. Code quality:
   - The interface should follow best practices for code organization and style, such as using appropriate variable and function names, and including appropriate comments and documentation. 
   - The code should be modular and reusable, with well-defined interfaces between different components. 
   - The code should be tested and debugged, to ensure that it works as expected and produces correct results.
6. Documentation:
   - The interface should have appropriate documentation, including docstrings for each method and class. 
   - The docstrings should describe the purpose and usage of each method and class, as well as the input and output types. 
   - The docstrings should follow the conventions of the chosen machine learning library and programming language.
7. Error handling:
   - The interface should include appropriate error handling, such as catching and handling exceptions that may be raised during model fitting or prediction. 
   - The error handling should include appropriate logging or notifications, to help debugging and troubleshooting. 
   - The error handling should be customized based on the specific errors that may be encountered, for example by catching different types of exceptions for different types of input errors.
