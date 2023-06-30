# Letter to reviewer
```
Hi!
I have been working on this project for a few days now. 
However, I must admit that the database is still fake, which is my biggest regret. 
Nevertheless, I do not believe that waiting would be beneficial for the process.
I have added tests to the project. If this were a real project, 
I would focus on increasing their coverage and refactoring the test structure.
As a side note, this is my first project using fastAPI. 
I decided to follow the given template. 
Usually, I work with Django. 
The Schema/Model implementation in this form is new to me, 
and I feel that it would require improvements 
if I had connected it to a real database.
Thank you for your time and consideration.

Best regards,
Jakub Wysocki
```

# How to run
Make sure you have installed Docker and running docker deamon.
  - To run the application use `docker-compose up --build`
  - To run the tests use `docker-compose -f ./docker-compose-run-tests.yaml up --build`

Before creating a porfolio please add tickers wit APPL and CMG symbols.
To create the ticker go to http://localhost:8001/api/v1/docs#/tickers/create_ticker_api_v1_tickers__post 
or you can use those two commands 
```
curl -X 'POST' \
  'http://localhost:8001/api/v1/tickers/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "symbol": "APPL",
  "price": 0
}'

curl -X 'POST' \
  'http://localhost:8001/api/v1/tickers/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "symbol": "CMG",
  "price": 0
}'
```
Those two are mocked by stock exchange mocker and will be updated.

To create portfolio with 10000 cash use this command.
```
curl -X 'POST' \
  'http://localhost:8001/api/v1/portfolios/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "cash": 10000,
  "positions": [
  ],
  "orders": [
  ]
}'
```

# Requirements

- [ ] The user is able to define his initial investment
  - the cash
  - the stocks

- [x] The system is periodically receives prices (tickers) from stock exchange
  - all the prices (tickers) should be recorded in the system in the system
  - the price changes may impact the portfolio
    
- [x] When the price of the stock in users portfolio changes significantly the portfolio is rebalanced
  - if stock that is in portfolio gained more than 10% in value the system sells 50% of the gain
    - the gained cash should be added to cash in portfolio
    - the position should be reduced
    
- [x] The app should be able to run in docker container
  - provide a dockerfile
  
 - [x] Please provide instruction how to run the app in docker container and how to test it at the top of the README.md file 

# Hints
- Please do not focus on the user management. We take it for granted and you do not have to implement it
- Please write reasonable amount of tests ( integration tests are fine, you do not have to unittest everything, unless it makes sense)
- What we would like to understand from this task
  - Your ability to understand the domain and to design domain models
  - The way you design the solution
  - The way you design API
  - The way you write tests

# Assumptions
- The system does not allow partial stocks, so the number of stocks in portfolio is always integer
- The system should attempt to sell only full stocks
- The selling process should be mocked, but please keep in mind that in real world it would require an integration with external system


# Blueprint
- The repository contains code that can be used as a starting point of the solution
  - You can use it but if you prefer to start from scratch, feel free to do so
  - This structure is a simplified version of the structure we use in our projects

## If you use the existing code as blueprint
- Feel free to modify the existing domain models, or change the existing ones it you will decide that they are not suitable for the solution
- There are some existing tests in the project, please check them 
- The database.py is just a mock of a database. A fake implementation basing on lists.
  - Feel free to use it as is, but you can as well connect to a real database