# Team Flamingo: On My Watch API
### Backend Engineers: Amanda McMullin and John Parrish

This repository is the API for a React web application called On My Watch. The API was built using Django and Django REST Framework, and allows users to recommend movies or television shows, see what their friends have recommended, and comment on recommendations.

## API Endpoints

Base URL: [https://onmywatch.herokuapp.com](https://onmywatch.herokuapp.com)

| URL                                     |    Method    |                                   Function |
| :-------------------------------------- | :----------: | -----------------------------------------: |
| /auth/users/                            |     POST     |                                Create User |
| /auth/token/login/                      |     POST     |                                      Login |
| /auth/token/logout/                     |     POST     |                                     Logout |
| /api/recommendation/                    |  GET, POST   | View Recommendation, Create Recommendation |
| /api/recommendation/<int:pk>/comment/   |  GET, POST   |              View Comments, Create Comment |
| /api/users/follow/                      |     POST     |                                Follow User |
| /api/user/watchlist/recommendations/    |     GET      |          View User Favorite Recommendation |
| /api/recommendation/<int:pk>/watchlist/ | POST, DELETE |            Add Favorites, Remove Favorites |
| /api/recommendation/<int:pk>/delete/    |    DELETE    |                     Delete Recommendations |
| /api/tags/                              |  GET, POST   |                      View Tags, Create Tag |
| /api/tag/<int:pk>/delete/               |    DELETE    |                                Delete Tags |
