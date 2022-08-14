# Team Flamingo: On My Watch API
### Backend Engineers: Amanda McMullin and John Parrish

This repository is the API for a React web application called On My Watch. The API was built using Django and Django REST Framework, and allows users to recommend movies or television shows, see what their friends have recommended, and comment on recommendations.

## API Endpoints

Base URL: [https://onmywatch.herokuapp.com](https://onmywatch.herokuapp.com)

| URL                             |  Method   |                                   Function |
| :------------------------------ | :-------: | -----------------------------------------: |
| /auth/users/                    |   POST    |                                Create User |
| /auth/token/login/              |   POST    |                                      Login |
| /auth/token/logout/             |   POST    |                                     Logout |
| /api/recommendation/            | GET, POST | View Recommendation, Create Recommendation |
| /api/recommendation/pk/comment/ | GET, POST |              View Comments, Create Comment |
