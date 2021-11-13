

# Microservice with Django RestFrameWork

### Descripcion Y Contexto

Este proyecto esta desarrollando en el lengauje Python usando el Framework de Django Rest. Se realizara un crud de Categorias, Productos e Items.


### Requeriments

- asgiref==3.4.1
- Django==3.2.9
- django-cors-headers==3.10.0
- django-simple-history==3.0.0
- djangorestframework==3.12.4
- gunicorn==20.1.0
- Pillow==8.4.0
- python-decouple==3.5
- pytz==2021.3
- sqlparse==0.4.2
- whitenoise==5.3.0




## Category

### GET

List Category

Request 

    --http://127.0.0.1:8000/petStore/category/
 
Response 
 
```
[
    {
        "id": 1,
        "description": "Large Angelfish"
    },
    {
        "id": 2,
        "description": "Dogs"
    },
  ]
```
    
 List Category By Id
 
 Request GET
 
    --http://127.0.0.1:8000/petStore/category/
    
Response

```
{
    "id": 2,
    "description": "Dogs"
}
   
 ```
   
### POST

Request 

```
  --http://127.0.0.1:8000/petStore/category/2/
  
   {
        "description": "CategoryExample"
    }

```

### DELETE

Request 

```
    http://127.0.0.1:8000/petStore/category/2/
    
```


## Product

### GET

List Products

Request 

    --http://127.0.0.1:8000/petStore/product/
    
Response

```
[
    {
        "id": 1,
        "name": "Angelfish",
        "description": "Aquatic animal",
        "categoy": 1
    },
    {
        "id": 2,
        "name": "ziberan",
        "description": "Aquatic animal",
        "categoy": 1
    }
]

```

List Product by Id


Request 

    --http://127.0.0.1:8000/petStore/product/1/
    
    
Response

```
{
    "id": 1,
    "name": "Angelfish",
    "description": "Aquatic animal",
    "categoy": 1
}

```


### POST 


Request
```
http://127.0.0.1:8000/petStore/product/1/

{
    "name": "Godzilla",
    "description": "Aquatic animal",
    "categoy": 2
}

```


##Item

### POST

Request 

```
      http://127.0.0.1:8000/petStore/item/

{
    "image": "/archivos/975de4e0-3832-4e57-a81c-53b11f847ee1.jpg",
    "description": "Large Angelfish2",
    "quantity": 30,
    "price": 2400.0,
    "product": 1
}
```
