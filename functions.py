from database_conn import DataBase
from graphics import Graphics

class Functions:

    def __init__(self):
        self.db = DataBase()
        self.graph = Graphics()

    def createUser(self, username, currency):
        
        try:
            self.db.check_user(username)
            return "User already exists"

        except Exception as e:
            
            try:
                self.db.create_user(username, currency)
            
            except Exception as e:
                self.db.rollback()
                return "Error creating user"
            
            finally:
                self.db.commit()
                return "User created"

        finally:
            self.db.commit()

    def addIncome(self, username, income, description):

        try:
            self.db.check_user(username)
            self.db.add_column(username, income, 0, description)
            self.updateBalance(username, float(income), 0)
            return "Income added"

        except Exception as e:
            self.db.rollback()
            err = str(e).split(',')[0]
            if err == "(1146":
                return "User doesn't exist"
            else:
                return "Error adding income, please try again or later"

        finally:
            self.db.commit()

    def addExpense(self, username, expense, description):

        try:
            self.db.check_user(username)
            self.db.add_column(username, 0, expense, description)
            self.updateBalance(username, 0, float(expense))
            return "Expense added"

        except Exception as e:
            self.db.rollback()
            err = str(e).split(',')[0]
            if err == "(1146":
                return "User doesn't exist"
            else:
                return "Error adding expense, please try again or later"

        finally:
            self.db.commit()

    def getBalance(self, username):

        try:
            self.db.check_user(username)
            balance = self.db.get_balance(username)
            return balance

        except Exception as e:
            self.db.rollback()
            print(e)
            err=str(e).split(',')[0]
            if err == "(1146":
                return "User doesn't exist"
            else:
                return "Error getting balance please try again or later"

        finally:
            self.db.commit()
    
    def updateBalance(self, username, income, expense):

        try:
            self.db.update_balance(username, income, expense)
        except Exception as e:
            print("Error updating balance:", e)
            self.db.rollback()
        finally:
            self.db.commit()

    def deleteUser(self, username):

        try:
            self.db.check_user(username)
            self.db.deleteUser(username)
            return "User deleted"
        except Exception as e:
            self.db.rollback()
            err = str(e).split(',')[0]
            if err == "(1146":
                return "User doesn't exist"
            else:
                return "Error deleting user, please try again or later"
        finally:
            self.db.commit()

    def getGraph(self, username, option):

        try:
            # Check if the user exists
            self.db.check_user(username)
            balance, income, expense = self.db.get_mensual_balance(username)
            currency = self.db.checkCurrency(username)
            self.graph.plot(balance, income, expense, option, currency)
            return 'Graph created'
        except Exception as e:
            self.db.rollback()
            err = str(e).split(',')[0]
            print(err)
            if err == "(1146":
                return "User doesn't exist"
            else:
                return 'Error'
            
        finally:
            self.db.commit()
        
        


