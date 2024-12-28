## Call Planning 

### **1. Create a New Call Plan (POST /call/)**
- **URL**: `http://127.0.0.1:8000/call/`
- **Method**: `POST`
- **Description**: This endpoint allows you to create a new call plan for a lead.
- **Payload**:

```json
{
  "lead": 1,                     // ID of the lead (Restaurant instance)
  "frequency": "DAILY",          // Frequency: "DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"
  "notes": "Initial call plan."  // Notes (optional)
}
```

- **Response** (Success):

```json
{
  "id": 1,
  "lead": 1,
  "frequency": "DAILY",
  "last_called": null,
  "next_call_date": "2024-12-29T00:00:00Z",
  "notes": "Initial call plan."
}
```

---

### **2. Get All Call Plans (GET /call/)**
- **URL**: `http://127.0.0.1:8000/call/`
- **Method**: `GET`
- **Description**: Fetches a list of all call plans.
- **Response**:

```json
[
  {
    "id": 1,
    "lead": 1,
    "frequency": "DAILY",
    "last_called": null,
    "next_call_date": "2024-12-29T00:00:00Z",
    "notes": "Initial call plan."
  },
  {
    "id": 2,
    "lead": 2,
    "frequency": "WEEKLY",
    "last_called": "2024-12-25T15:00:00Z",
    "next_call_date": "2024-12-31T15:00:00Z",
    "notes": "Follow-up call plan."
  }
]
```

---

### **3. Get Call Plans Requiring a Call Today (GET /call/today/)**
- **URL**: `http://127.0.0.1:8000/call/today/`
- **Method**: `GET`
- **Description**: Fetches the list of call plans whose `next_call_date` matches today's date.
- **Response**:

```json
[
  {
    "id": 1,
    "lead": 1,
    "frequency": "DAILY",
    "last_called": null,
    "next_call_date": "2024-12-28T00:00:00Z",
    "notes": "Initial call plan."
  }
]
```

---

### **4. Get a Specific Call Plan (GET /call/{id}/)**
- **URL**: `http://127.0.0.1:8000/call/{id}/`
- **Method**: `GET`
- **Description**: Fetches the details of a specific call plan using its ID.
- **Response**:

```json
{
  "id": 1,
  "lead": 1,
  "frequency": "DAILY",
  "last_called": null,
  "next_call_date": "2024-12-29T00:00:00Z",
  "notes": "Initial call plan."
}
```

---

### **5. Update a Call Plan (PATCH /call/{id}/)**
- **URL**: `http://127.0.0.1:8000/call/{id}/`
- **Method**: `PATCH`
- **Description**: Allows you to update the details of a specific call plan, such as frequency, last called, or notes.
- **Payload**:

```json
{
  "frequency": "WEEKLY",        // New frequency, if updating
  "notes": "Updated call plan." // Updated notes
}
```

- **Response** (Success):

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

### **6. Record a Call (POST /call/{id}/record_call/)**
- **URL**: `http://127.0.0.1:8000/call/{id}/record_call/`
- **Method**: `POST`
- **Description**: This endpoint records the last call made for the given `CallPlan` and updates the `next_call_date` based on the frequency.
- **Payload**:

```json
{
  "last_called": "2024-12-28T10:00:00Z"  // Timestamp of when the call was made
}
```

- **Response**:

```json
{
  "id": 1,
  "lead": 1,
  "frequency": "DAILY",
  "last_called": "2024-12-28T10:00:00Z",
  "next_call_date": "2024-12-29T10:00:00Z",
  "notes": "Initial call plan."
}
```

---

### **7. Set or Update Frequency for a Call Plan (PATCH /call/{id}/set_frequency/)**
- **URL**: `http://127.0.0.1:8000/call/{id}/set_frequency/`
- **Method**: `PATCH`
- **Description**: This endpoint allows you to set or update the call frequency for a given `CallPlan`.
- **Payload**:

```json
{
  "frequency": "WEEKLY"  // New frequency to set
}
```

- **Response**:

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

### **8. Delete a Call Plan (DELETE /call/{id}/)**
- **URL**: `http://127.0.0.1:8000/call/{id}/`
- **Method**: `DELETE`
- **Description**: This endpoint deletes a specific call plan based on the provided `id`.
- **Response** (Success):

```json
{
  "detail": "Successfully deleted the call plan."
}
```

---

### **Summary of API Endpoints**


![alt text](image-1.png)