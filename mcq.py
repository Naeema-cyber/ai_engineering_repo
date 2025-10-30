{
  "mcqs": {
    "User Authentication and Authorization in FastAPI": {
      "Authentication and Authorization": [
        {
          "title": "User Authentication and Authorization in FastAPI - Quiz",
          "description": "Test your knowledge of user authentication and authorization concepts in FastAPI.",
          "questions": [
            {
              "question": "Why is user authentication essential in backend systems?",
              "options": [
                "To improve the visual appeal of the application.",
                "To ensure only authorized users can access specific resources and functionalities.",
                "To reduce the server load.",
                "To simplify the codebase."
              ],
              "answer": "To ensure only authorized users can access specific resources and functionalities.",
              "difficulty": "Beginner"
            },
            {
              "question": "Which of the following is a secure method for storing passwords?",
              "options": [
                "Storing passwords in plain text.",
                "Storing passwords using simple encryption.",
                "Storing passwords using hashing algorithms like bcrypt.",
                "Storing passwords in a publicly accessible file."
              ],
              "answer": "Storing passwords using hashing algorithms like bcrypt.",
              "difficulty": "Beginner"
            },
            {
              "question": "What is a JSON Web Token (JWT) used for?",
              "options": [
                "To store user passwords.",
                "To manage user sessions and authenticate requests.",
                "To define the database schema.",
                "To style the user interface."
              ],
              "answer": "To manage user sessions and authenticate requests.",
              "difficulty": "Beginner"
            },
            {
              "question": "In the context of authentication, what does 'login functionality' typically involve?",
              "options": [
                "Creating a new user account.",
                "Verifying user credentials and generating a session token.",
                "Deleting a user account.",
                "Resetting a user's password."
              ],
              "answer": "Verifying user credentials and generating a session token.",
              "difficulty": "Beginner"
            },
            {
              "question": "How can you protect API endpoints using token-based authentication?",
              "options": [
                "By making the API endpoints publicly accessible.",
                "By requiring a valid token in the request headers to access the endpoint.",
                "By encrypting the entire API.",
                "By hiding the API endpoints from the user."
              ],
              "answer": "By requiring a valid token in the request headers to access the endpoint.",
              "difficulty": "Intermediate"
            },
            {
              "question": "What is OAuth2 primarily used for?",
              "options": [
                "Encrypting data in the database.",
                "Managing access control and authorization for authenticated users.",
                "Creating user interfaces.",
                "Optimizing database queries."
              ],
              "answer": "Managing access control and authorization for authenticated users.",
              "difficulty": "Intermediate"
            },
            {
              "question": "How can FastAPI's dependency system be used with OAuth2?",
              "options": [
                "To automatically generate API documentation.",
                "To inject dependencies for authentication and authorization, simplifying access control.",
                "To manage database connections.",
                "To handle error logging."
              ],
              "answer": "To inject dependencies for authentication and authorization, simplifying access control.",
              "difficulty": "Intermediate"
            },
            {
              "question": "What is the purpose of retrieving the authenticated user's profile?",
              "options": [
                "To display the user's name on the screen.",
                "To access user-specific data and personalize the application experience.",
                "To track user activity.",
                "To send promotional emails."
              ],
              "answer": "To access user-specific data and personalize the application experience.",
              "difficulty": "Intermediate"
            },
            {
              "question": "Why is it important to restrict access to protected routes?",
              "options": [
                "To make the application more complex.",
                "To ensure that only authorized users can access sensitive data and functionalities.",
                "To improve the application's performance.",
                "To reduce the amount of code needed."
              ],
              "answer": "To ensure that only authorized users can access sensitive data and functionalities.",
              "difficulty": "Intermediate"
            },
            {
              "question": "Which of the following is a common header used to send a JWT?",
              "options": [
                "Content-Type",
                "Authorization",
                "User-Agent",
                "Accept"
              ],
              "answer": "Authorization",
              "difficulty": "Beginner"
            },
            {
              "question": "What does the term 'scope' refer to in the context of OAuth2?",
              "options": [
                "The size of the database.",
                "The permissions granted to an application to access a user's data.",
                "The programming language used.",
                "The number of users in the system."
              ],
              "answer": "The permissions granted to an application to access a user's data.",
              "difficulty": "Intermediate"
            },
            {
              "question": "What is the role of a 'client' in OAuth2?",
              "options": [
                "The server that hosts the API.",
                "An application requesting access to a user's data on a resource server.",
                "The user accessing the application.",
                "The database used by the application."
              ],
              "answer": "An application requesting access to a user's data on a resource server.",
              "difficulty": "Intermediate"
            },
            {
              "question": "What is a 'resource server' in OAuth2?",
              "options": [
                "The server that authenticates the user.",
                "The server that hosts the protected resources and verifies the access token.",
                "The client application.",
                "The database server."
              ],
              "answer": "The server that hosts the protected resources and verifies the access token.",
              "difficulty": "Intermediate"
            },
            {
              "question": "What is the purpose of a 'refresh token' in OAuth2?",
              "options": [
                "To immediately grant access to resources.",
                "To obtain a new access token without requiring the user to re-authenticate.",
                "To revoke access to resources.",
                "To encrypt the access token."
              ],
              "answer": "To obtain a new access token without requiring the user to re-authenticate.",
              "difficulty": "Advanced"
            },
            {
              "question": "Which FastAPI security dependency is commonly used for handling OAuth2?",
              "options": [
                "HTTPBasic",
                "HTTPDigest",
                "OAuth2PasswordBearer",
                "APIKeyHeader"
              ],
              "answer": "OAuth2PasswordBearer",
              "difficulty": "Intermediate"
            }
          ]
        }
      ]
    }
  }
}


