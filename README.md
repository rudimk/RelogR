## Logstah

### The hippest logger in town.

Logstah is a generic logger that uses RethinkDB as its primary store. Logs are stored as a RethinkDB document with a message, a timezone-aware timestamp and a unique UUID, and can be queried using a range of RethinkDB client libraries in multiple languages - see [here](https://www.rethinkdb.com/docs/install-drivers/) for a full list of which languages have working drivers.



### Prerequisites

1. For one, you should be using Python! 
2. A running RethinkDB instance. Make sure there's a separate database called `relogr`, containing a table called `relogr_logs`. Yes, the names don't make a lot of sense, long story behind that.
3. A fondness for <*insert alcoholic beverage of your choice*>.

### Getting started

Grab the latest version from PyPI: 

`pip install logstah`

Next, initialize Logstah:

```python
from logstah import Logstah

logger = Logstah(rethinkdb_host=<IP>, rethinkdb_port=<PORT>, timestamp_format=<FORMAT>, timezone=<ZONE>)
```

The timestamp format uses traditional placeholders; for `23-Jun-2016 13:34:20`, you'd use `DD-MMM-YYYY HH:mm:SS` as the timestamp format. The timezones are from the tz database - check out [this list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to see what your desired timezone's tz identifier is.

Now all that's left, is a bit of logging! When you need to log an event or a message:

```python
logger.log(message="A las armas!")
```

And that's it! Logstah will store that as a log with the timestamp and a unique ID in the `relogr_logs` table. 



### FAQs

**Q.** Why RethinkDB?

**A.** I like RethinkDB. I think it's a great database. I think it's kind of hipster too. And I like ReQL a lot. I hope you like it too.

**Q.** Can I store different kinds of messages/events from different sources?

**A.** Yes, but it'll be rather hard to determine what's what, when you're out analyzing those logs. The idea is that the next version of Logstah introduces *categories*, which can be assigned to a logging message - that would help you differentiate between log entries being streamed from different sources. Hang in there, bud.

**Q.** Is this for real?

**A.** Trust me, if Donald Trump can become the President - *anything's possible*.

**Q.** Alright, I get it. But I don't use Python...

**A.** I'd love to convert you to Python, but I'm sure you'll see the light soon enough. In the meantime, yes - I'm thinking of writing ports for Ruby, Crystal, Go and *maybe* Node.js. No timelines on that though, so if you want to pitch in, let's fly.