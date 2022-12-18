# Labs Prototype DS API
This project is a prototype for a machine learning (ML) API built using the FastAPI framework. The goal of the project is to build key features for the API, including a database component and an ML model component. The suggested technology stack for this project includes FastAPI, MongoDB, and Scikit.

The project will be completed in four sprints, each with its own set of tasks. During the first sprint (Setup), the team will set up their local development environment by installing necessary software and packages, and will hold a planning session to discuss and plan the project.

In the second sprint (Build), the team will set up the database and create the necessary tables and schema, collect and generate data for use in the ML model, and integrate the database component into the application, including creating any necessary API endpoints.

In the third sprint (Build), the team will build and train the ML model on the collected data, serialize the trained model to make it easier to load and use for predictions, and integrate the ML model component into the application, including creating any necessary API endpoints.

In the fourth and final sprint (Share), the team will analyze the results of the ML model and make any necessary improvements, deploy the ML API to a production environment, and wrap up the project with a final presentation or review.

The project will also have a few required components, including an application interface, an ML model, and a database interface. To set up your local environment, you will create a virtual environment, install the necessary requirements, and start the local server. Additionally, the project will use environment variables stored in a `.env` file. See below for details.

As possible stretch goals, you may also implement data validation with Pydantic, refactor the API endpoints into routers, and/or implement authentication for the API.

---
## Data Science Labs Journey

### Sprint 1 (Setup)
- Local setup: Setting up the local development environment, including installing necessary software and packages.
- Planning Session: Meeting to discuss and plan the project, including deciding on the database and machine learning model to use.

### Sprint 2 (Build I)
- Database Component: Setting up the database and creating the necessary tables and schema.
  - Signup for a MongoDB account or another database service. 
- Generate Data: Collecting and generating data to be used in the machine learning model.
  - This may require creating a new script for generating data.
- App Integration: Integrating the database component into the application, 
  - This may require adding or modifying API endpoints.

### Sprint 3 (Build II)
- Machine Learning Model Component: Build and train the machine learning model on the generated data.
  - Make sure you are training the model on the datat in the database.
- JobLib: Serialize the trained model, allowing it to be used for predictions in the cloud.
- App Integration: Integrate the machine learning model component into the application.
  - This may require adding or modifying API endpoints.

### Sprint 4 (Share)
- Analyze: Validate the results of the machine learning model and making any necessary improvements.
- Deploy: Register for an account at PythonAnywhere and deploy your machine learning API.
- Defend: Wrap up the project with a final presentation.

---
### Required Components
- Application Interface
- Machine Learning Model
- Database Interface

### Local Setup
1. Create Virtual Environment
2. Install Requirements & Environment Variables
3. Start Local Server

### Environment Variables
- Create a `.env` file and copy and paste the following environment variable into the file.
  - `FERNET_KEY=TUP5lxgpBU5Dvl5sMOpf2w0-2T8DhCIekAyho2Ob_5w=`
- You may need additional environment variables for connecting to your database.

### Stretch Goals
- Implement Data Validation with Pydantic
- Refactor the API endpoints into routers
- Implement Authentication for the API
