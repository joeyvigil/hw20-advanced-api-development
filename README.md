# hw20-advanced-api-development
*following along with the practice assignments your Mechanic API*

![image](Mechanic_shop_pic.png)

## Rate Limiting and Caching
-   Using the Flask-Limiter package, have a rate limit applied to at least one route in your API
-   Using the Flask-Caching package, have implemented caching on at least on route in your API

**(Additional Optional Challenge):** Apply a default rate limit to your project, offering blanket protection to all routes. Feel free to dive into the Flask-Limiter docs to figure this out: <https://flask-limiter.readthedocs.io/en/stable/>

## Token Authentication
*requires python-jose package*
-   Create an encode_token function that takes in a mechanic_id to create a token specific to that user.
-   login_schema, which can be made by excluding all fields except email and password from your MechanicSchema
-   In your customer blueprint, create a login route:
-   ---- **POST '/login'** : passing in email and password, validated by login_schema
-   ---- After credentials have been validate utilizes the encode_token() function to make a token to be returned to that customer.
-   Create @token_required wrapper, that stores the mechanic_id from the token, in the request.
-   Create a route that requires a token, that returns the service_tickets related to that mechanic.
-   ---- **GET '/my-tickets'**: requires a Bearer Token authorization.
-   ---- The route function should receive the customer_id from the @token_required wrapper.
-   ---- Using that id query the service_tickets where the customer_id is equal to the id passed in.
-   Additionally add @token_required to any routes you think should require authorization. (ex: Update, Delete,...)

## Advanced Queries: (JUST ONE)
-   Add an update route to your service_ticket blueprint to add and remove mechanics from a ticket.
-   ---- Use id's to look up the mechanic to append or remove them from the ticket.mechanics list
-   Create an endpoint in mechanics blueprint that returns a list of mechanics in order of who has worked on the most tickets
-   Apply Pagination to GET Customers route.

## Inventory Model
**Assignment Continuation:** Incorporating a new resource to the API, we are now going to track inventory.

Create a new Inventory model in models.py which includes the following fields:
-   id: Unique Identifier
-   name: Part name
-   price: float value (price of the part)

## Many-to-Many Relationship
Establish a many-to-many relationship from Inventory to ServiceTicket, as One ticket can require many parts, and the same kind of part can be used on many different tickets.

The junction table does not have to support any additional fields, and can be a simple table object similar to your service_mechanic table.

**(Additional Optional Challenge)**: Make the junction table a Model object with additional field of quantity.

## Parts Blueprint
Create a new folder in blueprints for Inventory:
-   Initialize the blueprint (don't forget to import routes under the blueprint initialization)
-   Register the blueprint with a url_prefix = '/parts'
-   Create a Schema for Parts (use SQLAlchemyAutoSchema to generate schema from Parts Model and PartDescription Model)

## Inventory Routes
For inventory implement basic CRUD routes to Create, Read, Update, and Delete parts stored in our inventory.

### Create
```json
method: POST
url: http://127.0.0.1:5000/inventory
body (raw, JSON):
{    
    "name": "speaker",
    "price": "20",
    "quantity": "10"
}
response:
{
    "id": 1,
    "name": "speaker",
    "price": 20,
    "quantity": 10
}
```

### Read
```json
method: GET
url: http://127.0.0.1:5000/inventory
response:
[
    {
        "id": 1,
        "name": "speaker",
        "price": 20,
        "quantity": 10
    },
    {
        "id": 2,
        "name": "front bumper",
        "price": 120.25,
        "quantity": 2
    }
]
```

```json
method: GET
url: http://127.0.0.1:5000/inventory/1
response:
{
    "id": 1,
    "name": "speaker",
    "price": 20,
    "quantity": 10
}
```

### Update
```json
method: PUT
url: http://127.0.0.1:5000/inventory/1
body (raw, JSON):
{
    "name": "pioneer speakers 6.5 inch",
    "price": 25.00,
    "quantity": 42
}
response:
{
    "id": 1,
    "name": "pioneer speakers 6.5 inch",
    "price": 25,
    "quantity": 42
}
```

### Delete
```json
method: DELETE
url:http://127.0.0.1:5000/inventory/1
response:
{
    "message": "Successfully deleted inventory 1"
}
```


### Additionally Create a route in the service_ticket blueprint to add a single part to an existing Service Ticket
```json
method: POST
url: http://127.0.0.1:5000/ticket_inventory/1/assign-inventory/1
Authorization (Bearer Token): eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTY4MjY0OTksImlhdCI6MTc1NjgyMjg5OSwic3ViIjoiMiJ9.XNhCt0Uq-TVgCSBFS6v24AuxG824TCHjczzG3Gw14pU
response:
{
    "id": 1,
    "inventory_id": 1,
    "ticket_id": 1
}
```

## Testing and Submission
Test all routes in Postman to ensure each endpoint works as designed. In Postman add every test request to a collection, and export that collection to your API project folder. Push your work to Github and submit the link to the GitHub repo.