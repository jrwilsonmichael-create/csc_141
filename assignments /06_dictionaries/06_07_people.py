# I will be adding in people
people = {
    'Mike W': {'age' : 18, 'city' : 'Philadelphia'},
    'Mike A': {'age' : 19, 'city' : 'New york'},
    'Jhonahan': {'age' : 20, 'city' : 'Los Angeles'}
}
for name, info in people.items():
    age = info['age']
    city = info['city']
    print(f"{name} is {age} years old and lives in {city}.")