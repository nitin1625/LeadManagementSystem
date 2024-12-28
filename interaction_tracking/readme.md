3. Interaction Tracking 

## **General Interactions APIs**

### **1. Create a New Interaction**
- **Endpoint**:  
  ```http
  POST /track/interactions/
  ```
- **Purpose**:  
  Record a new interaction between a lead and a contact.

- **Payload**:
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

- **Example Response**:
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

### **2. List All Interactions**
- **Endpoint**:  
  ```http
  GET /track/interactions/
  ```
- **Purpose**:  
  Retrieve all recorded interactions, optionally filtered by `lead` or `contact`.

- **Filters**:
  - `?lead=<lead_id>`: Filter interactions for a specific lead.
  - `?contact=<contact_id>`: Filter interactions for a specific contact.

- **Example Request**:
  ```http
  GET /track/interactions/?lead=2
  ```

- **Example Response**:
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

### **3. Retrieve a Specific Interaction**
- **Endpoint**:  
  ```http
  GET /track/interactions/<interaction_id>/
  ```
- **Purpose**:  
  Fetch details of a specific interaction by its `id`.

- **Example Request**:
  ```http
  GET /track/interactions/1/
  ```

- **Example Response**:
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

### **4. Update an Interaction**
- **Endpoint**:  
  ```http
  PATCH /track/interactions/<interaction_id>/
  ```
- **Purpose**:  
  Modify an existing interaction (e.g., update interaction type, details, or date).

- **Payload**:
  ```json
  {
      "details": "Confirmed product interest."
  }
  ```

- **Example Response**:
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

### **5. Delete an Interaction**
- **Endpoint**:  
  ```http
  DELETE /track/interactions/<interaction_id>/
  ```
- **Purpose**:  
  Delete a specific interaction.

- **Example Request**:
  ```http
  DELETE /track/interactions/1/
  ```

- **Example Response**:
  ```json
  {
      "message": "Interaction deleted successfully."
  }
  ```

---

## **Order-Specific APIs**

### **6. List Order-Specific Interactions**
- **Endpoint**:  
  ```http
  GET /track/interactions/orders/
  ```
- **Purpose**:  
  Retrieve interactions where orders were placed (`order_placed=true`).

- **Filters**:
  - `?lead=<lead_id>`: Filter by a specific lead.

- **Example Request**:
  ```http
  GET /track/interactions/orders/?lead=2
  ```

- **Example Response**:
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

### **7. Retrieve Order Details (Optional, if using `Order` Model)**
If using the `Order` model, this API fetches detailed order information linked to an interaction.

- **Endpoint**:  
  ```http
  GET /track/interactions/<interaction_id>/order_details/
  ```
- **Purpose**:  
  Retrieve specific order details for an interaction.

- **Example Response**:
  ```json
  {
      "product_details": "50 units of Product A",
      "quantity": 50,
      "total_price": 500.00,
      "order_date": "2024-12-25T12:00:00Z"
  }
```