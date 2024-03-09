
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10608945&assignment_repo_type=AssignmentRepo)
# Exam 1

Update the solution contents of this file according to [the instructions](instructions/instructions.md).

## Solutions

The following sections contain a report on the solutions to each of the required components of this exam.

### Data munging

The code in the Python program, [solution.py](solution.py), contains the solutions to the **data munging** part of this exam.

### Spreadsheet analysis

The spreadsheet file, [wifi.xslx](data/wifi.xslx), contains the solutions to the **spreadsheet analysis** part of this exam. In addition, the formulas used in that spreadsheet are indicated below:

1. Total number of free Wi-Fi hotspots in NYC

```
=COUNTIF(C:C,"Free")
```

2. Number of free Wi-Fi hotspots in each of the 5 boroughs of NYC.

```
=COUNTIFS(C:C,"Free",B:B,2)
=COUNTIFS(C:C,"Free",B:B,3)
=COUNTIFS(C:C,"Free",B:B,1)
=COUNTIFS(C:C,"Free",B:B,5)
=COUNTIFS(C:C,"Free",B:B,4)
```

3. Number of free Wi-Fi hotspots provided by the LinkNYC - Citybridge in each of the zip codes of Manhattan.

```
=COUNTIFS(C:C,"Free",D:D,"LinkNYC - Citybridge",V:V,AE25)
```

4. The percent of all hotspots in Manhattan that are provided by LinkNYC - Citybridge.

```
=COUNTIFS(D:D,D15,B:B,1)/COUNTIF(B:B,1)*100%
```

### SQL queries

This section shows the SQL queries that you determined solved each of the given problems.

1. Write two SQL commands to create two tables named `hotspots` and `populations`.

```sql
DROP TABLE IF EXISTS hotspots;
CREATE TABLE hotspots (
  id INTEGER PRIMARY KEY,
  borough_id INTEGER,
  type TEXT,
  provider TEXT,
  name TEXT,
  location TEXT,
  latitude REAL,
  longitude REAL,
  x REAL,
  y REAL,
  location_t TEXT,
  remarks TEXT,
  city TEXT,
  ssid TEXT,
  source_id TEXT,
  activated DATETIME,
  borocode INTEGER,
  borough_name TEXT,
  nta_code TEXT,
  nta TEXT,
  council_district INTEGER,
  postcode INTEGER,
  boro_cd INTEGER,
  census_tract INTEGER,
  bctcb2010 INTEGER,
  bin INTEGER,
  bbl INTEGER,
  doitt_id INTEGER,
  lat_lng TEXT
)WITHOUT ROWID;
```

```sql
DROP TABLE IF EXISTS populations;
CREATE TABLE populations (
    borough TEXT,
    year INTEGER,
    fips_county_code INTEGER,
    nta_code TEXT,
    nta TEXT,
    population INTEGER
);
```

2. Import the data in the `wifi.csv` and `neighborhood_populations.csv` CSV files into these two tables.

```sql
.mode csv
.import /Users/sisi/Desktop/updated-exam1-SisiDzy/data/wifi.csv hotspots
```

```sql
.mode csv
.import /Users/sisi/Desktop/updated-exam1-SisiDzy/data/neighborhood_populations.csv populations
```

3. Display the five zip codes with the most Wi-Fi hotspots and the number of Wi-Fi-hotspots in each in descending order of the number of Wi-Fi-hotspots.

```sql
SELECT postcode, COUNT(id) FROM hotspots GROUP BY postcode ORDER BY COUNT(id) DESC LIMIT 5;
```

4. Display a list of the name, location, and zip code for all of the free Wi-Fi locations provided by `ALTICEUSA` in Bronx, in descending order of zip code.

```sql
SELECT name, location, postcode FROM hotspots WHERE NOT type = "Limited Free" AND provider = "ALTICEUSA" AND borough_name = "Bronx" ORDER BY postcode DESC;
```

5. Display the names of each of the boroughs of NYC, and the number of free Wi-Fi hotspots in each.

```sql
SELECT borough_name, COUNT(id) FROM hotspots WHERE type = 'Free' GROUP BY borough_name;
```

6. Display the number of wifi hotspots in Bay Ridge, Brooklyn along with the population of Bay Ridge, Brooklyn.

```sql
SELECT COUNT(hotspots.id), populations.population FROM hotspots INNER JOIN populations ON hotspots.nta=populations.nta WHERE hotspots.nta = "Bay Ridge" AND year = 2010;
```

7. Display the number of **Free** wifi hotspots in each of the 5 NYC boroughs, along with the population of each borough.

```sql
SELECT COUNT(hotspots.id) as number, hotspots.borough_name, new_table.sum FROM hotspots INNER JOIN (SELECT borough, SUM(population) as sum FROM populations
 WHERE year = 2010 GROUP BY borough) as new_table ON hotspots.borough_name = new_table.borough WHERE hotspots.type = 'Free' GROUP BY hotspots.borough_name;
```

8. Display the names of each of the neighborhoods in which there exist Wi-Fi hotspots, but for which we do not have population data.

```sql
SELECT DISTINCT hotspots.nta FROM hotspots LEFT JOIN populations ON hotspots.nta_code = populations.nta_code
WHERE populations.population IS NULL;
```

9. Write an additional SQL query of your choice using Sqlite with this table; then describe the results

Display the average population of the neighborhoods in Bronx in 2000.

```sql
SELECT ROUND(AVG(population)) FROM populations WHERE borough = 'Bronx' and year = 2000;
```

### Normalization and Entity-relationship diagramming

This section contains responses to the questions on normalization and entity-relationship diagramming.

1. Is the data in `wifi.csv` in fourth normal form?

```
No, it isn't.
```

2. Explain why or why not the `wifi.csv` data meets 4NF.

```
It doesn't meet 4NF because it even doesn't meet 1NF as the values in the "lat_lng" field are not singular values. And since the table's primary key is not a composite primary key, 2NF does not apply to the data. And many non-key fields are facts about other non-key fields, for example, borough_id is only related to borough_name but not the primary key, so the data doesn't meet 3NF. At last, since it violates 1NF and 3NF, it does not meet 4NF.
```

3. Is the data in `neighborhood_populations.csv` in fourth normal form?

```
No, it isn't.
```

4. Explain why or why not the `neighborhood_populations.csv` data meets 4NF.

```
First, values in all fields are singular and all records contain the same number of fields. But, there is no primary key in this data, so we cannot proceed to later normal forms. Moreover, there are non-key fields about other non-key fields, such as nta and nta_code. As a result, the data does not meet 4NF.
```

5. Use [draw.io](https://draw.io) to draw an Entity-Relationship Diagram showing a 4NF-compliant form of this data, including primary key field(s), relationship(s), and cardinality.

![Placeholder E-R Diagram](./images/placeholder-er-diagram.svg)
