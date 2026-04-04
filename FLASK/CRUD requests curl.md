#### Inserting a record using curl
curl --header "Content-Type:  application/json"  \
--request POST  \
--data '{"username": "luciocosta", "password":  "123456", "name": "Lucio Costa"}'  \
localhost:5000/users/insert

#### Deleting a record using curl
curl --request DELETE localhost:5000/users/delete/luciocosta


#### Updating a record using curl
curl -X PUT localhost:5000/users/update/luciocosta \
-H "Content-Type: application/json" \
-d '{"name": "Lucio Costa Atualizado"}'