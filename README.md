# API Info

This is a simple API created with Python and Flask. <br>
This API use GET and POST methods for differents routes.

**GET**

- http://0.0.0.0:3000/api/v1/server/server-status
- http://0.0.0.0:3000/api/v1/server/timeout

**POST**

- http://0.0.0.0:3000/api/v1/test/post-test

>Any other query to an incorrect route will be display an error message like this
```json
{
  "error": "Not found"
}
``` 

<br>

---

## How to run

Running on Docker

```sh
$ docker run -d --name api-test -p 3000:3000 conejado/api-test
```

<br>

Running on Kubernetes

```sh
$ git clone https://github.com/coneking/api-test.git
$ kubectl apply -f api-test/k8s
```
<br>

----

## How to use

If you running on docker, you can consume the api as shown below.
<br>

### GET 

The first path (server-status) show the json message `{"status": "running"}`.

```sh
$ curl http://0.0.0.0:3000/api/v1/server/server-status
{
  "status": "running"
}
```

<br>

The second path (timeout) will be display a json message after 3 minutes to simulate a 504 time-out error

```sh
$ curl http://0.0.0.0:3000/api/v1/server/timeout
{
  "time": "So slow... more than 3 minutes"
}
```

<br>

### POST

The following path will return the message sent in json format.

```sh
$ curl -X POST -d '{"Species": {"name": "Charmander", "ID": "4"}, "Type": {"name": "fire"}}' -H "Content-Type: application/json" http://0.0.0.0:3000/api/v1/test/post-test
{
  "Species": {
    "ID": "4", 
    "name": "Charmander"
  }, 
  "Type": {
    "name": "fire"
  }
}
```