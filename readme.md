# users 

|username  |   password    |  role   |
| -------- | ------------ | -------- |
|employee  | employee123 | superadmin|
|user1     |bigpassword123 | user    |


# endpoints

/restaurant/menu           <== GET , POST  
/restaurant/menu/<int:pk>  <== GET , PUT , DELETE 
/restaurant/booking        <== Get , PUT , POST , DELETE 
/auth                      <== Djoser Urls
/api-token-auth            <== rest-framework token auth
