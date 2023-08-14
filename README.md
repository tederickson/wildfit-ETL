# wildfit-ETL

WILDFIT Extract Transform Load

# Design

Read Excel spreadsheets and call the WILDFIT server to insert recipes.

The connection and secrets are found in the .env file.  The contents change based on test or production environment.

The project utilizes Object-oriented Programming.  The main class is ParseRecipes.py.  
* An abstract class defines the common methods of child classes tasked with parsing a particular Excel sheet
* Child classes parse the sheet, validate column headers and get the value of row and header
* Data classes are used to hold and convert the data to JSON
* Enums are used to map column headings to indexes
* The main class calls the RESTful web service with the JSON request

Command line arguments are used for help or to turn on debugging 
which writes the large JSON request into the local server's test directory.

# Acceptance Criteria
The title sheet contains the attributes common to the entire recipe.

The recipe sheet contains one or more recipes.  For example the meat and the sauce.

A recipe row has either a

* Title (new instruction group)
* Instruction (new recipe instruction added to the current instruction group)
* Ingredient (new ingredient add to the current instruction group)

But if there is only one instruction group then the Title is optional
