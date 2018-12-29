def build_person(first_name,last_name, age =''):
    """ Return a dictionary of information about a person """
    person = { 'first': first_name.title(), 'last' : last_name.title()}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix', age = 27)
programmer = build_person('oscar','lopez')
brogrammer = build_person('shawn','tarver',22)
print(musician)
print(brogrammer)
print(programmer)
