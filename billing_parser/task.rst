Introduction
~~~~~~~~~~~~

There is some billing system. It contains a lot of huge reports. All these
reports are generated in "csv" format. All these csv files are packed into
"zip" archives. All these archives are located in the same folder.

All csv files has similar structure with similar list of headers.

Important headers
~~~~~~~~~~~~~~~~~

There are a lot of headers in csv files, but some of them are more or less
important. Please look into "user:scalr-meta" and "Cost" headers.

Parse reports
~~~~~~~~~~~~~

If there are just 5 sections in "user:scalr-meta" header, use this line for
calculations. Under 5 sections we mean:

v1:5:9800005:44:8d49e87f-b77b-44c4-a6b8-feffb4a47cde

Where there are 5 blocks separated by ":" symbol.

If you find such header, you should also parse it. Using header from previous
step:

env=5
farm=9800005
farm_role=44
server=8d49e87f-b77b-44c4-a6b8-feffb4a47cde

Calculate cost for each parameter: env, farm, farm_role, server.

Each csv file is about a few GB. Each zip file is also about a few GB.
There are thousands of zip files. That's why it's better to parse all these
reports using threads or processes (you should deside what is better in this
case).

Save aggregated data into SQLite3 database.
It should be possible to find a cost for each env, farm, farm_role, server,
etc.


Some examples of zip archives with csv files should be found in data/
directory in current folder.
