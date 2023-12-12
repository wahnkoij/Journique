# Journique

### Project Description

Journique is an app designed for posting images and journaling. It provides a seamless platform for users to express their thoughts through text and multimedia, creating a rich and personalized journaling experience.

### Technologies Used

- Python
- Django (Django==5.0)
- HTML, CSS, JavaScript
- Bootstrap 
- PostgreSQL
- Docker
- Other relevant technologies...

### Installation

Follow these step-by-step instructions to install and run the Journique app.

#### Prerequisites

Make sure you have Python and pip installed on your machine.

#### Installation Steps

1. Clone the repository to your local machine:

   ```bash
   git clone "https://github.com/wahnkoij/Journique" 
   ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash 
    python -m venv venv
    source venv/bin/activate   # On Windows: .\venv\Scripts\activate
    ```
3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. How to Run
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
    
5. Open your web browser and navigate to http://localhost:8000/ to access the Journique app.


6. Make sure to update the Django secret key and other sensitive information in the settings.py file.
   Customize the app according to your preferences and needs.
   Feel free to explore and enhance the features based on your project goals.
