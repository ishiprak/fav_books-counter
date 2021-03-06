# Bookish (Library-Management-System-cum-REST-API-Service)

A Library management system used as **`REST API service`** with **`JWT Authentication`**, User Registration and Authorization functionalities built using **`Django`** web framework.
This program uses different Python packages, libraries and the Django Web-framework as well as JWT (JSON Web Token) Authentication to encapsulate the functionalities of a REST API service as well as a web-based utility.


## Setup and Execution of the program -


* On your computer, clone this repository or download the zip files and extract it.

* To download and install all the dependencies and sub-dependencies to run this program, use "`pip install -r requirtements.txt`" command in your terminal from the root of the downloaded or cloned git file.

* After the extraction, move to the "src" directory, which is the root directory for the actual executable files.

* To use the REST API service you can run "`python manage.py runserver`" command in your terminal to run a localhost server to utilise the REST service on your computer, and send `GET/POST/PUT/DELETE` requests on the mentioned url in the terminal for the server to use the REST API service for `Bookish`.

* To create or register your user account to generate JWT token, send a POST request to the `https://localhost:<your_port_for_server>/books/api/token/register/` with request body of `username`, `email`, `password`, and `password2` parameters. This step will create or register your account to the REST API service of `Bookish` and then you can move to the next step to generate your pair of JWT tokens to use the service.

* To generate the token via login, send a POST request to the `https://localhost:<your_port_for_server>/books/api/token/` with request body of `username` and `password` parameters. For this request the REST service will generate a response with JSON object for JWT pair of `Access Token` and `Refresh token` to use while accessing the REST API service of `Bookish`.

* To generate a new `Access Token` on expiry, you can use the `Refresh Token` and send a POST request to the `https://localhost:<your_port_for_server>/books/api/token/` with request body of `Refresh` token with parameter value of the actual Refresh Token provided after generation of your JWT pair of tokens. This will generate a response with with JSON object for new `Access Token` to use while accessing the REST API service of `Bookish`.




## Use cases of the REST API service for `Bookish` -


>  **For any request to the `Bookish` REST API service for creating / accessing / updating / deleting the books, always use request header with `header['Authorization'] = 'Bearer <your_JWT_access_token>'` for Token verification and Authorization.**



* To **`Create`** new books, send a POST request to the `https://localhost:<your_port_for_server>/books/books/` with request body of `title`, `author`, `genre`, and `amazon_url` parameters with values as per your book specifications. This will register your book in the Library management system which you can access later for reading / updating / deleting through the REST API service of `Bookish`.

* To **`Access / Read`** a list of all the books with specifications in the library system, send a GET request to the `https://localhost:<your_port_for_server>/books/books/`, which will generate a response with JSON data of all the books available in the `Bookish`.

* To **`Access / Read`** a particular book in the library system, send a GET request to the `https://localhost:<your_port_for_server>/books/books/<book_id>`, where the <book_id> will be a numerical integer from 1 to n, for n books in the library , in the order of book registration while creating the library. This request will generate a response with JSON data of all the books available in the `Bookish`.

* To **`Update`** a particular book in the library system, send a PUT request to the `https://localhost:<your_port_for_server>/books/books/<book_id>`, where the <book_id> will be a numerical integer from 1 to n, for n books in the library , in the order of book registration while creating the library, with request body of `title`, `author`, `genre`, and `amazon_url` parameters with values as per your new book specifications. All the parameters are optional to use as per your update requirements. This will update your current book specifications with the new paameters in the Library management system which you can access later for reading / updating / deleting through the REST API service of `Bookish`.

* To **`Delete`** a particular book in the library system, send a DELETE request to the `https://localhost:<your_port_for_server>/books/books/<book_id>`, where the <book_id> will be a numerical integer from 1 to n, for n books in the library , in the order of book registration while creating the library. This will delete your current book from the Library management system  and hence this book will not be available for accessing later for reading / updating / deleting through the REST API service of `Bookish`.




