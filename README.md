# cleverspace.io_event_scheduler
## Application includes
- Django rest api as backend
- used normal django to render the home page and also used python reqests to comunicate it with backend api
- used javascript and ajax for Crud operation on task 

## Features included
- to compensate the update event status( compleated or not ) i have implemented drag the event to some other dates to change the event date 
- we can extend the start and end time as extending the event from calender
- remove / create event
- otp authentication using smpt for registered user in the cleverspace application
- email password authentication also
- implemented JWT token 

## some working principles
- used jwt in backend authorisation , we will be saving access token session and pass that token in header each and every api calls to backend 
for tasks they are passed using ajax and for otp and login purpose they are passed using python requests

## working state 
- Backend = 100% working
- frontend = 90% working
  
## fix working on 
- issue on updating task compleation ( boolean field ) couldnt added trying to fix
- otp autentication sometimes not working in frontend , works 100% fine on backend need to fix on frontend

please feel free to contact developer nikhilmp448@gmail.com for any suggession
