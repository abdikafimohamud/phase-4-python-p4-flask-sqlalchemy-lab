from app import create_app, db
app = create_app()
from server.models import db, Animal

class TestAnimal:
    '''Animal model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        a = Animal()
        assert a
        assert isinstance(a, Animal)

    def test_has_name_and_species(self):
        '''can be instantiated with a name and species.'''
        a = Animal(name='Phil', species='Rhinoceros')
        assert a.name == 'Phil'
        assert a.species == 'Rhinoceros'