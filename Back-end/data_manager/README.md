Data management:

The program requires a private key of Firebase to run( which we cannot share to public).

data_collector.py   is a tweaked version of real-time search for gathering data. It collects data according to the taxonomy.

db_maintainance.py   is for managing data after they have been collected, especially for generating keywords for search api.

search_api.py   contains 3 apis: the search api, the product detail api, the comparison api.

categorize.py   is for parsing taxomony.en-US.txt into readable json.

taxonomy.en-US.txt   abd taxonomy.json are the Google product taxonomy.
