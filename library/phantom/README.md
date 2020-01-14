README
------


## REST_ingest


Refer to the docker file: Download

```
RUN pip3 install requests
ADD https://raw.githubusercontent.com/joelwking/Phantom-Cyber/master/REST_ingest/PhantomIngest.py /src/PhantomIngest.py
```

Or you can simply download using `wget`

Look at the documentation:

```bash
pydoc3 PhantomIngest
```

```bash
# python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import PhantomIngest as ingest
```

```python
help(ingest)
```



credentials = {
  "ph-auth-token": "/foo=",
  "server": "https://ec2-107-22-86-39.compute-1.amazonaws.com"
}


```python
import PhantomIngest as ingest

p = ingest.PhantomIngest(credentials.get('server'), credentials.get('ph-auth-token'))

kontainer = {"label": "events", "name": "Voltaire", "description": "French Enlightenment writer, historian, and philosopher."}

container_id = p.add_container(**kontainer)

art_i_fact = {"name": "François-Marie Arouet", "source_data_identifier": "IR_3458575"}
cef = {'sourceAddress': '192.0.2.1', 'sourcePort': '6553', 'sourceUserId': 'voltaire@example.net'}
meta_data = {"Influenced by": "John Locke, William Shakespeare, Isaac Newton", "Born": "November 21, 1694",
             "quote": "Judge of a man by his questions rather than by his answers."}

artifact_id = p.add_artifact(container_id, cef, meta_data, **art_i_fact)
```

Error handling

```python
>>> credentials['server'] = '172.31.44.15'
>>> credentials['server'] = '172.31.44.1'
>>>  p = ingest.PhantomIngest(credentials.get('server'), credentials.get('ph-auth-token')
  File "<stdin>", line 1
    p = ingest.PhantomIngest(credentials.get('server'), credentials.get('ph-auth-token')
    ^
IndentationError: unexpected indent
>>> p = ingest.PhantomIngest(credentials.get('server'), credentials.get('ph-auth-token')
... )
>>> try:
...     p.add_container(**kontainer)
... except Exception as e:
...     print(e)
...
HTTPSConnectionPool(host='172.31.44.1', port=443): Max retries exceeded with url: /rest/container (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7feb969cdda0>: Failed to establish a new connection: [Errno 113] No route to host',))
