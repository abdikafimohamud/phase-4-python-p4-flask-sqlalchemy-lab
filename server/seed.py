from app import create_app
from models import db, Animal, Zookeeper, Enclosure

app = create_app()

with app.app_context():
    print("Clearing db...")
    Animal.query.delete()
    Zookeeper.query.delete()
    Enclosure.query.delete()

    print("Seeding db...")

    zk1 = Zookeeper(name="Dylan Taylor", birthday="1985-06-10")
    zk2 = Zookeeper(name="Stephanie Contreras", birthday="1996-09-20")

    enc1 = Enclosure(environment="trees", open_to_visitors=True)
    enc2 = Enclosure(environment="pond", open_to_visitors=False)

    a1 = Animal(name="Logan", species="Snake", zookeeper=zk1, enclosure=enc1)
    a2 = Animal(name="Leo", species="Lion", zookeeper=zk2, enclosure=enc2)
    a3 = Animal(name="Milo", species="Monkey", zookeeper=zk2, enclosure=enc1)

    db.session.add_all([zk1, zk2, enc1, enc2, a1, a2, a3])
    db.session.commit()

    print("Done seeding.")
