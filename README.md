## RSS Annotation Tool Test Plan

### Introduction 

Below functions will be tested
* User Creation
* Login
* Logout
* Get feed

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
* TODO // Firefox v.65

### Test cases

#### User Creation Function

1. a user should be able to create an account with a valid username and valid password :white_check_mark: 
```
- Go to register page
- Fill related forms with valid data
- Click Submit button
- Expected: Successful User Creation 
```

2. a user should not be able to create an account with the same username and password :white_check_mark: 
```
- Go to register page
- Fill related forms with same username and password
- Click Submit button
- Expected: No User Creation - Warning 
```

3. a user should not be able to create an account with a similar same username and password :white_check_mark: 
```
- Go to register page
- Fill related forms with "user1" username and "user123" password
- Click Submit button
- Expected: No User Creation - Warning 
```

4. a user should not be able to create a username has a more than 30 character :white_check_mark: 
```
- Go to register page
- Fill related forms with "user1" username and "user123" password
- Click Submit button
- Expected: No User Creation - Warning 
``` 

5. a user should be able to create a username with the supported format(Letters, digits and @/./+/-/_ only) :white_check_mark: 
```
- Go to register page
- Fill related forms with "user_1" username and "p@ssW0rD" password
- Click Submit button
- Expected: Successful User Creation 
``` 

6. a user should not be able to create a password only numerically :white_check_mark: 
```
- Go to register page
- Fill related forms with "user1" username and "123456789" password
- Click Submit button
- Expected: No User Creation - Warning 
``` 

#### Login Function 

1. a user should be able to login with a valid username and valid password :white_check_mark: 
```
- Go to the login page
- Fill related forms with valid data
- Click Submit button
- Expected: Successful Login 
``` 

2. a user should not be able to login with a valid username and an invalid password :white_check_mark: 
```
- Go to the login page
- Fill related forms with a valid username and invalid password
- Click Submit button
- Expected: Unsuccessful Login - Warning 
``` 

3. a user should not be the able login with blank field/s :white_check_mark: 
```
- Go to the login page
- Leave blank form/s
- Click Submit button
- Expected: Unsuccessful Login - Warning 
``` 


#### Logout Function

1. a user should be able to log out :white_check_mark: 
```
- go to feeds page
- click logout
- Expected: Successful Logout 
``` 

2. a user should not be able to add RSS feed & see My Feeds after logout :white_check_mark: 
```
- go to feeds page
- click logout
- refresh page & back
- Expected: No Add & My Feeds button - Successful Logout 
``` 

#### Get Feed Function

1. a registered user should be able to add new feed sources :white_check_mark: 
```
- Login 
- Click New Feed 
- Add http://feeds.feedburner.com/TechCrunch/
- Expected: No User Creation - Warning 
``` 

2. a user should be able to get updates :white_check_mark: 
```
- go to feeds
- click TechCrunch 
- click check for updates
- Expected: Get updates 
``` 

3. a user should be able to add a comment in markdown format :white_check_mark: 
```
- go to favorite feed
- click first feed
- add a comment in markdown format
- Expected: User sees comments in the correct format 
```

4. a user should be able to see below data :white_check_mark: 
* Added by
* Feed URL
* Date added
* Last updated
* Last checked
* Title
* Date
* Author
* Comments
```
- go to favorite feed
- click first feed
- check above data
- Expected: Fields and values should be visible and correct 
``` 

#### Concerns 
* Login and Registration features may give specific messages.
* id attributes can be helpful for QAs for selecting items

#### Bugs
1. Username and comment section overlapping
step to reproduce
* go to feed page
* add comment 
Expected: Username and comment section should be aligned
Actual: Overlapping

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
* run ```pip install -r requirements.txt```
* run ```behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features```
* run ```allure generate allure/results/ -o allure/reports --clean```
Generated report will be located as a ```allure/reports/index.html```


Notice: Chrome driver in project compatible with MacOS
