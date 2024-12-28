# Key Account Manager (KAM) Lead Management System

## Project Overview

The **Key Account Manager (KAM) Lead Management System** is designed for key account managers to effectively manage leads, contacts, interactions, call planning, and performance tracking. This system plays a critical role in fostering relationships with large restaurant accounts by providing a centralized platform to monitor and enhance account performance.

Key features include:

- **Lead Management**: Add, track, and manage leads with their status.
- **Contact Management**: Maintain multiple points of contact (POCs) per account.
- **Interaction Tracking**: Record and monitor interactions like calls and orders.
- **Call Planning**: Schedule and track call frequencies.
- **Performance Tracking**: Identify high-performing accounts and underperformers.

This project also adheres to modularity and scalability principles, ensuring extensibility for future feature additions.

## System Requirements

- **Programming Language**: Python 3.8+
- **Framework**: Django 4.x+
- **Database**: SQLite (default, easily extendable to other databases)
- **Dependencies**: Specified in `requirements.txt`

### Core Requirements

1. RESTful API support with robust authentication and error handling.
2. Data models designed for efficient querying and entity relationships.
3. Business logic for call scheduling, performance metrics, and lead transitions.

## Project Structure

The application is modular, consisting of several Django apps to manage different functionalities:

```
LeadManagementSystem/
│
├── db.sqlite3                  # SQLite database file
├── manage.py                   # Django's management script
├── requirements.txt            # Project dependencies
├── readme.md                   # Project documentation
│
├── call_planning/              # Call planning module
├── contact/                    # Contact management module
├── interaction_tracking/       # Interaction tracking module
├── leads/                      # Lead management module
├── performance_tracking/       # Performance analysis module
│
└── LeadManagementSystem/       # Main project folder (contains settings.py)
```

## Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd LeadManagementSystem
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv env
   source env/bin/activate   # Linux/Mac
   env\Scripts\activate      # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

## Running Instructions

1. **Start the Server**
   ```bash
   python manage.py runserver
   ```

2. **Access the Application**
   Navigate to `http://127.0.0.1:8000/` in your web browser.

## Test Execution Guide

To validate the functionality of the application:

```bash
python manage.py test
```

Ensure that comprehensive test cases are implemented for both core and edge functionalities.

## API Documentation

The system offers RESTful APIs for seamless integration with external systems. Below are key API endpoints:

1. **Authentication**
   - `POST /api/token/`: Obtain JWT token for authentication.
   - `POST /api/token/refresh/`: Refresh JWT tokens.

2. **Modules**
   - `GET /lead/`: Access lead-related APIs.
   - `GET /contact/`: Access contact-related APIs.
   - `GET /track/`: Access interaction tracking APIs.
   - `GET /call/`: Access call planning APIs.
   - `GET /performance/`: Access performance tracking APIs.

