from flatten_json import flatten, unflatten
import json
import re
import sys

def generate_schema(data):
    """generate_schema(data) => dict
       flattens the data, generate the schema and return it 
    """
    flattened_data = flatten(data)
    schema = dict()
    temp = {
        'tag': '',
        'description': '',
        'required': False
    }
    # check each key and determine the type of its value
    for key in flattened_data:
        digits = re.findall(r'\d+', key) # checks if key contains digit; for keys containing lists
        if digits:
            r = key.find(digits[0])
            if  key[:r-1] not in schema:
                schema[key[:r-1]] = dict()
                if key.endswith(digits[0]): # lists of strings
                    temp.update({'type':"ENUM"})
                    schema[key[:r-1]].update(temp)
                else: # lists of dictionaries/json objects
                    temp.update({'type': "ARRAY"})
                    schema[key[:r-1]].update(temp)
            else:
                continue
        else:
            schema[key] = dict()
            if isinstance(flattened_data[key], bool):
                temp.update({'type': 'boolean'})
            elif isinstance(flattened_data[key], int):
                temp.update({'type': "integer"})
            elif isinstance(flattened_data[key], float):
                temp.update({'type': 'decimal'})
            elif isinstance(flattened_data[key], str):
                temp.update({'type': 'string'})
            elif not flattened_data[key]:
                temp.update({'type': 'null'})
            schema[key].update(temp)
    return schema

def main():
    """
       main() ==> None
       Gets input and output file names from terminal:
           python generateSchema <inputFile> <outputFile>
       then writes schema to output file.
    """
    inpFile = sys.argv[1]
    outFile = sys.argv[2]

    with open(inpFile) as fh:
        data = json.load(fh)
    
    data.pop('attributes')
    schema = generate_schema(data)
    
    with open(outFile, 'w') as fh:
        json.dump(schema, fh, indent=4)


## test

if __name__ == "__main__":
    main()