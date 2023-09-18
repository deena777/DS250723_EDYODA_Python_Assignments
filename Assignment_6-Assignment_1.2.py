'''
2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
'''


import json

indian_states = {
    "Kerala": "Thiruvananthapuram",
    "Andhra Pradesh": "Amaravati",
    "Telangana": "Hyderabad",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Gujarat": "Gandhinagar"
}

filename = "indian_states.json"
with open(filename, "w") as file:
    json.dump(indian_states, file, indent=4)

print(f"The Indian states and capitals have been written to '{filename}'.")