### Sample Request: Authentication
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password": "password"}'
```

### Sample Request: Fetch Leads
```bash
curl -X GET http://127.0.0.1:8000/lead/ \
-H "Authorization: Bearer <your_token>"
```




## Lead Management

This module handles the management of restaurant leads, enabling key account managers to create, update, and track leads effectively.

### API Endpoints

#### **1. List All Leads**
**Endpoint**: `GET /lead/restaurants/`  
**Description**: Retrieves a list of all leads.

---

#### **2. Create a New Lead**
**Endpoint**: `POST /lead/restaurants/`  
**Description**: Creates a new lead with the provided details.  

**Payload**:
```json
{
    "name": "The Great Restaurant",
    "address": "123 Food Street",
    "city": "New York",
    "state": "New York",
    "pincode": "10001",
    "contact_person": "John Doe",
    "phone": "+1234567890",
    "email": "johndoe@example.com",
    "lead_status": "NEW",
    "potential_revenue": 5000.00,
    "notes": "Interested in premium features.",
    "assigned_to": 1
}
```

---

#### **3. Get Single Lead**
**Endpoint**: `GET /lead/restaurants/{id}/`  
**Description**: Fetches the details of a specific lead by its unique ID.

---

#### **4. Update Lead**
**Endpoint**: `PUT /lead/restaurants/{id}/`  
**Description**: Updates the details of an existing lead.  

**Payload**: Similar to the payload for creating a lead.

---

#### **5. Delete Lead**
**Endpoint**: `DELETE /lead/restaurants/{id}/`  
**Description**: Deletes a lead by its ID.

---

#### **6. Change Lead Status**
**Endpoint**: `POST /lead/restaurants/{id}/change_status/`  
**Description**: Updates the status of a lead to reflect its current stage in the pipeline.  

**Payload**:
```json
{
    "status": "CONTACTED"
}
```

---

#### **7. Get Lead Status History**
**Endpoint**: `GET /lead/restaurants/{id}/status_history/`  
**Description**: Fetches the history of status changes for a specific lead.

---

### Sample Usage

#### Example: Create a New Lead
**Request**:
```bash
curl -X POST http://127.0.0.1:8000/lead/restaurants/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your_token>" \
-d '{
    "name": "The Great Restaurant",
    "address": "123 Food Street",
    "city": "New York",
    "state": "New York",
    "pincode": "10001",
    "contact_person": "John Doe",
    "phone": "+1234567890",
    "email": "johndoe@example.com",
    "lead_status": "NEW",
    "potential_revenue": 5000.00,
    "notes": "Interested in premium features.",
    "assigned_to": 1
}'
```

**Response**:
```json
{
    "id": 1,
    "name": "The Great Restaurant",
    "address": "123 Food Street",
    "city": "New York",
    "state": "New York",
    "pincode": "10001",
    "contact_person": "John Doe",
    "phone": "+1234567890",
    "email": "johndoe@example.com",
    "lead_status": "NEW",
    "potential_revenue": 5000.00,
    "notes": "Interested in premium features.",
    "assigned_to": 1,
    "created_at": "2024-12-28T10:00:00Z",
    "updated_at": "2024-12-28T10:00:00Z"
}
```


## Contact Management

This module manages the contact details of individuals associated with leads, such as restaurant managers and other stakeholders.

### API Endpoints

#### **1. Create Contact**
**Endpoint**: `POST /contact/contacts/`  
**Description**: Adds a new contact associated with a restaurant.  

**Payload**:
```json
{
    "restaurant": 1,
    "name": "John Doe",
    "role": "Manager",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "address": "123 Street, City, Country"
}
```

---

#### **2. List Contacts**
**Endpoint**: `GET /contact/contacts/`  
**Description**: Retrieves a list of all contacts.  

**Response**:
```json
[
    {
        "id": 1,
        "restaurant": 1,
        "name": "John Doe",
        "role": "Manager",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "address": "123 Street, City, Country"
    }
]
```

---

#### **3. Retrieve Contact by ID**
**Endpoint**: `GET /contact/contacts/{id}/`  
**Description**: Fetches the details of a specific contact by its unique ID.  

**Response**:
```json
{
    "id": 1,
    "restaurant": 1,
    "name": "John Doe",
    "role": "Manager",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "address": "123 Street, City, Country"
}
```

---

#### **4. Update Contact**
**Endpoint**: `PUT /contact/contacts/{id}/`  
**Description**: Updates the details of an existing contact.  

**Payload**:
```json
{
    "restaurant": 1,
    "name": "John Smith",
    "role": "Head Manager",
    "email": "john.smith@example.com",
    "phone": "987-654-3210",
    "address": "456 Avenue, City, Country"
}
```

---

#### **5. Delete Contact**
**Endpoint**: `DELETE /contact/contacts/{id}/`  
**Description**: Deletes the contact with the given ID.

---

### Sample Usage

#### Example: Create a New Contact
**Request**:
```bash
curl -X POST http://127.0.0.1:8000/contact/contacts/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your_token>" \
-d '{
    "restaurant": 1,
    "name": "John Doe",
    "role": "Manager",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "address": "123 Street, City, Country"
}'
```

**Response**:
```json
{
    "id": 1,
    "restaurant": 1,
    "name": "John Doe",
    "role": "Manager",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "address": "123 Street, City, Country"
}
```



## Interaction Tracking

This module manages the recording and tracking of interactions between leads and contacts, including calls, emails, and orders.

### **General Interactions APIs**

#### **1. Create a New Interaction**
**Endpoint**: `POST /track/interactions/`  
**Purpose**: Record a new interaction between a lead and a contact.

**Payload**:
```json
{
    "lead": 2,
    "contact": 3,
    "interaction_type": "CALL",
    "details": "Followed up on last week's discussion.",
    "order_placed": false,
    "date": "2024-12-24T15:30:00Z"
}
```

**Example Response**:
```json
{
    "id": 1,
    "lead": 2,
    "contact": 3,
    "interaction_type": "CALL",
    "details": "Followed up on last week's discussion.",
    "order_placed": false,
    "date": "2024-12-24T15:30:00Z"
}
```

---

#### **2. List All Interactions**
**Endpoint**: `GET /track/interactions/`  
**Purpose**: Retrieve all recorded interactions, optionally filtered by `lead` or `contact`.

**Filters**:
- `?lead=<lead_id>`: Filter by a specific lead.
- `?contact=<contact_id>`: Filter by a specific contact.

**Example Request**:
```http
GET /track/interactions/?lead=2
```

**Example Response**:
```json
[
    {
        "id": 1,
        "lead": 2,
        "contact": 3,
        "interaction_type": "CALL",
        "details": "Followed up on last week's discussion.",
        "order_placed": false,
        "date": "2024-12-24T15:30:00Z"
    },
    {
        "id": 2,
        "lead": 2,
        "contact": 4,
        "interaction_type": "EMAIL",
        "details": "Sent product catalog.",
        "order_placed": false,
        "date": "2024-12-25T10:00:00Z"
    }
]
```

---

#### **3. Retrieve a Specific Interaction**
**Endpoint**: `GET /track/interactions/<interaction_id>/`  
**Purpose**: Fetch details of a specific interaction by its unique ID.

**Example Request**:
```http
GET /track/interactions/1/
```

**Example Response**:
```json
{
    "id": 1,
    "lead": 2,
    "contact": 3,
    "interaction_type": "CALL",
    "details": "Followed up on last week's discussion.",
    "order_placed": false,
    "date": "2024-12-24T15:30:00Z"
}
```

---

#### **4. Update an Interaction**
**Endpoint**: `PATCH /track/interactions/<interaction_id>/`  
**Purpose**: Modify an existing interaction.

**Payload**:
```json
{
    "details": "Confirmed product interest."
}
```

**Example Response**:
```json
{
    "id": 1,
    "lead": 2,
    "contact": 3,
    "interaction_type": "CALL",
    "details": "Confirmed product interest.",
    "order_placed": false,
    "date": "2024-12-24T15:30:00Z"
}
```

---

#### **5. Delete an Interaction**
**Endpoint**: `DELETE /track/interactions/<interaction_id>/`  
**Purpose**: Delete a specific interaction.

**Example Response**:
```json
{
    "message": "Interaction deleted successfully."
}
```

---

### **Order-Specific APIs**

#### **6. List Order-Specific Interactions**
**Endpoint**: `GET /track/interactions/orders/`  
**Purpose**: Retrieve interactions where orders were placed (`order_placed=true`).

**Filters**:
- `?lead=<lead_id>`: Filter by a specific lead.

**Example Response**:
```json
[
    {
        "id": 3,
        "lead": 2,
        "contact": 5,
        "interaction_type": "ORDER",
        "details": "Placed an order for 50 units of product A.",
        "order_placed": true,
        "date": "2024-12-25T12:00:00Z"
    }
]
```

---

#### **7. Retrieve Order Details**
**Endpoint**: `GET /track/interactions/<interaction_id>/order_details/`  
**Purpose**: Fetch detailed order information linked to an interaction.  

**Example Response**:
```json
{
    "product_details": "50 units of Product A",
    "quantity": 50,
    "total_price": 500.00,
    "order_date": "2024-12-25T12:00:00Z"
}
```

## Call Planning
 endpoints supporting the creation, retrieval, updating, and deletion of call plans. Here's a concise summary of its key functionalities:

### **Core Functionalities**
1. **Create a New Call Plan**:
   - Record call plans for leads with customizable frequency options (Daily, Weekly, etc.).
   - Optional notes to provide context for the plan.

2. **Retrieve Call Plans**:
   - Fetch all call plans or filter by today's required calls.
   - Get details of a specific plan via its unique ID.

3. **Update Call Plans**:
   - Modify plan attributes like frequency or notes.
   - Record calls dynamically, updating the `next_call_date` based on frequency.

4. **Frequency Management**:
   - Adjust call frequency with a dedicated endpoint.

5. **Deletion of Plans**:
   - Cleanly remove any outdated or unnecessary call plans.

---

### **Efficiency Features**
- **Next Call Logic**: Automatically calculates the next call date based on frequency.
- **Today’s Calls**: Quickly retrieve all calls due for today, ensuring high-priority actions are not missed.

---

### **API Highlights**


#### **1. Create a New Call Plan**  
- **Endpoint**:  
  `POST /call/`  
- **Purpose**:  
  Create a call plan for a lead.  
- **Payload**:  
  ```json
  {
    "lead": 1,
    "frequency": "DAILY",
    "notes": "Initial call plan for lead 1."
  }
  ```  
- **Example Response**:  
  ```json
  {
    "id": 1,
    "lead": 1,
    "frequency": "DAILY",
    "last_called": null,
    "next_call_date": "2024-12-29T00:00:00Z",
    "notes": "Initial call plan for lead 1."
  }
  ```

---

#### **2. Get All Call Plans**  
- **Endpoint**:  
  `GET /call/`  
- **Purpose**:  
  Retrieve all call plans.  
- **Example Response**:  
  ```json
  [
    {
      "id": 1,
      "lead": 1,
      "frequency": "DAILY",
      "last_called": null,
      "next_call_date": "2024-12-29T00:00:00Z",
      "notes": "Initial call plan for lead 1."
    },
    {
      "id": 2,
      "lead": 2,
      "frequency": "WEEKLY",
      "last_called": "2024-12-25T15:00:00Z",
      "next_call_date": "2024-12-31T15:00:00Z",
      "notes": "Follow-up call plan for lead 2."
    }
  ]
  ```

---

#### **3. Get Call Plans Requiring a Call Today**  
- **Endpoint**:  
  `GET /call/today/`  
- **Purpose**:  
  Retrieve call plans that require a call today.  
- **Example Response**:  
  ```json
  [
    {
      "id": 1,
      "lead": 1,
      "frequency": "DAILY",
      "last_called": null,
      "next_call_date": "2024-12-28T00:00:00Z",
      "notes": "Initial call plan for lead 1."
    }
  ]
  ```

---

#### **4. Get a Specific Call Plan**  
- **Endpoint**:  
  `GET /call/{id}/`  
- **Purpose**:  
  Retrieve details of a specific call plan.  
- **Example Response**:  
  ```json
  {
    "id": 1,
    "lead": 1,
    "frequency": "DAILY",
    "last_called": null,
    "next_call_date": "2024-12-29T00:00:00Z",
    "notes": "Initial call plan for lead 1."
  }
  ```

---

#### **5. Update a Call Plan**  
- **Endpoint**:  
  `PATCH /call/{id}/`  
- **Purpose**:  
  Update an existing call plan.  
- **Payload**:  
  ```json
  {
    "frequency": "WEEKLY",
    "notes": "Updated call plan."
  }
  ```  
- **Example Response**:  
  ```json
  {
    "id": 1,
    "lead": 1,
    "frequency": "WEEKLY",
    "last_called": null,
    "next_call_date": "2024-12-29T00:00:00Z",
    "notes": "Updated call plan."
  }
  ```

---

#### **6. Record a Call**  
- **Endpoint**:  
  `POST /call/{id}/record_call/`  
- **Purpose**:  
  Record a call and update `last_called` and `next_call_date`.  
- **Payload**:  
  ```json
  {
    "last_called": "2024-12-28T10:00:00Z"
  }
  ```  
- **Example Response**:  
  ```json
  {
    "id": 1,
    "lead": 1,
    "frequency": "DAILY",
    "last_called": "2024-12-28T10:00:00Z",
    "next_call_date": "2024-12-29T10:00:00Z",
    "notes": "Initial call plan for lead 1."
  }
  ```

---

#### **7. Set or Update Frequency for a Call Plan**  
- **Endpoint**:  
  `PATCH /call/{id}/set_frequency/`  
- **Purpose**:  
  Set or update the frequency of a call plan.  
- **Payload**:  
  ```json
  {
    "frequency": "WEEKLY"
  }
  ```  
- **Example Response**:  
  ```json
  {
    "id": 1,
    "lead": 1,
    "frequency": "WEEKLY",
    "last_called": "2024-12-28T10:00:00Z",
    "next_call_date": "2025-01-04T10:00:00Z",
    "notes": "Updated call plan."
  }
  ```

---

#### **8. Delete a Call Plan**  
- **Endpoint**:  
  `DELETE /call/{id}/`  
- **Purpose**:  
  Delete a specific call plan.  
- **Example Response**:  
  ```json
  {
    "detail": "Successfully deleted the call plan."
  }
  ```



## Performance Tracking

This module provides insights into the performance of leads and accounts, including identifying well-performing accounts, tracking ordering patterns, and pinpointing underperforming accounts.

---

### **1. Track Well-Performing Accounts**  
- **Endpoint**: `GET /performance/performing-accounts/`  
- **Purpose**: Retrieve a list of well-performing restaurants with high revenue potential.  
- **Payload**: None required.  
- **Example Response**:  
  ```json
  [
    {
      "id": 1,
      "name": "Restaurant A",
      "lead_status": "CONVERTED",
      "potential_revenue": 15000.00,
      "cuisine_type": "Italian",
      "restaurant_type": "Fine Dining"
    },
    {
      "id": 2,
      "name": "Restaurant B",
      "lead_status": "CONVERTED",
      "potential_revenue": 12000.00,
      "cuisine_type": "Chinese",
      "restaurant_type": "Casual"
    }
  ]
  ```  

---

### **2. Monitor Ordering Patterns and Frequency**  
- **Endpoint**: `GET /performance/order-patterns/`  
- **Purpose**: Analyze the ordering frequency of restaurants over the past and current months.  
- **Payload**: None required.  
- **Example Response**:  
  ```json
  [
    {
      "restaurant_id": 1,
      "name": "Restaurant A",
      "orders_last_month": 15,
      "orders_this_month": 5
    },
    {
      "restaurant_id": 2,
      "name": "Restaurant B",
      "orders_last_month": 10,
      "orders_this_month": 3
    }
  ]
  ```  

---

### **3. Identify Underperforming Accounts**  
- **Endpoint**: `GET /performance/underperforming-accounts/`  
- **Purpose**: Retrieve a list of underperforming restaurants based on lead status and potential revenue.  
- **Payload**: None required.  
- **Example Response**:  
  ```json
  [
    {
      "id": 3,
      "name": "Restaurant C",
      "lead_status": "NEW",
      "potential_revenue": 5000.00,
      "cuisine_type": "Indian",
      "restaurant_type": "Fast Food"
    },
    {
      "id": 4,
      "name": "Restaurant D",
      "lead_status": "LOST",
      "potential_revenue": 2000.00,
      "cuisine_type": "Mexican",
      "restaurant_type": "Fast Casual"
    }
  ]
  ```  

---

### **Summary of Endpoints**

| **Endpoint**                               | **Method** | **Purpose**                                          |
|--------------------------------------------|------------|------------------------------------------------------|
| `/performance/performing-accounts/`        | `GET`      | Track well-performing accounts based on revenue.    |
| `/performance/order-patterns/`             | `GET`      | Monitor ordering patterns and frequency.            |
| `/performance/underperforming-accounts/`   | `GET`      | Identify underperforming accounts.                  |

---

### **Key Insights**
1. **Performing Accounts**:
   - Includes restaurants with high potential revenue and converted lead status.
   - Helps focus on top-performing clients.

2. **Ordering Patterns**:
   - Analyzes order trends for the past and current months.
   - Useful for identifying changes in engagement.

3. **Underperforming Accounts**:
   - Highlights restaurants needing additional attention or intervention.
   - Targets accounts with low revenue and engagement levels.

