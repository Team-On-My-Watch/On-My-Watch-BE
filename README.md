# Team Flamingo: On My Watch API
### Backend Engineers: Amanda McMullin and John Parrish

This repository is the API for a React web application called On My Watch. The API was built using Django and Django REST Framework, and allows users to recommend movies or television shows, see what their friends have recommended, and comment on recommendations.

## API Endpoints

Base URL: [https://onmywatch.herokuapp.com](https://onmywatch.herokuapp.com)

|                 | URL                                     |    Method    |                                   Function |
| :-------------: | :-------------------------------------- | :----------: | -----------------------------------------: |
|      Admin      | /auth/users/                            |     POST     |                                Create User |
| Authentication  | /auth/token/login/                      |     POST     |                                      Login |
|                 | /auth/token/logout/                     |     POST     |                                     Logout |
| Recommendations | /api/recommendation/                    |  GET, POST   | View Recommendation, Create Recommendation |
|                 | /api/recommendation/<int:pk>/           |     GET      |                     Recommendation Details |
|                 | /api/recommendation/<int:pk>/delete/    |    DELETE    |                     Delete Recommendations |
|    Comments     | /api/recommendation/<int:pk>/comment/   |  GET, POST   |              View Comments, Create Comment |
|    Followers    | /api/follows/                           |     POST     |                              Follow a user |
|                 | api/myfollowers/                        |     GET      |                          List of Followers |
|                 | api/following/                          |     GET      |            List of Users You Are Following |
|   Watch List    | /api/user/watchlist/recommendations/    |     GET      |          View User Favorite Recommendation |
|                 | /api/recommendation/<int:pk>/watchlist/ | POST, DELETE |            Add Favorites, Remove Favorites |
|      Tags       | /api/tags/                              |  GET, POST   |                      View Tags, Create Tag |
|                 | /api/tag/<int:pk>/delete/               |    DELETE    |                                Delete Tags |
|      Users      | api/user/<int:pk>/recommendations/      |     GET      |             View All Users Recommendations |
