# AirBnB Clone Project

## Description

The AirBnB Clone project is a command-line interface (CLI) that serves as the first step towards building a full web application. The CLI allows users to manage AirBnB objects, including creating new objects, retrieving objects, performing operations on objects, updating object attributes, and destroying objects. The project involves creating Python classes for AirBnB objects, implementing a storage engine for persistence, and building a command interpreter using the `cmd` module.

## Command Interpreter

### How to Start

To start the AirBnB Clone command interpreter, run the `console.py` script located in the project's root directory:

```bash
$ ./console.py

###How to Use

Once the command interpreter is running, you can enter commands at the prompt. The available commands include:

create: Create a new AirBnB object.

show: Retrieve and display information about a specific object.

destroy: Remove an object from the storage.

all: Display information about all stored objects or objects of a specific type.

update: Update the attributes of an object.

Additionally, you can use the help command to see a list of available commands and their descriptions.

###Examples

$ ./console.py
(hbnb) create User
62010b85-7b2f-4f0c-830b-ebe5f55d515d
(hbnb) show User 62010b85-7b2f-4f0c-830b-ebe5f55d515d
[User] (62010b85-7b2f-4f0c-830b-ebe5f55d515d) {'id': '62010b85-7b2f-4f0c-830b-ebe5f55d515d', 'created_at': '2023-10-10T12:00:00', 'updated_at': '2023-10-10T12:00:00'}
(hbnb) all
["[User] (62010b85-7b2f-4f0c-830b-ebe5f55d515d) {'id': '62010b85-7b2f-4f0c-830b-ebe5f55d515d', 'created_at': '2023-10-10T12:00:00', 'updated_at': '2023-10-10T12:00:00'}"]
(hbnb) quit
