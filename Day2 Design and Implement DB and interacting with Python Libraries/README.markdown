# Netflix Shows Database Project

This project involves creating a relational database using **SQL Server** to store data about Netflix shows, and performing data insertion through a Python application. The dataset is based on a CSV file containing information on various Netflix shows, including movie/TV show type, cast, director, country, genre, etc.

## **Project Overview**

The goal of this project is to:
- **Create a database schema** for storing information related to Netflix shows, including tables for shows, directors, cast members, countries, and genres.
- **Insert data** into the database from a CSV file, ensuring that there are no duplicates and maintaining the integrity of relationships between shows, cast, director, country, and genre.
- **Normalize text data** (e.g., remove accents and ensure case-insensitivity) to handle potential issues with data matching during insertion.

## **Key Features**
- **ERD Creation**: A detailed Entity-Relationship Diagram (ERD) is created based on the CSV data structure to guide the database design.
- **SQLAlchemy**: Uses SQLAlchemy ORM to interact with SQL Server.
- **Data Normalization**: Ensures that data inserted into the database does not contain duplicates, including normalized cast, director, and genre names to prevent insertion issues.
- **Error Handling**: Handles errors related to unique constraints, ensuring that the system continues functioning even if some records fail to insert.

## Database Schema
The database schema includes the following key tables:

- **Show**: Main show details
- **Director**: Show directors
- **Cast**: Cast members
- **Country**: Countries where shows are available
- **Genre**: Genres for shows
- **Show_Metadata**: Metadata for each show, such as date_added and rating
- **Join Tables**:
  - **Show_Director**: Links shows to directors
  - **Show_Cast**: Links shows to cast members
  - **Show_Country**: Links shows to countries
  - **Show_Genre**: Links shows to genres

## ERD Diagram
Below is the Entity-Relationship Diagram (ERD) representing the database schema:

![ERD Image](https://github.com/Ahmed-Gomaa1/Data-Engineer-Daily-Tasks/blob/main/Day2%20Design%20and%20Implement%20DB%20and%20interacting%20with%20Python%20Libraries/Netflix%20Shows.png)

## **Setup and Requirements**
1. Install Python dependencies:
    - `SQLAlchemy`
    - `pandas`
    - `pyodbc`
    - `unicodedata`
    - `sys`

# **Project Workflow**
 - **Data Processing**: Read the data from the CSV file, clean and normalize the data, and insert it into the database while maintaining relationships between shows, directors, cast, country, and genre.
 - **Integrity Handling**: Ensure that no duplicates are inserted by checking existing records before each insert.
 - **Error Handling**: If duplicates are found (e.g., a director or cast member already exists), the script will skip the insertion for that particular record and continue processing the rest of the file.

# **Conclusion**
 - This project demonstrates how to design a database schema and populate it with data from a CSV file while ensuring data integrity and normalization using Python and SQL Server. 
 - This solution is extensible for more complex datasets and can be adapted to other relational databases as needed.
