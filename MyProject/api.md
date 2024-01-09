# API Documentation

## Pins

### GET /api/pins/

**Description:**
Retrieve a list of all pins.

**Request:**
- Method: GET

**Response:**
- Status Code: 200 OK
- Body: List of pins with details.

---

### POST /api/pins/

**Description:**
Create a new pin.

**Request:**
- Method: POST
- Headers: `{ "Authorization": "Bearer <your_token>" }`
- Body: Pin details to be created.

**Response:**
- Status Code: 201 Created
- Body: Details of the created pin.

---

### GET /api/pins/<int:pk>/

**Description:**
Retrieve details of a specific pin.

**Request:**
- Method: GET
- Headers: `{ "Authorization": "Bearer <your_token>" }`

**Response:**
- Status Code: 200 OK
- Body: Details of the requested pin.

---

### PUT /api/pins/<int:pk>/

**Description:**
Update details of a specific pin.

**Request:**
- Method: PUT
- Headers: `{ "Authorization": "Bearer <your_token>" }`
- Body: Updated pin details.

**Response:**
- Status Code: 200 OK
- Body: Updated details of the pin.

---

### DELETE /api/pins/<int:pk>/

**Description:**
Delete a specific pin.

**Request:**
- Method: DELETE
- Headers: `{ "Authorization": "Bearer <your_token>" }`

**Response:**
- Status Code: 204 No Content

---

## Users

### GET /api/users/

**Description:**
Retrieve a list of all users.

**Request:**
- Method: GET
- Headers: `{ "Authorization": "Bearer <your_token>" }`

**Response:**
- Status Code: 200 OK
- Body: List of users with details.

---

### GET /api/users/<int:pk>/

**Description:**
Retrieve details of a specific user.

**Request:**
- Method: GET
- Headers: `{ "Authorization": "Bearer <your_token>" }`

**Response:**
- Status Code: 200 OK
- Body: Details of the requested user.

---

## Categories

### GET /api/categories/

**Description:**
Retrieve a list of all categories.

**Request:**
- Method: GET
- Headers: `{ "Authorization": "Bearer <your_token>" }`

**Response:**
- Status Code: 200 OK
- Body: List of categories with details.

---

### POST /api/categories/

**Description:**
Create a new category.

**Request:**
- Method: POST
- Headers: `{ "Authorization": "Bearer <your_token>" }`
- Body: Category details to be created.

**Response:**
- Status Code: 201 Created
- Body: Details of the created category.

---

### GET /api/categories/<int:pk>/

**Description:**
Retrieve details of a specific category.

**Request:**
- Method: GET
- Headers: `{ "Authorization": "Bearer <your_token>" }`

**Response:**
- Status Code: 200 OK
- Body: Details of the requested category.

---

### PUT /api/categories/<int:pk>/

**Description:**
Update details of a specific category.

**Request:**
- Method: PUT
- Headers: `{ "Authorization": "Bearer <your_token>" }`
- Body: Updated category details.

**Response:**
- Status Code: 200 OK
- Body: Updated details of the category.

---

### DELETE /api/categories/<int:pk>/

**Description:**
Delete a specific category.

**Request:**
- Method: DELETE
- Headers: `{ "Authorization": "Bearer <your_token>" }`

**Response:**
- Status Code: 204 No Content

---

