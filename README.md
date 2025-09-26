Flask REST API — User Management

This project demonstrates how to build a simple REST API using Flask to manage user data. The main objective of the project is to understand and implement the fundamentals of REST API development. The API provides basic CRUD operations such as creating, reading, updating, and deleting users, with the data stored in an in-memory dictionary for simplicity.

The project uses Python and Flask, and you can test the endpoints using Postman or Curl. Once you clone the repository and install the required dependencies with pip install flask, you can run the app using python app.py. The API supports multiple routes: GET to fetch all users or a specific user by ID, POST to create new users, PUT to update existing users, and DELETE to remove users. For example, sending a POST request to /users with a JSON body containing name and email will create a new user, while a PUT request to /users/<id> will allow you to update the user details.

By building this project, I practiced creating endpoints with Flask, handling different HTTP methods, and working with JSON data. This task gave me a solid understanding of how REST APIs work and how they can be tested with tools like Postman or Curl. Overall, the outcome of this project is a strong foundation in API development fundamentals.
