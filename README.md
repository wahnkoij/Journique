# Journique

## Project Description

Journique is an app designed for posting images and journaling. It provides a seamless platform for users to express their thoughts through text and multimedia, creating a rich and personalized journaling experience.

## Technologies Used

- Python
- Django (version==3.2)
- HTML, CSS, JavaScript
- Bootstrap 
- PostgreSQL
- Docker
- Nginx
- Other relevant technologies...

## Installation

Follow these step-by-step instructions to install and run the Journique app.

### Prerequisites

Make sure you have Python and pip installed on your machine.

### Installation Steps

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

### Using Docker

[Journique](https://github.com/wahnkoij/Journique) can also be run using Docker for containerization. Follow the steps below:

1. Make sure you have Docker installed on your machine.

2. Navigate to the project directory:

    ```bash
    cd Journique
    ```

3. Build the Docker containers:

    ```bash
    docker-compose up --build -d
    ```

4. Run migrations within the Docker container:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

5. Open your web browser and navigate to http://localhost:8000/ to access the Journique app.

### Customization

Make sure to update the Django secret key and other sensitive information in the `settings.py` file. Customize the app according to your preferences and needs. Feel free to explore and enhance the features based on your project goals.
