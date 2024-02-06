# JB.28.01.dj1 Django Product Application

## Setup Instructions

1. **Clone the Repository:**

   git clone 

2. **Create Virtual Environment:**

    ```bash
    python -m venv venv

3. **Activate Virtual Environment:**

    ### On Windows:
        venv\Scripts\activate

    ### On macOS/Linux:
        source venv/bin/activate

4. **Install Dependencies:**

        pip install -r requirements.txt

5. **Apply Database Migrations:**

        python manage.py migrate

6. **Run the Development Server:**

        python manage.py runserver

7. **Launch on live server dashboard.html**

# Usage
## Register:

 - Open the application in your web browser.
- Click on the "Log In" button to go to the login page.
- If you don't have an account, click on the "Register" link to create a new account.
- Fill in the registration form with your username, email, and password.
- After registration, you will be redirected to the login page.

## Log In:

 - Use your registered username and password to log in.

## Add Products:

 - On the protected page, you can add products using the provided form.
 - Enter the product description, price, and choose an image file.
 - Click the "Add Product" button to submit the form.

## View Products:

 - The added products will be displayed on the page with their details.
 - You can see the product ID, description, price, and the time it was created.
 - Each product card also includes a "Del" button to delete the respective product.
## Delete Products:

 - Click the "Del" button on a product card to delete that product.
 - The product will be removed from the list.