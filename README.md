# ShelterSearchAPI
Welcome to this Django Real Estate API project! This API provides functionalities for managing property listings, real estate agents, and a blog. It's built using the Django framework, allowing you to easily interact with real estate data and content.

# Features
- Property Listings: View, create, update, and delete property listings. Each listing includes details like property type, location, price, and description.
- Real Estate Agents: Manage real estate agents' information, including their profiles, contact details, and listings they represent.
- Blog: The API includes a blog section where you can create and manage blog posts related to real estate. Share insights, tips, and news with your users.

# Installation
1. Clone this repository to your local machine.
   ```
   git clone https://github.com/Brainboxx/ShelterSearchAPI.git
   ```
2. Navigate to the project directory.
   ```
   cd ShelterSearchAPI
   ```
3. Create a virtual environment (recommended).
   ```
   python -m venv venv
   ```
4. Activate the virtual environment
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On Mac:
     ```
     source venv/bin/activate
     ```      
5. Install the required dependencies.
   ```
   pip install -r requirements.txt
   ```
6. Set up the database.
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Create a superuser account to access the admin panel.
   ```
   python manage.py createsuperuser
   ```   
8. Start the development server.
   ```
   python manage.py runserver
   ```
# Usage
- Access the admin panel at http://localhost:8000/admin/ to manage property listings, agents, and blog posts.
- Explore and interact with the API endpoints for property listings, agents, and blog via the docs at http://localhost:8000/api/docs/.

# Contributing
Contributions are welcome! If you find a bug or have suggestions, please open an issue or submit a pull request. Make sure to follow the project's coding standards.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
   
