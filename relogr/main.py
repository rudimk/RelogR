import rethinkdb as r
import arrow as a

class RelogR(object):
    # Store config info as class attributes.
    rethinkdb_host = None
    rethinkdb_port = None
    timestamp_format = None

    # Initialize the RelogR class with config info.
    def __init__(self, rethinkdb_host, rethinkdb_port, timestamp_format):
        self.rethinkdb_host = rethinkdb_host
        self.rethinkdb_port = rethinkdb_port
        self.timestamp_format = timestamp_format
    
    
    
