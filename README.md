# library_ex


Pros and Cons of Using Two Dictionaries

Pros:
- Faster lookups for both title and author searches since each dictionary is dedicated to a specific operation.
- Straightforward implementation and intuitive data storage.
- Clear separation of responsibilities: one dictionary for titles, another for authors.

Cons: 
- Duplication of data (books stored in both dictionaries).
- Maintaining synchronization between dictionaries can be challenging during updates or deletions.
- Code Overhead more code is required to handle operations like adding, updating, or deleting books compared to a single dictionary.


Pros and Cons of Using Two Tries

Pros:
- Highly efficient prefix-based searches (autocomplete and partial matches) for both titles and authors.
- Search operations are quick, even for large datasets.

Cons:
- Requires more memory to store the tries.
- Implementation is more complex compared to dictionary-based or single-trie solutions.
