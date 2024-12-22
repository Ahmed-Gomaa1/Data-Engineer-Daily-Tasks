# Netflix Shows Database Project

This project involves creating a relational database using **SQL Server** to store data about Netflix shows, and performing data insertion through a Python application. The dataset is based on a CSV file containing information on various Netflix shows, including movie/TV show type, cast, director, country, genre, etc.

## **Project Overview**

The goal of this project is to:
- **Create a database schema** for storing information related to Netflix shows, including tables for shows, directors, cast members, countries, and genres.
- **Insert data** into the database from a CSV file, ensuring that there are no duplicates and maintaining the integrity of relationships between shows, cast, director, country, and genre.
- **Normalize text data** (e.g., remove accents and ensure case-insensitivity) to handle potential issues with data matching during insertion.
- **Generate a report** for successful insertion and error handling for duplicate data.

## **Key Features**
- **ERD Creation**: A detailed Entity-Relationship Diagram (ERD) is created based on the CSV data structure to guide the database design.
- **SQLAlchemy**: Uses SQLAlchemy ORM to interact with SQL Server.
- **Data Normalization**: Ensures that data inserted into the database does not contain duplicates, including normalized cast, director, and genre names to prevent insertion issues.
- **Error Handling**: Handles errors related to unique constraints, ensuring that the system continues functioning even if some records fail to insert.
  
## **Setup and Requirements**

1. Install Python dependencies:
    - `SQLAlchemy`
    - `pandas`
    - `pyodbc`
