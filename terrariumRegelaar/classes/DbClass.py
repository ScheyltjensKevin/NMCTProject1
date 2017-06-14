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

    # def getDataFromDatabase(self):
    #     # Query zonder parameters
    #
    #     sqlQuery = "SELECT * FROM tablename"
    #
    #     self.__cursor.execute(sqlQuery)
    #     result = self.__cursor.fetchall()
    #     self.__cursor.close()
    #     return result

    # def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
    #     # Query met parameters
    #     sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
    #     # Combineren van de query en parameter
    #     sqlCommand = sqlQuery.format(param1=voorwaarde)
    #
    #     self.__cursor.execute(sqlCommand)
    #     result = self.__cursor.fetchall()
    #     self.__cursor.close()
    #     return result

    def setSensorDataToDatabase(self, sensortype,waarde,timestamp):
        # Query met parameters
        sqlQuery = "INSERT INTO sensordata (sensortype, waarde, timestamp) VALUES ('{param1}', '{param2}','{param3}')"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=sensortype)
        sqlCommand = sqlQuery.format(param2=waarde)
        sqlCommand = sqlQuery.format(param3=timestamp)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def setlampDataToDatabase(self, lamptype,timestamp):
        # Query met parameters
        sqlQuery = "INSERT INTO lamp (lamptype,timestamp) VALUES ('{param1}', '{param2}')"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=lamptype)
        sqlCommand = sqlQuery.format(param2=timestamp)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def setfansDataToDatabase(self, startTime, stopTime,duration):
        # Query met parameters
        sqlQuery = "INSERT INTO ventilatoren (startTime, stopTime, duration) VALUES ('{param1}', '{param2}','{param3}')"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=startTime)
        sqlCommand = sqlQuery.format(param2=stopTime)
        sqlCommand = sqlQuery.format(param3=duration)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()
