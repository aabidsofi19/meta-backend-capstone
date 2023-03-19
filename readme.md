# users 

|username  |   password    |  role   |
| -------- | ------------ | -------- |
|employee  | employee123 | superadmin|
|user1     |bigpassword123 | user    |


# views 

`restaurant/views.py` contains all the view sets 


# endpoints

## restaurant urls in (restaurant/urls.py)
/restaurant/menu/items          <== GET , POST  
/restaurant/menu/<int:pk>  <== GET , PUT , DELETE 
/restaurant/booking/tables       <== Get , PUT , POST , DELETE 

## auth urls in (./littlelemon/urls.py) 
/auth                      <== Djoser Urls   
/api-token-auth            <== rest-framework token auth


# tests 

## test files are in ./tests folder ( of project root not restaurant app )

`test_models.py` contains test for models
`test_views.py`  contains tests for views 

run `python manage.py test` to run them 




