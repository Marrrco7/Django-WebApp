
Overview
--------

Dynamic web application developed using Django, allowing for easy addition, update, display, and deletion of game information. The application integrates with a PostgreSQL database to efficiently store and retrieve game data for a videogames company (Threading Labs).

Table of Contents
-----------------

- Project Structure
  - Features
  - Analysis and Design
  - Challenge Overview
  - Solution Architecture
  - Functionalities
  - System Architecture
  - Database Design

Project Structure
-----------------


Relevatn Features
--------

- **CRUD functionalities**: Create, Read, Update, and Delete video game entries.
- **User Authentication**: Secure login and logout functionalities for staff members.
- **Permissions**: Restrict access to certain views only to users with certain permissions.
- **Responsive Design**: Easy to use UI made with Bootstrap4.


Analysis and Design
-------------------

### Solution Architecture

![image](https://github.com/user-attachments/assets/496a4afa-7767-429f-871e-cc012faa441a)

The architecture composed by these following components:

- **Web Application**: The project is build as a Django webApp that serves as a backend. It handles data validation, business logic
  and HTTP requests by the users thanks to the Django MVT architecturarl pattern:
  
  - **Models**: Define the structure of the database (VideoGame and Genre models).
  - **Views**: Handle the business logic and provides posibility to interact with the models.
  - **Templates**: Render the user interface using HTML and Bootstrap4.

- **Database**: The project uses a relational postgre SQL database for data storage and efficient retrieving of information. The Django App interacts with this database
  through the ORM (Object Relational Mapper), making it easier to perform CRUD operations. The columns of the database are defined in the Django models.py: Title, Release date, Description,
  and Genre. The database design is composed by two tables: Videogame and Genre, implemented with a one to many relationship (a genre can have multiple games, but each genre's game must be only one).

**Tables**:

1. **Genre**
   - `id`: Primary key
   - `title`: String (50 chars)

2. **VideoGame**
   - `id`: Primary key
   - `title`: String (100 chars)
   - `release_date`: Date
   - `description`: String (100 characters)
   - `genre_id`: Foreign key referencing the `Genre` table
  
  
- **Local Environment**: The application is running in a local server allowing staff members to access the WebApp by connecting to the IP address of the local machine.

### Functionalities

- **Game Adding**: Users can add new video games by filling the form rendered by the views.py
- **Details Editing**: Users can update existing game information.
- **Game Deletion**: Possibility to easily remove games from the catalog (permission required).
- **View Game List**: Users can view a list of all games in the catalog.
- **User Authentication**: Users must log in to access the application.
- **Permissions**: Only authorized users can add, edit, or delete games (Admins and managers).
- **Security**: Implement proper authentication and authorization mechanisms (CSRF tokens, loggin authentication).
- **Usability**: UI intuitive and easy to navigate, designed for staff memebers with non-technical backround.


### User Interface Design
 **Base Template**: Includes navigation and common UI elements.
- **Videogame List**: Displays a table of all video games with options to edit or delete.
- **Videogame Form**: Form for adding or editing a video game.
- **Authentication Pages**: Login and logout pages.

**Design Elements**:

- **Bootstrap 4.3.1**: Used for responsive design and styling (includes the jumbotron component).
- **Font Awesome 6.6.0**: Provides icons for buttons and actions.
- **Jumbotron Component**: Used for the header section in the base template.
- **Base Template**: Includes navigation and common UI elements.
- **Videogame List**: Displays a table of all video games with options to edit or delete.
- **Videogame Form**: Form for adding, deleting or updating videogames
