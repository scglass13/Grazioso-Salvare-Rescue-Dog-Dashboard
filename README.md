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
