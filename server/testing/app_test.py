import re
import pytest
from server.app import create_app, db
from server.models import Animal, Enclosure, Zookeeper

app = create_app()

class TestApp:
    '''Flask application in app.py'''

    @pytest.fixture(autouse=True, scope="class")
    def setup(self):
        with app.app_context():
            db.drop_all()
            db.create_all()

            a_1 = Animal(name='Simba', species='Lion')
            a_2 = Animal(name='Nala', species='Lioness')
            e = Enclosure(environment='Savannah', open_to_visitors=True)
            z = Zookeeper(name='Joe', birthday='1990-05-10')

            e.animals = [a_1, a_2]
            z.animals = [a_1, a_2]
            db.session.add_all([a_1, a_2, e, z])
            db.session.commit()

            yield

            db.session.remove()
            db.drop_all()

    def test_animal_route(self):
        response = app.test_client().get('/animal/1')
        assert response.status_code == 200

    def test_animal_route_has_attrs(self):
        response = app.test_client().get('/animal/1')
        assert '<ul>' in response.data.decode()
        assert 'Name' in response.data.decode()
        assert 'Species' in response.data.decode()

    def test_animal_route_has_many_to_one_attrs(self):
        response = app.test_client().get('/animal/1')
        assert 'Zookeeper' in response.data.decode()
        assert 'Enclosure' in response.data.decode()

    def test_zookeeper_route(self):
        response = app.test_client().get('/zookeeper/1')
        assert response.status_code == 200

    def test_zookeeper_route_has_attrs(self):
        response = app.test_client().get('/zookeeper/1')
        assert 'Name' in response.data.decode()
        assert 'Birthday' in response.data.decode()

    def test_zookeeper_route_has_one_to_many_attr(self):
        response = app.test_client().get('/zookeeper/1')
        assert 'Animal' in response.data.decode()

    def test_enclosure_route(self):
        response = app.test_client().get('/enclosure/1')
        assert response.status_code == 200

    def test_enclosure_route_has_attrs(self):
        response = app.test_client().get('/enclosure/1')
        assert 'Environment' in response.data.decode()
        assert 'Open to Visitors' in response.data.decode()

    def test_enclosure_route_has_one_to_many_attr(self):
        response = app.test_client().get('/enclosure/1')
        assert 'Animal' in response.data.decode()
