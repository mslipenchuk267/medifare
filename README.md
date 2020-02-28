# Medifare

### Install Dependencies:
**Fuzzywuzzy** : Fuzzy Logic String Matcing Library
- Link: https://github.com/seatgeek/fuzzywuzzy
- Install: pip install fuzzywuzzy

# Build
### Server
Run: `python server.py <port>`
### Client
Run: `python client.py <host> <port>`

# Client Usage
1. Enter a medical procedure
2. View result
3. Respond y/n to do another transaction

# User Query Matching
1. Compare user query to list of medical procedures
- `match_scores = process.extract(user_search_query,medical_procedure_list)`
  - This returns a list of tuples containing procedure name and match percentage pairs
2. Pick procedure with highest match to user query
- `best_match = process.extractOne(user_search_query,medical_procedure_list)`
  - This returns a tuple containing the best matched procedure and corrsponding match percentage
