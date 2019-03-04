## RSS Annotation Tool Test Plan

### Introduction 

Below functions will be tested
* User Creation
* Login
* Logout
* Get feed
* Add feed source to bookmarks
* Remove feed source from bookmarks

### Test cases

#### User Creation Function

1. a user should be able to create an account with a valid username and valid password 
2. a user should not be able to create an account with the same username and password 
3. a user should not be able to create an account with similar same username and password 
4. a user should not be able to create a username has a more than 30 character
5. a user should be able to create a username with the supported format(Letters, digits and @/./+/-/_ only)


#### Login Function 

1. a user should be able to login with a valid username and valid password 
2. a user should not be able to login with a valid username and an invalid password
3. a user should not be the able login page for both, when the field is blank and Submit button is clicked
4. a user should be able to see invalid login message


#### Logout Function

1. a user should be able to log out
2. a user should not be able add RSS feed after logout


##### Get Feed Function

1. a registered user should be able to add new feed sources
2. a user should be able to get get updates
3. a user should be able to see below data 
* Added by
* Feed URL
* Date added
* Last updated
* Last checked

* Title
* Date
* Author
* Comments

### In scope
* Computer users
* Only EN language users

### Out Of Scope
* Mobile users
* Mobile Browsers

### Risks
App will be public, so below concerns should be reviewed 
* Load test
* Performans test
* Security test

### Environment
* Google Chrome v.72 
* Firefox v.65

### Techs
* Python 
* Selenium 
* Behave
