def build_person(first_name,last_name, age =''):
    """ Return a dictionary of information about a person """
    person = { 'first': first_name.title(), 'last' : last_name.title()}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix', age = 27)
print(musician)