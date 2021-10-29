## JSON schema sniffer

### Description

The generateSchema.py script sniffs the schema of an input JSON file and writes it to the specified output JSON file. It does this by first flattening the input, then analyze the keys of the flattened data. For deeply nested objects, the flattened key would comprise the initial parent and child keys separated by an underscore ('_'). If the the nested object comprises a list, the index of each item in the array is appended at the end of the flattened key, and if this array comprises other nested objects, its parent-child keys are appended at the end of the index of the array. Keys generated from more than one level of the JSON data are separated with underscores.

So, keys having numbers are from objects with arrays. The script uses this information to map the arrays of keys that ends with a number as ENUM, and those whose keys don't as ARRAY. Below is the structure of the output schema:

"""
{
    "key": {
        "type": <"string"|"integer"|"boolean"|"ENUM"|"ARRAY"|"null">,
        "tag": "",
        "description": "",
        "required" : false
    }
}
"""

The type attribute is determined from the value of each object as follows:
string ==> "string"
whole numbers ==> "integer"
floating point numbers ==> "decimal"
True/False ==> "boolean"
Array of strings ==> "ENUM"
Array of objects ==> "ARRAY"
Empty array ==> "null"

## Dependencies

* flatten_json==0.1.13

## How to Use Script

python generateSchema.py <path_to_inputFile> <path_to_outputFile>

## How to run unit test

python -m unittest -v test_schema.py

Here are the test cases considered:
* Checks if schema doesn't capture features of the 'attributes' key;
* Checks if description is in all attributes; 
* Checks if required is in all attributes;
* Checks if required attribute is set to False.
* Checks if tag is in all attributes.
* Checks if type is in all attributes.
* Checks if the type attribute has one of the valid types.





