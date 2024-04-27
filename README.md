# Global Rain: Grazioso Salvare Rescue Dog Dashboard

## Motivation
This project is developed for Grazioso Salvare, an innovative international rescue-animal training company, to aid in the identification and categorization of dogs suitable for search-and-rescue training. Grazioso Salvare partners with a non-profit agency operating animal shelters in the Austin, Texas region, which provides data for this purpose.

## Getting Started:
### Installation
1.	Clone the repository.
2.	Install the required Python packages.
3.	Make sure MongoDB is installed and running locally.
### Usage
1.	Run the dashboard.
2.	Navigate to the dashboard notebook and execute the cells to run the dashboard.
## CRUD Tests
 ![image](https://github.com/scglass13/CS-340-Client-server-dev/assets/78313023/bc8488a8-0b60-4c73-be3f-7babb722e1ef)

## Screenshots:
### Dashboard Overview:
 ![image](https://github.com/scglass13/CS-340-Client-server-dev/assets/78313023/fec49e80-fa7b-4a75-a8c3-0a1ec8c59102)
![image](https://github.com/scglass13/CS-340-Client-server-dev/assets/78313023/5613661e-0ae1-40f2-8ec9-789af191aaff)

### Water Rescue Filter:
 ![image](https://github.com/scglass13/CS-340-Client-server-dev/assets/78313023/384782ce-8212-4191-ad8a-36a20eb8d18c)

### Mountain or Wilderness Rescue Filter:
 ![image](https://github.com/scglass13/CS-340-Client-server-dev/assets/78313023/1436b382-7103-44b8-b69d-05d941f8ca3b)

### Disaster Rescue Filter:
 ![image](https://github.com/scglass13/CS-340-Client-server-dev/assets/78313023/4302c57f-07ae-40ad-b8db-e791baf05088)

### Animal Geolocation:
 ![image](https://github.com/scglass13/CS-340-Client-server-dev/assets/78313023/ce0bb0cb-8d3f-4e3c-95ba-ed5d86f337df)


## Tools Used
- Python: Used for the backend development of the dashboard.
- Jupyter Notebook: Integrated development environment for running the dashboard.
- Dash (Plotly): Framework for creating interactive web applications in Python.
- MongoDB: Used as the database model to store and retrieve data.
- Pandas: Data manipulation and analysis library.
- Plotly Express: Library for creating interactive and expressive plots.
- Dash Leaflet: Dash component for interactive maps.

## Project Steps
1.	Database Setup: Established CRUD functionality in Python for MongoDB.
2.	Dashboard Development:
    - Created an interactive data table displaying animal shelter data.
    - Developed filter options for Water Rescue, Mountain or Wilderness Rescue, and Disaster Rescue.
    - Built widgets for dynamic data presentation, including a geolocation chart and a pie chart.
4.	Testing and Deployment:
	  - Tested the dashboard to ensure functionality.
    - Deployed the dashboard locally for user interaction.
    - Captured screenshots to demonstrate dashboard functionality.

## Challenges
- Created a single function to update dashboard and map to prevent duplicate callbacks.
- Implemented dynamic pie chart to display different values based on current filter.
- Established proper callbacks to ensure required dashboard functionality.

## Module Questions
1. How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
   - To ensure programs are maintainable, readable, and adaptable, I focus on clear code organization, meaningful variable and function names, and thorough documentation. In the CRUD Python module for Project One, these principles were crucial for others (or myself in the future) to understand and modify the code easily. By separating database interaction into a module, it enhanced readability and maintainability, as changes to the database structure could be localized. In the future, this module could be reused in various projects requiring MongoDB integration, saving time and ensuring consistency in database operations.
2. How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
   - As a computer scientist, I approach problems methodically, breaking them down into smaller, more manageable tasks. For Grazioso Salvare's database and dashboard requirements, I first analyzed the specifications, identified key functionalities, and designed a database schema accordingly. This approach differed from previous assignments by focusing on real-world application and client needs rather than theoretical concepts. In the future, I would continue to use techniques, such as agile development methodologies, to efficiently meet client requests and adapt to changing requirements.
3. What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
   - Computer scientists solve complex problems by applying computational techniques and algorithms to find efficient solutions. In the context of projects like Grazioso Salvare's, our work can streamline operations, improve data management, and provide valuable insights through analytics. By developing the CRUD Python module and integrating it into their systems, we enable Grazioso Salvare to manage their animal data more effectively and make informed decisions. This project showcases the practical relevance of computer science in solving real-world challenges.
