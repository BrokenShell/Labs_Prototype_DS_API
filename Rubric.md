# Labs Prototype DS API: Rubrics

## Database Interface Rubric

The provided rubric outlines the criteria that could be used to evaluate a database interface for a
MongoDB database using the PyMongo library. The criteria includes functionality such as connecting
to the database, inserting, retrieving, updating, and deleting documents, as well as code quality,
documentation, and error handling.

1. Connecting to the database
    - Can the interface connect to a MongoDB database using the PyMongo library and a connection
      string?
    - Does the interface use environment variables to store the connection string?
    - Stretch: Does the interface provide options for authentication when connecting to the
      database?
2. Inserting documents
    - Can the interface insert new documents into a MongoDB collection using the insert_one method?
    - Does the interface handle errors and exceptions when inserting documents?
    - Stretch: Can the interface insert multiple documents at once using the insert_many method?
3. Retrieving documents
    - Can the interface retrieve documents from a MongoDB collection using the find method and a
      query?
    - Does the interface handle errors and exceptions when retrieving documents?
    - Stretch: Can the interface retrieve documents using projection to specify which fields to
      include in the returned documents?
4. Updating documents
    - Can the interface update an existing document in a MongoDB collection using the update_one
      method and a query?
    - Does the interface handle errors and exceptions when updating documents?
    - Stretch: Can the interface update multiple documents at once using the update_many method?
5. Deleting documents
    - Can the interface delete a document from a MongoDB collection using the delete_one method and
      a query?
    - Does the interface handle errors and exceptions when deleting documents?
    - Stretch: Can the interface delete multiple documents at once using the delete_many method?
6. Code quality
    - Does the code follow good programming practices?
    - Is the code Pythonic: idiomatic, maintainable, extensible and readable?
    - Stretch: Does the code follow SOLID principles for software engineering?
7. Documentation
    - Does the interface provide clear and thorough documentation for its code?
    - Does the documentation include descriptions of the methods and variables, as well as examples
      of how to use the code?
    - Stretch: Does the documentation include information on how to install and set up the
      interface?
8. Error Handling
    - Does the interface handle errors in a Pythonic manner?
    - Does the interface fail gracefully and provide the caller with information to avoid such
      failure in the future?
    - Stretch: Does the interface provide appropriate error messages that are clear and informative
      for the user?
