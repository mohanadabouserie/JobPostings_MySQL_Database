# JobPostingsDB Project

## Overview

The JobPostingsDB project is a comprehensive solution for managing job postings and company details through a relational database system. The project involves the use of a web crawler to scrape data from Wuzzuf’s website, which is then stored in a MySQL database. Additionally, a client application has been developed to connect to a remote MySQL server, allowing users to register, submit job applications, and view relevant postings and company information.

## Features

- **Web Crawler:**
  - Utilized a web crawler using Python to extract data from Wuzzuf’s website.
  - Extracted job postings and company details to populate the relational database.

- **Relational Database System:**
  - Designed and implemented a MySQL database to store job postings and company information.
  - Ensured data integrity and relationships between tables.

- **Client Application:**
  - Developed a client application that connects to a remote MySQL server.
  - Facilitates user registration, allowing individuals to create accounts for personalized experiences.
  - Enables users to submit job applications through the application interface.
  - Provides a user-friendly display of relevant job postings and company details.

- **Data Cleaning:**
  - Implemented data cleaning processes to ensure the accuracy and consistency of information scrapped from Wuzzuf's website.

## Technologies Used

- **MySQL:**
  - Utilized MySQL as the relational database management system.

- **Web Scraping:**
  - Employed a web crawler for extracting data from Wuzzuf’s website using Python.

- **Client Application:**
  - Developed using PyQt library.
