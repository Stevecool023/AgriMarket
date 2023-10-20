AgriMarket Command Interpreter

## Description

AgriMarket is a command-line tool for managing our Agricultural website's data. It provides a command interpreter that allows us to create, retrieve, update, and destroy objects related to the website. It offers a flexible storage system to store and persist objects to a JSON file. This project serves as a foundation for the AgriMarket web application.

## Command Interpreter

The command interpreter allows one to interact with AgriMarket objects using the provided commands. It provides an abstraction between the objects and their storage, making it easy to manipulate data without worrying about the underlying storage mechanism.

## Getting Started

To start the AgriMarket Command Interpreter, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Stevecool023/agrimarket.git

2. Navigate to the project directory:

   cd AgriMarket_back-end

3. Start the command interpreter:

./console.py


Usage
The command interpreter supports various commands to manage objects. Here are some examples:

create <class_name>: Create a new object of the specified class.
show <class_name> <object_id>: Display information about a specific object.
update <class_name> <object_id> <attribute_name> "<new_value>": Update an object's attribute.
all <class_name>: List all objects of the specified class.
destroy <class_name> <object_id>: Delete an object.
quit: Exit the command interpreter.
For detailed usage examples, refer to the Examples section below.


Examples
1. Create a new User:
   (AgriMarket_back-end) create User

2. Update the name of a User:
   (AgriMarket_back-end) update User 1 name "John Doe"

3. Show information about a Product:
   (AgriMarket_back-end) show Product 42

4. List all Equipment:
   (AgriMarket_back-end) all Equipment.
