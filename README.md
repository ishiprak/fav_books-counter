# Bookish (Favourite-Books-Manager)
<p>A Library management REST API service with JWT authentication, User Registration and Authorization functionalities built using Django web framework.</p>
This program uses different Python packages, libraries and the Django Web-framework as well as JWT (JSON Web Token) Authentication to encapsulate the functionalities of a REST API service as well as a web-based utility.

## Setup and Running of the program -
* On your computer, clone this repository or download the zip files and extract it.
* To download and install all the dependencies and sub-dependencies to run this program, use "`pip install -r requirtements.txt`" command in your terminal from the root fo the git downloaded or cloned file.
* After the extraction, move to the "src" directory, which is the root directory for the actual executable files.
* To use the REST API service you can run "`python manage.py runsercver`" command in your terminal to run a localhost server to utilise the REST service on your computer, and send GET/POST/PUT/DELETE requests on the mentioned url in the terminal for the server to use the REST API service for `Bookish`.
* To create or register your user account to generate JWT token send a POST request to the "https://localhost:<your_port_for_server>/books/api/token/register/" with request body of `username`, `email`, `password`, and `password2` parameters. This step will create or register your account to the REST API service of `Bookish` and then you can move to the next step to generate your pair of JWT tokens to use the service.
* To generate the token via login send a POST request to the "https://localhost:<your_port_for_server>/books/api/token/" with request body of `username` and `password` parameters. For this request the REST service will generate a response with JSON object for JWT pair of `Access Token` and `Refresh token` to use while accessing the REST API service of `Bookish`.
* To generate a new `Access Token`, you can use the `Refresh Token` and send a POST request to the "https://localhost:<your_port_for_server>/books/api/token/" with request body of `Refresh` token with parameter value of the actual Refresh Token provided after generation of your JWT pair of tokens. This will generate a response with with JSON object for new `Access Token` to use while accessing the REST API service of `Bookish`.

## Use cases of the REST API service for `Bookish` -
* To create new books send a a POST request to the "https://localhost:<your_port_for_server>/books/api/token/" with request body of `Refresh` token with parameter value of the actual Refresh Token provided after generation of your JWT pair of tokens. This will generate a response with with JSON object for new `Access Token` to use while accessing the REST API service of `Bookish`.



