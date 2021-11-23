# Examples of curl requests

1. Authentication
> curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin12345"}' 
> http://localhost:8000/login/
 
2. Create new survey
> curl -X POST -H "Content-Type: application/json" -H  "Authorization: Token 19af1a84a22b01595cf99dc61261877ec2189268" 
> -d '{"name": "test1567", "end_date": "2025-01-11", "description": "New survey"}' http://127.0.0.1:8000/surveys/add/

3. Edit existing survey
> curl -X POST -H "Content-Type: application/json" -H  "Authorization: Token 19af1a84a22b01595cf99dc61261877ec2189268" 
> -d '{"id": 1, "name": "test edit", "end_date": "2025-01-11", "description": "Edited survey"}' 
> http://127.0.0.1:8000/surveys/edit/

4. Delete survey
> curl -X POST -H "Content-Type: application/json" -H  "Authorization: Token 19af1a84a22b01595cf99dc61261877ec2189268" 
> -d '{"id": 2}' http://127.0.0.1:8000/surveys/delete/

5. Get list of available surveys
> curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/surveys/

5. Add a new question
> curl -X POST -H "Content-Type: application/json" -H  "Authorization: Token 19af1a84a22b01595cf99dc61261877ec2189268" 
> -d '{"survey_id": 1, "text": "Ask something", "type": 1}' http://127.0.0.1:8000/questions/add/

6. Edit the question:
> curl -X POST -H "Content-Type: application/json" -H  "Authorization: Token 2e5f8795c5780d83f8fe95d1dfe247aae06dc9e6" 
> -d '{"id": 1, "survey": "2", "text": "Edited question", "type": "2"}' http://127.0.0.1:8000/questions/edit/

7. Delete the question:
> curl -X POST -H "Content-Type: application/json" -H  "Authorization: Token 2e5f8795c5780d83f8fe95d1dfe247aae06dc9e6" 
> -d '{"id": 5}' http://127.0.0.1:8000/questions/delete/

8. Get question list by survey 
> curl -X POST -H "Content-Type: application/json" -H  "Authorization: Token 2e5f8795c5780d83f8fe95d1dfe247aae06dc9e6" 
> -d '{"survey": 1}' http://127.0.0.1:8000/questions/

9. Add response to question:
> curl -X POST -H "Content-Type: application/json" -H  "Authorization: Token 2e5f8795c5780d83f8fe95d1dfe247aae06dc9e6" 
> -d '{"person_id": 100, "answer": "A", "question": 1}' http://127.0.0.1:8000/responses/add/

10. Get info about surveys by user
> curl -X POST -H "Content-Type: application/json" -H  "Authorization: Token 2e5f8795c5780d83f8fe95d1dfe247aae06dc9e6" 
> -d '{"person_id": 1}' http://127.0.0.1:8000/responses/


