## RSS Annotation Tool Test Plan

### Introduction 

Below functions will be tested
* User Creation
* Login
* Logout
* Get feed

### Test cases

#### User Creation Function

1. a user should be able to create an account with a valid username and valid password 
- Go to register page
- Fill related forms with valid data
- Click Submit button
Expected: Successful User Creation
Result: Successful User Creation

2. a user should not be able to create an account with the same username and password 
- Go to register page
- Fill related forms with same username and password
- Click Submit button
Expected: No User Creation - Warning
Result: No User Creation - Warning

3. a user should not be able to create an account with a similar same username and password 
- Go to register page
- Fill related forms with "user1" username and "user123" password
- Click Submit button
Expected: No User Creation - Warning
Result: No User Creation - Warning

4. a user should not be able to create a username has a more than 30 character
- Go to register page
- Fill related forms with "user1" username and "user123" password
- Click Submit button
Expected: No User Creation - Warning
Result: No User Creation - Warning

5. a user should be able to create a username with the supported format(Letters, digits and @/./+/-/_ only)
- Go to register page
- Fill related forms with "user_1" username and "p@ssW0rD" password
- Click Submit button
Expected: Successful User Creation
Result: Successful User Creation

6. a user should not be able to create a password only numerically
- Go to register page
- Fill related forms with "user1" username and "123456789" password
- Click Submit button
Expected: No User Creation - Warning
Result: No User Creation - Warning

#### Login Function 

1. a user should be able to login with a valid username and valid password 
- Go to login page
- Fill related forms with valid data
- Click Submit button
Expected: Successful Login
Result: Successful Login

2. a user should not be able to login with a valid username and an invalid password
- Go to login page
- Fill related forms with valid username and invalid password
- Click Submit button
Expected: Unsuccessful Login - Warning
Result: Unsuccessful Login - Warning

3. a user should not be the able login with blank field/s
- Go to login page
- Leave blank form/s
- Click Submit button
Expected: Unsuccessful Login - Warning
Result: Unsuccessful Login - Warning


#### Logout Function

1. a user should be able to log out
- go to feeds page
- click logout
Expected: Successful Logout
Result: Successful Logout

2. a user should not be able to add RSS feed & see My Feeds after logout
- go to feeds page
- click logout
- refresh page & back
Expected: No Add & My Feeds button - Successful Logout
Result: No Add & My Feeds button - Successful Logout

##### Get Feed Function

1. a registered user should be able to add new feed sources
- Login 
- Click New Feed 
- Add http://feeds.feedburner.com/TechCrunch/
Expected: No User Creation - Warning
Result: No User Creation - Warning

2. a user should be able to get updates
- go to feeds
- click TechCrunch 
- click check for updates
Expected: Get updates
Result: Get updates

3. a user should be able to add comment in markdown format
- go to favorite feed
- click first feed
- add comment in markdown format
Expected: user sees comments in correct format
Results: user sees comments in correct format

4. a user should be able to see below data 
* Added by
* Feed URL
* Date added
* Last updated
* Last checked

* Title
* Date
* Author
* Comments

- go to favorite feed
- click first feed
- check above data
Expected: Fields and values should be visible and correct
Result: Fields and values should be visible and correct

### In scope
* Computer users
* Only EN language users

### Out Of Scope
* Mobile users
* Mobile Browsers

### Risks
The app will be public, so below concerns should be reviewed 
* Load test
* Performance test
* Security test

### Environment
* Google Chrome v.72 
//TODO 
* Firefox v.65

### Techs
* Python 
* Selenium 
* Behave

### Automation

#### Requirements
* Chrome v.72 

#### Usage
* open terminal 
* go to automation project
* pip ```pip install -r requirements.txt```
* run ```behave```

Notice: Chrome driver in project compatible with MacOS