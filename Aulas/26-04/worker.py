from database import Database

class Worker:
    def __init__(self, worker):
        self.db = Database()
        

    def insert_worker(self, id):
        return self.db.search_worker(id)
        

