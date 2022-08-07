<h1><img src="images/hbnb img.png" alt="logo python" width="650" height="270"><br/><b>0x00. AirBnB clone - The console</b></h1>

[![contribuitors](https://img.shields.io/github/contributors/cbarros7/AirBnB_clone?style=plastic)](https://github.com/cbarros7/AirBnB_clone/graphs/contributors)
[![lisence](https://img.shields.io/github/license/Nonyfuego/AirBnB_clone?style=plastic)](https://github.com/Nonyfuego/AirBnB_clone/blob/main/LICENSE.md)
[![plattaforms](https://img.shields.io/powershellgallery/p/DNS.1.1.1.1?color=%23EF7F1A&style=plastic)](https://www.powershellgallery.com/packages/DNS.1.1.1.1/0.0.7)
[![python version](https://img.shields.io/pypi/pyversions/3?color=%23EF7F1A&style=plastic)](https://www.python.org/download/releases/3.0/)

[![Twitter Nony](https://img.shields.io/twitter/follow/nonyfuego?label=NonyNzekwe&style=social)](https://twitter.com/nonyfuego)
[![Twitter vicky](https://img.shields.io/twitter/follow/tori_etim?label=VickyEtim&style=social)](https://twitter.com/tori_etim)

## **Background Context**
## **First step: Write a command interpreter to manage your AirBnB objects.**
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## **What’s a command interpreter?**
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## **Resources**
Read or watch: [cmd module](https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw), [packages](https://intranet.hbtn.io/rltoken/jKl9WFpKA-fPt7_guv9_3Q), [uuid module](https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g), [datetime](https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q), [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g), [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg), [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A)

### **Requirements Python Scripts**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7 or more)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").-MyClass.my_function.__doc__)')

### **Requirements Python Unit Tests**
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# HOW WORK THE CONSOL

## Steep for test the console
### 1. Clone the repository with HTTPS:
```
$ git clone https://github.com/nonyfuego/AirBnB_clone.git
```
### 2. Go to folder AirBnB_clone
```
$ cd AirBnB_clone
```
### 3. Run the consol file
```
$ ./console.py
```
Alfter in you screen can show the prompt of the terminal:
```
(hbnb)
```

## Command for test the console
the command that you can type are:
- help ó ?: this show the help avalible for command and the commands.
```
(hbnb)?

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
- **EOF** and **quit**: this commands are for exit the console, the EOF is the signal get to press the key combination Ctrl + d
```
(hbnb)quit
❯

  ~/holberton/AirBnB_clone   main ·········  07:48:50 PM ─╮
❯
```
- **create**: you can create an instane of the class that you want. The command is ***create "class name" or "class name". create()***, if the instance is create correcty it is saved and in screen console show you the ***id*** for instance created. The clas avalible are
   - BaseModel
   - Place
   - User
   - Amenity
   - City
   - State
   - Review
```
(hbnb)create Place
93d823aa-f03a-41f6-bf80-aecaa7445d1d
(hbnb)
(hbnb)create User
07563c34-e7f8-4b20-84bb-73ff9e30291b
(hbnb)
(hbnb)User.create()
b81095e8-1ad3-4ccf-b525-695baac4d071
(hbnb)
(hbnb)BaseModel.create()
5984b7e6-8c9b-4593-ac87-6bc17a9c400d
(hbnb)
(hbnb)
```


- **all**: this command show you all instances saved, and have many usage forms. if the file.json is not avalible or until the user not to created anything the command show a list empty, else the command print the information. the usage forms is ***all or all "class name" or "class name".all()***, if you specify the class name the console find and return only class with name specated.
```
(hbnb)all
[]
(hbnb)all BaseModel
[]
(hbnb)all
["[Place] (93d823aa-f03a-41f6-bf80-aecaa7445d1d) {'updated_at': datetime.datetime(2020, 7, 1, 20, 2, 16, 57756), 'id': '93d823aa-f03a-41f6-bf80-aecaa7445d1d', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 16, 57733)}", "[User] (07563c34-e7f8-4b20-84bb-73ff9e30291b) {'updated_at': datetime.datetime(2020, 7, 1, 20, 2, 23, 121839), 'id': '07563c34-e7f8-4b20-84bb-73ff9e30291b', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 23, 121816)}", "[User] (b81095e8-1ad3-4ccf-b525-695baac4d071) {'updated_at': datetime.datetime(2020, 7, 1, 20, 2, 32, 778710), 'id': 'b81095e8-1ad3-4ccf-b525-695baac4d071', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 32, 778702)}", "[BaseModel] (5984b7e6-8c9b-4593-ac87-6bc17a9c400d) {'updated_at': datetime.datetime(2020, 7, 1, 20, 2, 44, 768066), 'id': '5984b7e6-8c9b-4593-ac87-6bc17a9c400d', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 44, 768044)}"]
(hbnb)all BaseModel
["[BaseModel] (5984b7e6-8c9b-4593-ac87-6bc17a9c400d) {'updated_at': datetime.datetime(2020, 7, 1, 20, 2, 44, 768066), 'id': '5984b7e6-8c9b-4593-ac87-6bc17a9c400d', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 44, 768044)}"]
(hbnb)
(hbnb)Place.all()
["[Place] (93d823aa-f03a-41f6-bf80-aecaa7445d1d) {'updated_at': datetime.datetime(2020, 7, 1, 20, 2, 16, 57756), 'id': '93d823aa-f03a-41f6-bf80-aecaa7445d1d', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 16, 57733)}"]
(hbnb)
```

- **show**: this command is similar to all but show you the espefic instance for id and name class. the usage is ***show "class name" "class id" or "class name".show(class id)***
```
(hbnb)
(hbnb)show User b81095e8-1ad3-4ccf-b525-695baac4d071
[User] (b81095e8-1ad3-4ccf-b525-695baac4d071) {'updated_at': datetime.datetime(2020, 7, 1, 20, 2, 32, 778710), 'id': 'b81095e8-1ad3-4ccf-b525-695baac4d071', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 32, 778702)}
(hbnb)
(hbnb)User.show(b81095e8-1ad3-4ccf-b525-695baac4d071)
[User] (b81095e8-1ad3-4ccf-b525-695baac4d071) {'updated_at': datetime.datetime(2020, 7, 1, 20, 2, 32, 778710), 'id': 'b81095e8-1ad3-4ccf-b525-695baac4d071', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 32, 778702)}
(hbnb)
(hbnb)
```

- **update**: this command is for update the eny class that you need create a new attribute, the usage is ***update "lass name" "id" "attribute name" "attribute value" or User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "Jose")***
```
(hbnb)
(hbnb)update User b81095e8-1ad3-4ccf-b525-695baac4d071 first_name "Jose Vallejo C."
(hbnb)
(hbnb)show User b81095e8-1ad3-4ccf-b525-695baac4d071
[User] (b81095e8-1ad3-4ccf-b525-695baac4d071) {'updated_at': datetime.datetime(2020, 7, 1, 20, 27, 26, 376508), 'id': 'b81095e8-1ad3-4ccf-b525-695baac4d071', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 32, 778702), 'first_name': 'Jose Vallejo C.'}
(hbnb)
(hbnb)User.update("b81095e8-1ad3-4ccf-b525-695baac4d071", "first_name", "Carlos Barros")
(hbnb)
(hbnb)show User b81095e8-1ad3-4ccf-b525-695baac4d071
[User] (b81095e8-1ad3-4ccf-b525-695baac4d071) {'updated_at': datetime.datetime(2020, 7, 1, 20, 29, 11, 686213), 'id': 'b81095e8-1ad3-4ccf-b525-695baac4d071', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 32, 778702), 'first_name': 'Carlos'}
(hbnb)
(hbnb)
```

- **destroy**: when you want delete an class saved in the file.json usage this command typed ***destroy "class name" "class id" or "class name.destroy(id class)***
```
(hbnb)
(hbnb)Place.show("93d823aa-f03a-41f6-bf80-aecaa7445d1d")
(hbnb)
["[Place] (93d823aa-f03a-41f6-bf80-aecaa7445d1d) {'updated_at': datetime.datetime(2020, 7, 1, 20, 2, 16, 57756), 'id': '93d823aa-f03a-41f6-bf80-aecaa7445d1d', 'created_at': datetime.datetime(2020, 7, 1, 20, 2, 16, 57733)}"]
(hbnb)
(hbnb)Place.destroy("93d823aa-f03a-41f6-bf80-aecaa7445d1d")
(hbnb)
(hbnb)Place.show("93d823aa-f03a-41f6-bf80-aecaa7445d1d")
show Place 93d823aa-f03a-41f6-bf80-aecaa7445d1d
** no instance found **
(hbnb)
