class MySet:
    def __init__(self, enumerable=None):
        # Initialize the dictionary to store unique values
        self.dictionary = {}
        
        # If enumerable is None, set it to an empty list
        if enumerable is None:
            enumerable = []
        
        # Populate the dictionary with unique values from the enumerable
        for value in enumerable:
            self.dictionary[value] = True
    
    # Check if a value is present in the set
    def has(self, value):
        return value in self.dictionary
    
    # Convert the set to a string representation
    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'
        
    # Add a value to the set
    def add(self, value):
        self.dictionary[value] = True
        return self  # Return the instance to allow method chaining
    
    # Get the size of the set
    def size(self):
        return len(self.dictionary)
    
    # Delete a value from the set
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self  # Return the instance to allow method chaining
    
    # Clear all values from the set
    def clear(self):
        self.dictionary.clear()
