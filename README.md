Step-by-Step Guide for API Access from the Frontend

1.    User Registration:
        When the user submits their registration form, capture their details (username, password, email).
        Send a POST request to the registration endpoint (http://127.0.0.1:8000/api/accounts/auth/registration/).
        On successful registration, inform the user and possibly log them in automatically.

        content must be provided:(POST)
            {
                "username": "your_name",
                "email": "your_email@gmail.com",
                "password1": "TestPassword123",
                "password2": "TestPassword123",
                "first_name": "fname",
                "last_name": "lname",
                "phone_no": "9813121824",
                "address": "Godawari"
            }

2.    User Login:
        After registration, or if they’re returning users, prompt the user for their credentials (username and password).
        Send a POST request to the login endpoint (e.g., http://127.0.0.1:8000/api/token/).
        Store the received access and refresh tokens securely (e.g., in local storage or cookies).

        content must be provided:(POST)
            {
                "username": "your_name",
                "password": "TestPassword123"
            }

3.    Access Protected API Endpoints:
        For any protected resources (like user profile, order history), add the Authorization header to requests. Use the access token obtained during login.
        Example: For fetching the user profile, send a GET request to the profile endpoint (e.g., http://127.0.0.1:8000/api/accounts/profile/) with the token in the header.


        For update the profile information:
            http://127.0.0.1:8000/api/accounts/profile/?Authorization=Bearer IxswU7BBJKL7yXj88uwO7UsXGDm4lLm0

        content must be provided:(PUT)
            {
                "user": 11,
                "first_name": "Ram",
                "last_name": "Ram",
                "email": "Ram@gmail.com",
                "phone_no": "1234567890",
                "address": "123 Main Street",
                "profile_img": null
            }



4.    Handle Token Expiry:
        Implement a check for token expiration before making requests.
        If the access token is expired, use the refresh token to obtain a new access token by sending a POST request to the refresh endpoint (e.g., http://127.0.0.1:8000/api/token/refresh/).



5.    Logging Out:
        Provide a logout option in your frontend.
        When the user logs out, clear the stored tokens and optionally send a request to the logout endpoint (e.g., http://127.0.0.1:8000/api/accounts/auth/logout/).
        
            

6.    User Experience:
        Ensure to handle success and error responses gracefully. Inform users of the results of their actions (e.g., registration success, login failure, order placement).
        Maintain a user-friendly interface by displaying loading indicators during API requests and appropriate messages for various actions.


7.    To Handle orders:
        http://127.0.0.1:8000/api/orders/

        content must be provided:(POST)
            {
                "product_name": "Acer",
                "quantity": 5,
                "price": 450000.00
            }


8.    To see the specific order information:(GET)
        http://127.0.0.1:8000/api/orders/1/?

9.    To see the whole product History:(GET)
        http://127.0.0.1:8000/api/orders/history/

10.   For Payments:(POST)
        http://127.0.0.1:8000/api/orders/payments/

        content must be provided:
            {
                "order": 1,         // Order ID
                "amount": 1200.00
            }


11.   Update the status of the product after paymennt:
        http://127.0.0.1:8000/api/orders/payments/1/


        content must be provided:
        {
            "status": "completed"  // or "pending", "failed"
        }





Summary of Key Actions

    Register → Capture user details and call the registration API.
    Login → Get tokens and store them.
    Access APIs → Use the access token to interact with protected endpoints.
    Refresh Tokens → Manage token expiry.
    Logout → Clear tokens and optionally call the logout API.

This flow will allow users to interact with your backend APIs securely and effectively through your frontend application. Let me know if you have any questions or need further details!