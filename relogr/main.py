import rethinkdb as r
import arrow as a
import collections

class RelogR(object):
    # Store config info as class attributes.
    rethinkdb_host = None
    rethinkdb_port = None
    timestamp_format = None
    timezone = None

    # Initialize the RelogR class with config info.
    def __init__(self, rethinkdb_host, rethinkdb_port, timestamp_format, timezone):
        self.rethinkdb_host = rethinkdb_host
        self.rethinkdb_port = rethinkdb_port
        self.timestamp_format = timestamp_format
        self.timezone = timezone
    
    def log(self, message):
        timestamp = a.now().to(self.timezone).format(self.timestamp_format)
        r.connect(rethinkdb_host, rethinkdb_port).repl()
        payload = collections.OrderedDict()
        payload['timestamp'] = timestamp
        payload['message'] = message
        r.db('relogr').table('relogr_logs').insert(payload).run()
        return True

    
