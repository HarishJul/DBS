import numpy as np

def same_person(data):
    data = np.array(data)

    # For each user, match it with the whole matrice
    matches = sum(user == data for user in data)
    
    # Isolated users only match with themselves, hence only have 1 on their line
    isolated = set(np.where(np.sum(matches, axis=1) == data.shape[1])[0])
    
    # Together are other users
    together = set(range(len(data))) ^ set(isolated)
    
    return together



data = [
("username1","phone_number1", "email1"),
("usernameX","phone_number1", "emailX"),
("usernameZ","phone_numberZ", "email1Z"),
("usernameY","phone_numberY", "emailX"),
]

print(same_person(data))