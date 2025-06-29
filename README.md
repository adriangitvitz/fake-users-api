## Generate Fake Users

Returns fake users using `faker` python library in the same JSON format as [https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users). 
It returns valid and invalid emails to explore validation, and supports pagination.

```json
{
    "id": "471b9b0f",
    "name": "Michael Kirby",
    "username": "imorgan",
    "email": "imorgan!@mendo.co",
    "address": {
      "street": "Rebecca Heights",
      "suite": "Apt. 446",
      "city": "Mira Mesa",
      "zipcode": "94944",
      "geo": {
        "lat": "32.9156",
        "lng": "-117.1439"
      }
    },
    "phone": "(734)429-1384x982",
    "website": "preston-ingram.info",
    "company": {
      "name": "Mendoza-Smith",
      "catchPhrase": "Fully-configurable tangible knowledge user",
      "bs": "utilize user-centric convergence"
    }
}
```

### Usage

```shell
uv sync
```

```shell
fastapi dev users_api/main.py
```

### Endpoint

```shell
curl http://localhost:8000/users?page=1
```
