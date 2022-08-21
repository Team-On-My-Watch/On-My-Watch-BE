*** ~ OLD INFO FROM LAST PROJECT  - USE AS TEMPLATES ~ *** 

### List Answers / Create Answer
> /api/questions/int:pk/answer/
- List Answers:
  - Method: GET
  - The URL pk identifies the question whose answers will return
  - Response: 200_OK, Array of answers for question specified in URL

- Create Answer:
  - Method: POST
  - The URL pk identifies the question being answered
  - Data JSON: Example

```
{
"answer_body": "your sample answer here"	
}
```
_
  - Response: 201_Created





### Star Question / Unstar Question
> /api/questions/int:pk/star
- Methods: star- POST, unstar - DELETE


### Delete Question
> /api/questions/int:pk/trash
- Method: DELETE 
- The pk in the URL above identifies the question you wish to delete
- Response: 204_NO_CONTENT


### Star Answer / Unstar Answer
> /api/answers/int:pk/star
- Methods: star- POST, unstar - DELETE


### List User's Questions and Answers
> /api/myquestions/
- Method: GET
- Response: 200_OK, Array of all questions and answers created by specific user
