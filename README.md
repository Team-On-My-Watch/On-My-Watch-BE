# Team Flamingo: On My Watch API
### Backend Engineers: Amanda McMullin and John Parrish

This repository is the API for a React web application called On My Watch. The API was built using Django and Django REST Framework, and allows users to recommend movies or television shows, see what their friends have recommended, and comment on recommendations.

## API Endpoints

Base URL: [https://onmywatch.herokuapp.com](https://onmywatch.herokuapp.com)

|                 | URL                                       |    Method    |                                   Function |
| :-------------: | :---------------------------------------- | :----------: | -----------------------------------------: |
|      Admin      | /auth/users/                              |     POST     |                                Create User |
| Authentication  | /auth/token/login/                        |     POST     |                                      Login |
|                 | /auth/token/logout/                       |     POST     |                                     Logout |
| Recommendations | /api/recommendation/                      |  GET, POST   | View Recommendation, Create Recommendation |
|                 | /api/recommendation/<int:pk>/             |     GET      |                     Recommendation Details |
|                 | /api/recommendation/<int:pk>/delete/      |    DELETE    |                     Delete Recommendations |
|    Comments     | /api/recommendation/<int:pk>/comment/     |  GET, POST   |              View Comments, Create Comment |
|    Followers    | /api/follows/                             |     POST     |                              Follow a User |
|                 | /api/myfollowers/                         |     GET      |                          List of Followers |
|                 | /api/following/                           |     GET      |            List of Users You Are Following |
|   Watch List    | /api/user/watchlist/recommendations/      |     GET      |          View User Favorite Recommendation |
|                 | /api/recommendation/<int:pk>/watchlist/   | POST, DELETE |            Add Favorites, Remove Favorites |
|  Watched List   | /api/watchedlist/                         |     GET      |                   View User's Watched List |
|                 | /api/recommendation/<int:pk>/watchedlist/ | POST, DELETE |           Add To, Remove From Watched List |
|      Tags       | /api/tags/                                |  GET, POST   |                      View Tags, Create Tag |
|                 | /api/tag/<int:pk>/delete/                 |    DELETE    |                                Delete Tags |
|      Users      | /api/user/<int:pk>/recommendations/       |     GET      |             View All Users Recommendations |
|      Search     | /api/search/recommendations/?search=      |     GET      |      Search All Recommendations Title/Desc |
|                 | /api/search/movie/recommendations/?search=|     GET      |Search All Moive Recommendations Title/Desc |
|                 | /api/search/tvs/recommendations/?search=  |     GET      |  Search All TVS Recommendations Title/Desc |




### Register
> /auth/users/
- Method: POST
- Data JSON:

```python
{
    "username": "<username>",
    "password": "<password>"
}
```

- Response: User JSON Object


### Login
> /auth/token/login/
- Method: POST
- Data JSON:

```python
{ 
	"username": "<username>", 
	"password": "<password>" 
}
```

- Response: Example Authentication Token

```python
{
	"auth_token": "a0b8f9382584861a9ad9bc54cd63649f8df4f3c9"
}
```


### Logout
> /auth/token/logout/
- Method: POST

- Data: Authentication Token (See Example Authentication Token in Login section)

- Response: No Data


### View All Recommendations
> /api/recommendation/
- Method: GET
- Response: 200_OK, Array of all recommendations


### Create Recommendation
> /api/recommendation/
- Method: POST
- Data JSON: Example

```
{
	"id": 4,
	"user": "amanda",
	"user_info": {
		"id": 7,
		"username": "amanda"
	},
	"reason": "Bob Odenkirk is incredible....yet again.",
	"saved_by": [],
	"imdbid": "abqnmluvn1",
	"title": "Nobody",
	"medium": "M",
	"genre": "Drama",
	"tag": [],
	"description": "Bob Odenkirk is the only person that could ever play this role and make it so believable and so good. The fight scene on the bus, with Sammy Davis Jr. playing in the background...chef's kiss.",
	"streaming_service": null,
	"poster": null,
	"created_at": "2022-08-21T02:07:42.492664Z"
}
```

Response: 201_Created


### Recommendation Detail
> /api/recommendation/int:pk/
- Method: GET
- The URL pk identifies the recommendation for which to return details
- Response: 200_OK, Array of details for recommendation specified in URL


### Delete Recommendation
> /api/recommendation/int:pk/delete/
- Method: DELETE 
- The pk in the URL above identifies the recommendation you wish to delete
- Response: 204_NO_CONTENT

### Follow a User
> /api/follows/
- Method: POST

### Unfollow a User
> /api/follows/<int:pk>/delete
- Method: DELETE
- The pk in the URL above refers to the id number of the following relationship you wish to delete. 
- Response: 204_NO_CONTENT

### List of Followers
> /api/myfollowers/
- Method: GET

### List of Users You Are Following
> /api/following/
- Method: GET
- 
### View User's Favorite Recommendations
> /api/user/watchlist/recommendations/
- Method: GET
- 
### Add Favorites
> /api/recommendation/int:pk/watchlist/
- Method: POST
- 
### Remove Favorites
> /api/recommendation/int:pk/watchlist/
- Method: DELETE

### View User's Watched List
> /api/watchedlist/  
- Method: GET

### Add to Watched List
> /api/recommendation/<int:pk>/watchedlist/
- Method: POST
-

### Remove from Watched List
> /api/recommendation/<int:pk>/watchedlist/
- Method: DELETE
-

### View Tags
> /api/tags/
- Method: GET
- 
### Create Tag
> /api/tags/
- Method: POST
- 
### Delete Tag
> /api/tag/int:pk/delete/
- Method: DELETE
- 
### View All Users Recommendations
>/api/user/int:pk/recommendations/
- Method: GET
- 




# Running a local PostgreSQL database

### Clone the API repository
```bash
git clone https://github.com/Team-On-My-Watch/On-My-Watch-BE.git
```

### Install project dependencies
This project uses [Python 3.10](https://www.python.org/).

Use [pipenv](https://pypi.org/project/pipenv/) to run a virtual enviroment with all the project dependencies.

Activate a vitual enviroment:
```bash
pipenv shell
```

Install dependencies:
```bash
pipenv install
```

### Create a local PostgreSQL database
This project uses [PostgreSQL 14.4](https://www.postgresql.org/).

Install PostgreSQL:
```bash
brew install postgresql
```

Start PostgreSQL:
```bash
brew services start postgresql
```

When creating a local database, it is generally considered good practice to use the same name for username and database name.

Create a user:
```bash
createuser -d <username>
```

Create a database:
```bash
createdb -U <username> <dbname>
```

### Configure Django to connect to your local database
Install a Python PostgreSQL adapter:
```bash
pipenv install psycopg2-binary
```

Create a .env file in /core directory:
```bash
touch ./core/.env
```

Refer to .env for how to configure your local copy of .env. Include a database url with the following syntax:
```bash
DATABASE_URL=postgres://<username>:@127.0.0.1:5432/<dbname>
```

### Run your local server
```bash
python manage.py runserver
```

### Database tools
[Postico](https://eggerapps.at/postico/) and [Dbeaver](https://dbeaver.io/) are great tools to that provide a GUI to interact with your database. [Insomnia](https://insomnia.rest/products/insomnia) is a great way to query your server, whether local or remote. All three are available on Homebrew.
