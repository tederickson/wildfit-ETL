# wildfit-ETL

WILDFIT Extract Transform Load

# Design

Read Excel spreadsheets and call the WILDFIT server to insert recipes.

The title sheet contains the attributes common to the entire recipe.

The recipe sheet contains one or more recipes.  For example the meat and the sauce.

A recipe row has either a

* Title (new instruction group)
* Instruction (new recipe instruction added to the current instruction group)
* Ingredient (new ingredient add to the current instruction group)

But if there is only one instruction group then the Title is optional
