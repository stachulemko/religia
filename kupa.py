import pandas as pd

# List of tuples
students = pd.DataFrame([('Ankit', 23, 'Delhi', 'A'),
            ('Swapnil', 22, 'Delhi', 'B'),
            ('Aman', 22, 'Dehradun', 'A'),
            ('Jiten', 22, 'Delhi', 'A'),
            ('Jeet', 21, 'Mumbai', 'B')
            ])
students
# Check if 'Jiten' is in the DataFrame
index_list = students[students[0] == 'Jeet']
print(index_list)
