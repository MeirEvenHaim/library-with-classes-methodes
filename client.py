import sqlite3

class Client:
    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

class ClientDAL:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def add_client(self, client):
        """
        Add a new client to the database.
        """
        self.c.execute("INSERT INTO client (name, city, age) VALUES (?, ?, ?)",
                       (client.name, client.city, client.age))
        self.conn.commit()

    def get_all_clients(self):
        """
        Retrieve all clients from the database.
        """
        self.c.execute("SELECT * FROM client")
        return self.c.fetchall()

    # Add other CRUD operations
