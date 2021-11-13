

# Microservice with Django RestFrameWork

## Descripcion Y Contexto

Este proyecto esta desarrollando en el lengauje Pythonn usando el Framework de Django Rest. Se realizara un crud de Categorias, Productos e Items.


## Requeriments

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




# Category

## GET

List Category

Request body

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
   

