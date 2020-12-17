# Bank Api
---
* [Show Customers List](https://github.com/furserr/bankApi#show-customers-list)
* [Create Customer](https://github.com/furserr/bankApi#create-customer)
* [Show Customer](https://github.com/furserr/bankApi#show-customer)
* [Update Customer](https://github.com/furserr/bankApi#update-customer)
* [Delete Customer](https://github.com/furserr/bankApi#delete-customer)
* [Show Accounts List](https://github.com/furserr/bankApi#show-accounts-list)
* [Create Account](https://github.com/furserr/bankApi#create-account)
* [Show Account](https://github.com/furserr/bankApi#show-account)
* [Update Account](https://github.com/furserr/bankApi#update-account)
* [Delete Account](https://github.com/furserr/bankApi#delete-account)
* [Show Transfers List](https://github.com/furserr/bankApi#show-transfers-list)
* [Create Transfer](https://github.com/furserr/bankApi#create-transfer)
* [Show Transfer](https://github.com/furserr/bankApi#show-transfer)
* [Delete Transfer](https://github.com/furserr/bankApi#delete-transfer)
* [Show Transfer History](https://github.com/furserr/bankApi#show-transfer-history)

### Show Customers List

  Returns json data about customers.

* **URL**

  /customers/

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "id" : 12, "name" : "Michael Scott" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Not Found" }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/customers/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  ---
  
### Create Customer


* **URL**

  /customers/

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   name=[string]

* **Data Params**

  { "name" : "Dwight Schrute" }

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{ "id" : 13, "name" : "Dwight Schrute" }`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ "name": ["This field may not be blank."] }`
---

### Show Customer

  Returns json data about a single customer.

* **URL**

  /customers/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   id=[integer]

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "id" : 13, "name" : "Dwight Schrute" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/customers/12/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  ---
### Update Customer


* **URL**

  /customers/:id

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
 
   id=[integer]

* **Data Params**

  `{ "id" : 13, "name" : "Dwight Schrute" }`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "id" : 13, "name" : "Dwight Schrute" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`
---
### Delete Customer


* **URL**

  /customers/:id

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
   id=[integer]

* **Data Params**

  None

* **Success Response:**

  * **Code:** 204 <br />
    **Content:** `None`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/customers/12/",
      dataType: "json",
      type : "DELETE",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  ---

### Show Accounts List

  Returns json data about accounts.

* **URL**

  /accounts/

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "id" : 12, "balance" : 100.0, "customer": 3 }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Not Found" }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/accounts/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  ---
  
### Create Account


* **URL**

  /accounts/

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   balance=[float]
   customer=[integer]

* **Data Params**

  `{ "id" : 12, "balance" : 100.0, "customer": 3 }`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{ "id" : 12, "balance" : 100.0, customer: 3 }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`
---

### Show Account

  Returns json data about a single account.

* **URL**

  /accounts/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   id=[integer]

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "id" : 12, "balance" : 100.0, customer: 3 }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/accounts/12/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  ---
### Update Account


* **URL**

  /accounts/:id

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
 
   id=[integer]

* **Data Params**

  `{ "id" : 12, "balance" : 100.0, customer: 3 }`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "id" : 12, "balance" : 110.0, customer: 3 }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`
---
### Delete Account


* **URL**

  /accounts/:id

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
   id=[integer]

* **Data Params**

  None

* **Success Response:**

  * **Code:** 204 <br />
    **Content:** `None`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/accounts/12/",
      dataType: "json",
      type : "DELETE",
      success : function(r) {
        console.log(r);
      }
    });
  ```
    ---

### Show Transfers List

  Returns json data about transfers.

* **URL**

  /transfers/

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "id" : 12, "sender" : 2, "receiver": 3, "balance": 20.0 }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Not Found" }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/transfers/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  ---
  
### Create Transfer


* **URL**

  /transfers/

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   sender=[int]
   receiver=[int]
   balance=[float]

* **Data Params**

  `{ "id" : 12, "sender" : 2, "receiver": 3, "balance": 20.0 }`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{ "id" : 12, "sender" : 2, "receiver": 3, "balance": 20.0 }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`
---

### Show Transfer

  Returns json data about a single transfer.

* **URL**

  /transfers/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   id=[integer]

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "id" : 12, "sender" : 2, "receiver": 3, "balance": 20.0 }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/transfers/12/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  ---
### Delete Transfer


* **URL**

  /transfers/:id

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
   id=[integer]

* **Data Params**

  None

* **Success Response:**

  * **Code:** 204 <br />
    **Content:** `None`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/transfers/12/",
      dataType: "json",
      type : "DELETE",
      success : function(r) {
        console.log(r);
      }
    });
  ```
---

### Show Transfer History

  Returns json data about given account's transfer history.

* **URL**

  /accounts/:id/history/

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   id=[integer]

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "id" : 12, "sender" : 2, "receiver": 3, "balance": 20.0 }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/accounts/12/history/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
