import sys

#import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}


def capital_of_Idaho():
    print("the capital of Idaho is:", STATES_CAPITALS['Idaho'])
        
capital_of_Idaho()
print ("\n")

def all_states():
    print ("The lists of the states is:")
    [print(keys) for keys in STATES_CAPITALS]
    

all_states()
print ("\n")

def all_capitals():
    print ("The list of thr capitals is:")
    for keys, value in STATES_CAPITALS.items():
        print(value)


all_capitals()
print ("\n")

def states_capitals_string():
    
    sorted_STATES_CAPITALS = sorted(STATES_CAPITALS.items(), key=lambda x:x[0])
    str = ""
    print ("The sort list of the states and capitals is:")

    for keys, value in sorted_STATES_CAPITALS:
        str += keys + '->' + value + ' , '
      
    print(str)
    
states_capitals_string()
print ("\n")


def get_state():
    capital = input('Enter a capital to find the state: ')
    for value, key in STATES_CAPITALS.items():
        if capital in key:
            print('The state is :', value)
               
get_state()


def get_state(capital):
    pass



def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    sys.exit(main())