{
  "mcqs": {
    "Relational Databases and MySQL Fundamentals": {
      "Database Basics and SQL": [
        {
          "title": "Relational Databases and MySQL Fundamentals - Quiz",
          "description": "Test your knowledge of relational databases and basic SQL operations.",
          "questions": [
            {
              "question": "What is a relational database?",
              "options": [
                "A database that stores data in a hierarchical structure.",
                "A database that stores data in tables with rows and columns.",
                "A database that stores data in a single file.",
                "A database that only stores images."
              ],
              "answer": "A database that stores data in tables with rows and columns.",
              "difficulty": "Beginner"
            },
            {
              "question": "Which of the following is NOT a key concept in relational databases?",
              "options": [
                "Tables",
                "Rows",
                "Columns",
                "Linked Lists"
              ],
              "answer": "Linked Lists",
              "difficulty": "Beginner"
            },
            {
              "question": "What is a primary key?",
              "options": [
                "A key that unlocks the database.",
                "A unique identifier for each row in a table.",
                "A key used for sorting data.",
                "A key used for encrypting data."
              ],
              "answer": "A unique identifier for each row in a table.",
              "difficulty": "Beginner"
            },
            {
              "question": "What is a foreign key?",
              "options": [
                "A key from a different database.",
                "A key that references the primary key of another table.",
                "A key used for searching data.",
                "A key used for backing up data."
              ],
              "answer": "A key that references the primary key of another table.",
              "difficulty": "Beginner"
            },
            {
              "question": "Which SQL command is used to create a new table?",
              "options": [
                "INSERT",
                "SELECT",
                "CREATE",
                "UPDATE"
              ],
              "answer": "CREATE",
              "difficulty": "Beginner"
            },
            {
              "question": "Which SQL command is used to add new data to a table?",
              "options": [
                "SELECT",
                "UPDATE",
                "DELETE",
                "INSERT"
              ],
              "answer": "INSERT",
              "difficulty": "Beginner"
            },
            {
              "question": "Which SQL command is used to retrieve data from a table?",
              "options": [
                "CREATE",
                "INSERT",
                "SELECT",
                "DELETE"
              ],
              "answer": "SELECT",
              "difficulty": "Beginner"
            },
            {
              "question": "Which SQL command is used to modify existing data in a table?",
              "options": [
                "INSERT",
                "DELETE",
                "UPDATE",
                "CREATE"
              ],
              "answer": "UPDATE",
              "difficulty": "Beginner"
            },
            {
              "question": "Which SQL command is used to remove data from a table?",
              "options": [
                "UPDATE",
                "SELECT",
                "DELETE",
                "CREATE"
              ],
              "answer": "DELETE",
              "difficulty": "Beginner"
            },
            {
              "question": "Why are relational databases useful?",
              "options": [
                "They are difficult to manage.",
                "They ensure data integrity and consistency.",
                "They are only useful for small datasets.",
                "They are not scalable."
              ],
              "answer": "They ensure data integrity and consistency.",
              "difficulty": "Beginner"
            },
            {
              "question": "In MySQL Workbench, what is the purpose of the SQL editor?",
              "options": [
                "To design the user interface.",
                "To write and execute SQL queries.",
                "To manage server settings.",
                "To create database backups."
              ],
              "answer": "To write and execute SQL queries.",
              "difficulty": "Beginner"
            },
            {
              "question": "What is the purpose of defining data types for columns in a table?",
              "options": [
                "To make the table look nicer.",
                "To ensure data consistency and validity.",
                "To speed up data retrieval.",
                "To reduce the size of the database."
              ],
              "answer": "To ensure data consistency and validity.",
              "difficulty": "Beginner"
            },
            {
              "question": "Which of the following data types is suitable for storing whole numbers in MySQL?",
              "options": [
                "VARCHAR",
                "TEXT",
                "INT",
                "DATE"
              ],
              "answer": "INT",
              "difficulty": "Beginner"
            },
            {
              "question": "Which of the following data types is suitable for storing text strings in MySQL?",
              "options": [
                "INT",
                "DATE",
                "BOOLEAN",
                "VARCHAR"
              ],
              "answer": "VARCHAR",
              "difficulty": "Beginner"
            },
            {
              "question": "What is the purpose of using `WHERE` clause in a `SELECT` statement?",
              "options": [
                "To specify the columns to retrieve.",
                "To filter the rows based on a condition.",
                "To sort the results.",
                "To group the results."
              ],
              "answer": "To filter the rows based on a condition.",
              "difficulty": "Beginner"
            }
          ]
        }
      ]
    }
  }
}

