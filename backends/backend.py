import abc

class DBBackend(abc.ABC):
    def open_db_file(self):
        """"""
    
    def prepare_db(self):
        """"""

    @abc.abstractmethod
    def fullfill_db(self):
        """"""
