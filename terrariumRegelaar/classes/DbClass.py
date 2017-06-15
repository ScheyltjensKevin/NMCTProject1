class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "kevin",
            "passwd": "036059940",
            "db": "terrariumDB"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getDataFromDatabase(self):
        # Query zonder parameters

        sqlQuery = "SELECT * FROM tablename"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def setTempDataToDatabase(self, valueTemp, timestamp, fans):
        if self.__cursor != self.__connection.cursor():
            self.__cursor = self.__connection.cursor()
        else:
            pass
        # Query met parameters
        sqlQuery = "INSERT INTO temperature (value,timestamp,fans) VALUES ('{param1}','{param2}','{param3}')"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=valueTemp,param2=timestamp,param3=fans)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def setHumDataToDatabase(self,valueHum, timestamp):
        if self.__cursor != self.__connection.cursor():
            self.__cursor = self.__connection.cursor()
        else:
            pass
        # Query met parameters
        sqlQuery = "INSERT INTO humidity (value,timestamp) VALUES ('{param1}','{param2}')"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=valueHum, param2=timestamp)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()