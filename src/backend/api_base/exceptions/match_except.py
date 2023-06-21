class DataNotMatchHash(Exception):
    """Exception raised for errors blockchain mismatch data errors
    Attributes:
        id: id of object
        table: name of table
    """

    def __init__(self, id, table, message_pattern="{} with {} has data mismatch in blockchain network!"):
        self.id = id
        self.table = table
        self.message = message_pattern.format(table, str(id))
        super().__init__(self.message)
