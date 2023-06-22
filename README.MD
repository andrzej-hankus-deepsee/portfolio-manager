# Requirements

- [ ] The user is able to define his initial investment
  - the cash
  - the stocks

- [ ] The system is periodically receives prices (tickers) from stock exchange
  - all the prices (tickers) should be recorded in the system in the system
  - the price changes may impact the portfolio
    
- [ ] When the price of the stock in users portfolio changes significantly the portfolio is rebalanced
  - if stock is in portfolio gained more than 10% in value the system sells 50% of the gain
    - the gained cash should be added to cash in portfolio
    - the position should be reduced
    
- [ ] The app should be able to run in docker container
  - provide a dockerfile
  
 - [ ] Please provide instruction how to run the app in docker container and how to test it at the top of the README.md file 

# Hints
- Please do not focus on the user management. We take it for granted and you do not have to implement it
- Please write reasonable amount of tests ( integration tests are fine, you do not have to unittest everything, unless it makes sense)
- What we would like to understand from this task
  - Your ability to understand the domain and to design domain models
  - The way you design the solution
  - The way you design API
  - The way you write tests


# Blueprint
- The repository contains code that can be used as a starting point of the solution
  - You can use it but if you prefer to start from scratch, feel free to do so
  - This structure is a simplified version of the structure we use in our projects

## If you use the existing code as blueprint
- Feel free to modify the existing domain models, or change the existing ones it you will decide that they are not suitable for the solution
- There are some existing tests in the project, please check them 
- The database.py is just a mock of a database. A fake implementation basing on lists.
  - Feel free to use it as is, but you can as well connect to a real database