import unittest
import json
import sys

schemaFile = input("Please enter name of schema file: ")

class TestSchema(unittest.TestCase):
    # set up data
    def setUp(self):
        """Load test data"""
          
        with open(schemaFile) as schema:
            self.schema = json.load(schema)

        self.keyDict = dict()
        for key in self.schema:
            self.keyDict[key] = list(self.schema[key])

    def testAttributeKeyIgnored(self):
        """Checks if schema doesn't capture features of the 'attributes' key."""

        isAttrIgnored = [
            True for key in self.schema if not key.startswith('attributes')
        ]
        return self.assertEqual(len(isAttrIgnored), len(self.schema))

    def testTagInAllAttrs(self):
        """Checks if tag is in all attributes"""
        isTagPresent = [True for key in self.keyDict if "tag" in self.keyDict[key]]
        return self.assertEqual(len(isTagPresent), len(self.keyDict))

    def testDescrInAllAttrs(self):
        """Checks if description is in all attributes"""
        isDescrPresent = [
            True for key in self.keyDict if "description" in self.keyDict[key]
            ]
        return self.assertEqual(len(isDescrPresent), len(self.keyDict))

    def testTypeInAllAttrs(self):
        """Checks if type is in all attributes"""
        isTypePresent = [
            True for key in self.keyDict if "type" in self.keyDict[key]
            ]
        return self.assertEqual(len(isTypePresent), len(self.keyDict))

    def testReqInAllAttrs(self):
        """Checks if required is in all attributes"""
        isReqPresent = [
            True for key in self.keyDict if "required" in self.keyDict[key]
            ]
        return self.assertEqual(len(isReqPresent), len(self.keyDict))

    def testReqIsFalse(self):
        """Checks if required attribute is set to False"""
        isNotRequired = [
            True for key in self.schema if not self.schema[key]["required"]
        ]
        return self.assertEqual(len(isNotRequired), len(self.schema))

    def testTypeIsValid(self):
        """Checks if the type attribute has one of the valid types:
           ['string', 'integer', 'decimal', 'boolean', 'ENUM', 'ARRAY']
        """
        validTypes = ['string', 'integer', 'decimal', 'boolean', 'ENUM', 'ARRAY']
        areAllTypesValid = [
            True for key in self.schema if self.schema[key]['type'] in validTypes
        ]
        return self.assertEqual(len(areAllTypesValid), len(self.schema))

   
    if __name__ == "__main__":
        unittest.main()