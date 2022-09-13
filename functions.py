from database_conn import DataBase
from graphics import Graphics

class Functions:

    def __init__(self):
        self.db = DataBase()
        self.graph = Graphics()

    def createUser(self, username):
        
        try:
            self.db.check_user(username)
            return "User already exists"

        except Exception as e:
            
            try:
                self.db.create_user(username)
            
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
            self.db.add_column(username, income, 0, description)
            print("Income added")
            self.db.commit()
            balance = self.db.get_balance(username)
            self.db.update_balance(username, income, 0, balance)

        except Exception as e:
            self.db.rollback()
            return "Error adding income, please try again or later"

        finally:
            self.db.commit()
            return "Income added"

    def addExpense(self, username, expense, description):

        try:
            self.db.add_column(username, 0, expense, description)

        except Exception as e:
            self.db.rollback()
            return "Error adding expense, please try again or later"

        finally:
            self.db.commit()
            return "Expense added"

    def getBalance(self, username):

        try:
            balance = self.db.get_balance(username)

        except Exception as e:
            print("Error getting balance")
            self.db.rollback()
            return "Error getting balance"

        finally:
            self.db.commit()
            return balance
    
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
            self.db.deleteUser(username)
        except Exception as e:
            print("Error deleting user:", e)
            self.db.rollback()
        finally:
            self.db.commit()

    def getGraph(self, username):
        try:
            data = self.db.get_mensual_balance(username)
            image = self.graph.plot(data)

        except Exception as e:
            print("Error getting graph:", e)
            self.db.rollback()
        finally:
            self.db.commit()
            return image
        
        


