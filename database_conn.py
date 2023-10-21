from chooseCategory import Category
from re import sub
import pymysql
import json

class DataBase:
    def __init__(self):
        #Load config.json
        
        jsonFile = open('config.json')
        config = json.load(jsonFile)

        #Get database info
        self.database = config['db']

        self.host = self.database['host']
        self.user = self.database['user']
        self.password = self.database['password']
        self.db = self.database['db_name']

        #Connect to database
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cursor = self.connection.cursor()
        print("Connected succedfully to database")

        # OpenAI
        self.category = Category()

    def check_user(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        self.cursor.execute(query, (username))
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False

    def create_user(self, username, currency):
        query = "CREATE TABLE `%s` (id INT AUTO_INCREMENT PRIMARY KEY, income DECIMAL, expense DECIMAL, date datetime DEFAULT CURRENT_TIMESTAMP, description VARCHAR(255), category VARCHAR(10))"
        self.cursor.execute(query, (username,))
        # Create a column in balance_users table
        sql = "INSERT INTO `balance_users` (`user`, `balance`, `total_income`, `total_expense`) VALUES (%s, '0', '0', '0')"
        self.cursor.execute(sql, (username,))
        # Create a column in currency table
        sql = "INSERT INTO `currency` (`id`, `currency`) VALUES (%s, %s)"
        self.cursor.execute(sql, (username, currency))  

    def add_column(self, username, income, expense, description):
        if expense != 0:
            category = self.category.chooseCategory(description)
            sql = "INSERT INTO `%s` (`income`, `expense`, `description`, `category`) VALUES ('0', '%s', '%s', '%s')"
        else:
            sql = "INSERT INTO `%s` (`income`, `expense`, `description`) VALUES ('%s', '0', '%s')"
        self.cursor.execute(sql, (username, income, expense, description, category))

    def get_balance(self, username):
        sql = "SELECT `balance` FROM `balance_users` WHERE `user` = %s"
        self.cursor.execute(sql, (username))
        result = self.cursor.fetchall()
        result = result[0][0]
        return result

    def update_balance(self, username, income, expense):
        sql = "SELECT `balance`, `total_income`, `total_expense` FROM `balance_users` WHERE `user` = %s"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchall()
        balance = float(result[0][0])
        total_income = float(result[0][1])
        total_expense = float(result[0][2])
        print("Updating balance")
        result = float(balance) + income - expense
        total_income += income
        total_expense += expense
        print("Balance: %s" % result, "Income: %s" % income, "Expense: %s" % expense)
        sql = "UPDATE `balance_users` SET `balance`=%s,`total_income`=%s,`total_expense`=%s WHERE user = %s"
        self.cursor.execute(sql, (result, total_income, total_expense, username))
        return result

    def get_mensual_balance(self, username):
        sql = "SELECT `income`, `expense`, date FROM `%s`"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchall()
        incomeAp = []
        date = []
        subT = 0
        lastDate = ""
        for long in result:
            dateSplit = str(long[2]).split(" ")

            if lastDate == "":
                lastDate = dateSplit[0]
                subT += float(long[0]) - float(long[1])
            elif lastDate == dateSplit[0]:
                subT += float(long[0]) - float(long[1])
            elif lastDate != dateSplit[0]:
                incomeAp.append(subT)
                date.append(lastDate)
                lastDate = dateSplit[0]
                subT += float(long[0]) - float(long[1])
        
        incomeAp.append(subT)
        date.append(lastDate)

        balance = [incomeAp, date]

        #Get the total income

        sql = "SELECT `income`, date FROM `%s` WHERE expense = '0'"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchall()

        incomeT = []
        dateIncome = []
        subT = 0
        lastDate = ""

        for long in result:
            dateSplit = str(long[1]).split(" ")

            if lastDate == "":
                lastDate = dateSplit[0]
                subT += float(long[0])
            elif lastDate == dateSplit[0]:
                subT += float(long[0])
            elif lastDate != dateSplit[0]:
                incomeT.append(subT)
                dateIncome.append(lastDate)
                subT = 0
                lastDate = dateSplit[0]
                subT += float(long[0])

        incomeT.append(subT)
        dateIncome.append(lastDate)

        income = [incomeT, dateIncome]
        
        #Get the total expense

        sql = "SELECT `expense`, date FROM `%s` WHERE income = '0'"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchall()

        expenseT = []
        dateExpense = []
        subT = 0
        lastDate = ""

        for long in result:
            dateSplit = str(long[1]).split(" ")

            if lastDate == "":
                lastDate = dateSplit[0]
                subT += float(long[0])
            elif lastDate == dateSplit[0]:
                subT += float(long[0])
            elif lastDate != dateSplit[0]:
                expenseT.append(subT)
                dateExpense.append(lastDate)
                subT = 0
                lastDate = dateSplit[0]
                subT += float(long[0])

        expenseT.append(subT)
        dateExpense.append(lastDate)

        expense = [expenseT, dateExpense]

        return balance, income, expense

    def deleteUser(self, username):
        sql = "DROP TABLE `%s`"
        self.cursor.execute(sql, (username,))
        sql = "DELETE FROM `balance_users` WHERE `user` = '%s'"
        self.cursor.execute(sql, (username,))
        sql = "DELETE FROM `currency` WHERE `id` = '%s'"
        self.cursor.execute(sql, (username,))
        print("User deleted")

    def checkCurrency(self, username):
        sql = "SELECT `currency` FROM `currency` WHERE `id` = '%s'"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchall()
        return result[0][0]

    def commit(self):
        self.connection.commit()
        return
    
    def close(self):
        self.connection.close()
        return

    def rollback(self):
        self.connection.rollback()
        return
    