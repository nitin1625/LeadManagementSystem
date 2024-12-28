![alt text](image.png)
Here are the APIs for the `contact` app with their corresponding URLs and payloads:

### 1. **Create Contact**
- **URL**: `/contact/contacts/`
- **Method**: `POST`
- **Payload**:
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

### 2. **List Contacts**
- **URL**: `/contact/contacts/`
- **Method**: `GET`
- **Payload**: None (Returns a list of contacts)

Example response:
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

### 3. **Retrieve Contact by ID**
- **URL**: `/contact/contacts/{id}/`
- **Method**: `GET`
- **Payload**: None (Returns the details of the contact with the given ID)

Example response:
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

### 4. **Update Contact**
- **URL**: `/contact/contacts/{id}/`
- **Method**: `PUT`
- **Payload**:
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

### 5. **Delete Contact**
- **URL**: `/contact/contacts/{id}/`
- **Method**: `DELETE`
- **Payload**: None (Deletes the contact with the given ID)