{
  "mcqs": {
    "SQLAlchemy and FastAPI Integration": {
      "Core Concepts and CRUD Operations": [
        {
          "title": "SQLAlchemy and FastAPI Integration - Quiz",
          "description": "Test your knowledge of SQLAlchemy, FastAPI, and their integration for database operations.",
          "questions": [
            {
              "question": "What is SQLAlchemy primarily used for?",
              "options": [
                "Creating user interfaces.",
                "Handling HTTP requests in Python.",
                "Providing an ORM for interacting with databases.",
                "Managing server infrastructure."
              ],
              "answer": "Providing an ORM for interacting with databases.",
              "difficulty": "Beginner"
            },
            {
              "question": "What does ORM stand for in the context of SQLAlchemy?",
              "options": [
                "Object Relational Mapping",
                "Object Rendering Model",
                "Operational Resource Management",
                "Object Request Manager"
              ],
              "answer": "Object Relational Mapping",
              "difficulty": "Beginner"
            },
            {
              "question": "Which of the following is NOT a benefit of using an ORM like SQLAlchemy?",
              "options": [
                "Increased code readability.",
                "Database abstraction.",
                "Automatic SQL injection prevention.",
                "Direct SQL query execution."
              ],
              "answer": "Direct SQL query execution.",
              "difficulty": "Intermediate"
            },
            {
              "question": "How does SQLAlchemy connect to a database?",
              "options": [
                "Through a connection string.",
                "By directly embedding the database file.",
                "Via a web browser interface.",
                "Using a proprietary API."
              ],
              "answer": "Through a connection string.",
              "difficulty": "Beginner"
            },
            {
              "question": "In SQLAlchemy, what is a `Model`?",
              "options": [
                "A representation of a database table as a Python class.",
                "A function for handling HTTP requests.",
                "A configuration file for the database.",
                "A tool for visualizing database schemas."
              ],
              "answer": "A representation of a database table as a Python class.",
              "difficulty": "Beginner"
            },
            {
              "question": "What is the purpose of `Base` in SQLAlchemy?",
              "options": [
                "It's the base class for all database models.",
                "It's a function for creating database connections.",
                "It's a decorator for defining API endpoints.",
                "It's a tool for managing database migrations."
              ],
              "answer": "It's the base class for all database models.",
              "difficulty": "Intermediate"
            },
            {
              "question": "Which of the following is a valid CRUD operation?",
              "options": [
                "Compile",
                "Refactor",
                "Update",
                "Deploy"
              ],
              "answer": "Update",
              "difficulty": "Beginner"
            },
            {
              "question": "In FastAPI, how do you typically access the database session?",
              "options": [
                "Through global variables.",
                "By directly importing the database connection.",
                "Using dependency injection.",
                "By creating a new session for each request."
              ],
              "answer": "Using dependency injection.",
              "difficulty": "Intermediate"
            },
            {
              "question": "Which HTTP method is typically used for creating a new resource in a RESTful API?",
              "options": [
                "GET",
                "PUT",
                "POST",
                "DELETE"
              ],
              "answer": "POST",
              "difficulty": "Beginner"
            },
            {
              "question": "Which HTTP method is typically used for retrieving a resource in a RESTful API?",
              "options": [
                "POST",
                "PUT",
                "GET",
                "DELETE"
              ],
              "answer": "GET",
              "difficulty": "Beginner"
            },
            {
              "question": "Which HTTP method is typically used for updating an existing resource in a RESTful API?",
              "options": [
                "POST",
                "PATCH",
                "GET",
                "DELETE"
              ],
              "answer": "PATCH",
              "difficulty": "Intermediate"
            },
             {
              "question": "Which HTTP method is typically used for deleting a resource in a RESTful API?",
              "options": [
                "POST",
                "PUT",
                "GET",
                "DELETE"
              ],
              "answer": "DELETE",
              "difficulty": "Beginner"
            },
            {
              "question": "What is the purpose of `db.add(instance)` in SQLAlchemy?",
              "options": [
                "To delete an instance from the database.",
                "To add a new instance to the database session.",
                "To update an existing instance in the database.",
                "To query the database for an instance."
              ],
              "answer": "To add a new instance to the database session.",
              "difficulty": "Beginner"
            },
            {
              "question": "What does `db.commit()` do in SQLAlchemy?",
              "options": [
                "It rolls back the current transaction.",
                "It saves the changes made in the session to the database.",
                "It closes the database connection.",
                "It starts a new transaction."
              ],
              "answer": "It saves the changes made in the session to the database.",
              "difficulty": "Beginner"
            },
            {
              "question": "What is the purpose of using `async def` when defining FastAPI routes that interact with a database?",
              "options": [
                "To make the route run faster.",
                "To enable asynchronous database operations, preventing blocking.",
                "To automatically generate API documentation.",
                "To simplify error handling."
              ],
              "answer": "To enable asynchronous database operations, preventing blocking.",
              "difficulty": "Advanced"
            }
          ]
        }
      ]
    }
  }
}