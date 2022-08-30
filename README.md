# Team Flamingo: On My Watch API
### Backend Engineers: Amanda McMullin and John Parrish

This repository is the API for a React web application called On My Watch. The API was built using Django and Django REST Framework, and allows users to recommend movies or television shows, see what their friends have recommended, and comment on recommendations.

## API Endpoints

Base URL: [https://onmywatch.herokuapp.com](https://onmywatch.herokuapp.com)

|             Type              | URL                                       |    Method    |                                Description |
| :---------------------------: | :---------------------------------------- | :----------: | -----------------------------------------: |
|        Authentication         | /auth/users/                              |     POST     |                                Create User |
|        Authentication         | /auth/token/login/                        |     POST     |                                      Login |
|        Authentication         | /auth/token/logout/                       |     POST     |                                     Logout |
|     Profile Image Upload      | /api/upload/                              |    PATCH     |                  Add Image for User Avatar |
|        Recommendations        | /api/recommendation/                      |  GET, POST   | View Recommendation, Create Recommendation |
|        Recommendations        | /api/recommendation/<int:pk>/             |     GET      |                     Recommendation Details |
|        Recommendations        | /api/recommendation/<int:pk>/delete/      |    DELETE    |                     Delete Recommendations |
|           Comments            | /api/recommendation/<int:pk>/comment/     |  GET, POST   |              View Comments, Create Comment |
|           Followers           | /api/follows/                             |     POST     |                              Follow a User |
|           Unfollow            | /api/follows/<int:pk>/delete              |    DELETE    |                            Unfollow a User |
|       List of Followers       | /api/myfollowers/                         |     GET      |                          List of Followers |
| List of Who User is Following | /api/following/                           |     GET      |            List of Users You Are Following |
|          Watch List           | /api/user/watchlist/recommendations/      |     GET      |          View User Favorite Recommendation |
|          Watch List           | /api/recommendation/<int:pk>/watchlist/   | POST, DELETE |            Add Favorites, Remove Favorites |
|         Watched List          | /api/watchedlist/                         |     GET      |                   View User's Watched List |
|         Watched List          | /api/recommendation/<int:pk>/watchedlist/ | POST, DELETE |           Add To, Remove From Watched List |
|             Tags              | /api/tags/                                |  GET, POST   |                      View Tags, Create Tag |
|             Tags              | /api/tag/<int:pk>/delete/                 |    DELETE    |                                Delete Tags |
|             Users             | /api/user/<int:pk>/recommendations/       |     GET      |             View All Users Recommendations |
|         Search - All          | /api/search/recommendations/?search=      |     GET      |      Search All Recommendations Title/Desc |

## Search Endpoint

Base Search URL [https://onmywatch.herokuapp.com/api/recommendation/]

|        Type         | URL                                                                    | Method |                             Description |
| :-----------------: | :--------------------------------------------------------------------- | :----: | --------------------------------------: |
|    Search - User    | /api/search/recommendations/?user=                                     |  GET   |     Search All Recommendations by Users |
|   Search - Medium   | /api/search/recommendations/?medium=                                   |  GET   | Search All Recommendations by Movie/TVS |
|    Search - Tag     | /api/search/recommendations/?tag=                                      |  GET   |      Search All Recommendations by Tags |
|       Search        | /api/search/recommendations/?search=                                   |  GET   |           Search All Recommendations by |
| Fields to search by | Title, Description, imdbid, Keywords, Genre, Streaming service, Reason |


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
	"password": "<password>",
	"username": "<username>"
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


### User Image Upload
> /api/upload/
- Method: PATCH
- Data: Binary file containing image file
- Headers and Values: 
  - Header: Content-Type, Value: image/extension_type 
    - example: Content-Type image/jpeg
  - Header: Content-Disposition, Value: attachment; filename=<name.ext> 
    - example: Content-Disposition attachment; filename=selfie.jpeg
- Response: 206 Partial Content / Response will contain link to the image uploaded on Amazon AWS


### View All Recommendations
> /api/recommendation/
- Method: GET
- Response: 200 OK / Array of all recommendations


### Create Recommendation
> /api/recommendation/
- Method: POST
- Data JSON: Example

```
{
	"reason": "Bob Odenkirk is incredible....yet again.",
	"saved_by": [],
	"watched_by": [],
	"imdbid": "abqnmluvn1",
	"title": "Nobody",
	"medium": "M",
	"genre": "Drama",
	"tag": [],
	"description": "Bob Odenkirk is the only person that could ever play this role and make it so believable and so good. The fight scene on the bus, with Sammy Davis Jr. playing in the background...chef's kiss."
}
```

Response: 201 Created / Array of all the recommendation data


### Recommendation Detail
> /api/recommendation/int:pk/
- Method: GET
- The pk in the URL above identifies the recommendation for which to return details
- Response: 200 OK / Array of details for recommendation specified in URL


### Delete Recommendation
> /api/recommendation/int:pk/delete/
- Method: DELETE 
- The pk in the URL above identifies the recommendation you wish to delete
- Response: 204 No Content


### View Comments for a Recommendation
> /api/recommendation/int:pk/comment/
- Method: GET
- The pk in the URL above identifies the recommendation for which you want to see comments
- Response: 200 OK / Array of comments for recommendation specified in URL


### Create a Comment for a Recommendation
> /api/recommendation/int:pk/comment/
- Method: POST
- Data JSON:

```python
{ 
	"recommendation": <int/pk>,
	"comment": "<Your comment.>"
}
```
- Response: 201 Created / Array containing user id, username, recommendation pk, comment, and created at date and time

### Follow a User
> /api/follows/
- Method: POST
- Data JSON:

```python
{ 
	"followee": pk
}
```
- Response: 201 Created / Follow relationship JSON object


### Unfollow a User
> /api/follows/<int:pk>/delete
- Method: DELETE
- Response: 204 No Content


### List of Followers
> /api/myfollowers/
- Method: GET
- Response: 200 OK / Array of users following your account


### List of Users You Are Following
> /api/following/
- Method: GET
- Response: 200 OK / Array of users you are following


### View User's Watch List 
> /api/user/watchlist/recommendations/
- Method: GET
- Response: 200 OK / Array of all shows on user's watch list


### Add Show to Watch List
> /api/recommendation/int:pk/watchlist/
- Method: POST
- Data: the pk in the URL above refers to the pk of the show to add to the watch list
- Response: 201 Created / Array containing user and show data


### Remove Show from Watch List
> /api/recommendation/int:pk/watchlist/
- Method: DELETE
- Data: The pk in the URL above refers to the pk of the show to be removed from watch list 
- Response: 204 No Content


### View User's Watched List
> /api/watchedlist/  
- Method: GET
- Response: 200 OK / Array of all shows on user's watched list
  

### Add to Watched List
> /api/recommendation/int:pk/watchedlist/
- Method: POST
- Data: the pk in the URL above refers to the pk of the show to add to the watched list
- Response: 201 Created / Array containing user and show data


### Remove from Watched List
> /api/recommendation/int:pk/watchedlist/
- Method: DELETE
- Data: The pk in the URL above refers to the pk of the show to be removed from watched list 
- Response: 204 No Content


### View Tags
> /api/tags/
- Method: GET
- Response: 200 OK / Array of all tag id's and names


### Create Tag
> /api/tags/
- Method: POST
- Data JSON:

```python
{
	"tags": "time travel"
}
```
- Response: 201 Created / Array containing tag id and name


### Delete Tag
> /api/tag/int:pk/delete/
- Method: DELETE
- Data: The pk in the URL above refers to the pk of the tag you wish to delete
- Response: 204 No Content


### View All Users Recommendations
>/api/user/int:pk/recommendations/
- Method: GET
- Data: the pk in the URL above refers to the pk of the user from whom you wish to see recommendations
- Response: 200 OK / Array of all recommendations by the user



# Running a local PostgreSQL database

### Clone the API repository
```bash
git clone https://github.com/Team-On-My-Watch/On-My-Watch-BE.git
```

### Install project dependencies
This project uses [Python 3.10](https://www.python.org/).

Use [pipenv](https://pypi.org/project/pipenv/) to run a virtual environment with all the project dependencies.

Activate a virtual environment:
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
