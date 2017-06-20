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

    def getTempDataFromDatabase(self):
        if self.__cursor != self.__connection.cursor():
            self.__cursor = self.__connection.cursor()
        else:
            pass

        # Query zonder parameters
        sqlQuery = "SELECT * FROM temperature"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getTempvalueDataFromDatabase(self):
        if self.__cursor != self.__connection.cursor():
            self.__cursor = self.__connection.cursor()
        else:
            pass

        # Query zonder parameters
        sqlQuery = "SELECT value FROM temperature"
        self.__connection.reset_session()
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()

        temp = result

        latest = len(temp) - 1

        temp = temp[latest - 21] + temp[latest - 20], temp[latest - 19] + temp[latest - 18], \
               temp[latest - 17] + temp[latest - 16], \
               temp[latest - 15] + temp[latest - 14], temp[latest - 13] + temp[latest - 12], \
               temp[latest - 11] + temp[latest - 10], \
               temp[latest - 9] + temp[latest - 8], temp[latest - 7] + temp[latest - 6], \
               temp[latest - 5] + temp[latest - 4], \
               temp[latest - 3] + temp[latest -2], temp[latest -1] + temp[latest]


        temp = str(temp).replace(",","")
        temp = str(temp).replace("(","")
        temp = str(temp).replace(")","")
        temp = str(temp).replace("[","")
        temp = str(temp).replace("]","")
        temp = str(temp).replace(" ","")
        temperature = ""
        templist = []
        a = 0
        for i in range(len(temp)):
            temperature += temp[i]
            if i == 3+a:
                templist.append(temperature)
                temperature =""
                a+=4
        return templist

    def getTempFansDataFromDatabase(self):
        if self.__cursor != self.__connection.cursor():
            self.__cursor = self.__connection.cursor()
        else:
            pass

        # Query zonder parameters
        sqlQuery = "SELECT fans FROM temperature"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getTempTimestampDataFromDatabase(self):
        if self.__cursor != self.__connection.cursor():
            self.__cursor = self.__connection.cursor()
        else:
            pass

        # Query zonder parameters
        sqlQuery = "SELECT timestamp FROM temperature"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        timestamp = result

        timestamp = str(timestamp).split(',')

        latest = len(timestamp) - 1

        timestamp = timestamp[latest - 73] + timestamp[latest - 72], timestamp[latest - 66] + timestamp[latest - 65], \
               timestamp[latest - 59] + timestamp[latest - 58], \
               timestamp[latest - 52] + timestamp[latest - 51], timestamp[latest - 45] + timestamp[latest - 44], \
               timestamp[latest - 38] + timestamp[latest - 37], \
               timestamp[latest - 31] + timestamp[latest - 30], timestamp[latest - 24] + timestamp[latest - 23], \
               timestamp[latest - 17] + timestamp[latest - 16], \
               timestamp[latest - 10] + timestamp[latest - 9], timestamp[latest - 3] + timestamp[latest - 2]



        timestamp = str(timestamp).replace("' ", "'")
        timestamp = str(timestamp).replace("(", "")
        timestamp = str(timestamp).replace(")", "")
        timestamp = str(timestamp).replace("'", "")
        timestamp = str(timestamp).replace(", ", ",")
        timestamp = str(timestamp).replace(" ", ":")
        timestamp = str(timestamp).split(',')

        return timestamp

    def getHumValueDataFromDatabase(self):
        if self.__cursor != self.__connection.cursor():
            self.__cursor = self.__connection.cursor()
        else:
            pass

        # Query zonder parameters
        sqlQuery = "SELECT value FROM humidity"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()

        hum = result

        latest = len(hum) - 1

        hum  = hum[latest - 21] + hum[latest - 20], hum[latest - 19] + hum[latest - 18], \
               hum[latest - 17] + hum[latest - 16], \
               hum[latest - 15] + hum[latest - 14], hum[latest - 13] + hum[latest - 12], \
               hum[latest - 11] + hum[latest - 10], \
               hum[latest - 9] + hum[latest - 8], hum[latest - 7] + hum[latest - 6], \
               hum[latest - 5] + hum[latest - 4], \
               hum[latest - 3] + hum[latest - 2], hum[latest - 1] + hum[latest]

        hum = str(hum).replace(",", "")
        hum = str(hum).replace("(", "")
        hum = str(hum).replace(")", "")
        hum = str(hum).replace("[", "")
        hum = str(hum).replace("]", "")
        hum = str(hum).replace(" ", "")
        humidity = ""
        humlist = []
        a = 0
        for i in range(len(hum)):
            humidity += hum[i]
            if i == 3 + a:
                humlist.append(humidity)
                humidity = ""
                a+=4

        return humlist


    def getHumTimestampDataFromDatabase(self):
        if self.__cursor != self.__connection.cursor():
            self.__cursor = self.__connection.cursor()
        else:
            pass

        # Query zonder parameters
        sqlQuery = "SELECT timestamp FROM humidity"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        timestamp = result
        timestamp = str(timestamp).split(',')

        latest = len(timestamp)-1

        timestamp = timestamp[latest - 73] + timestamp[latest - 72], timestamp[latest - 66] + timestamp[latest - 65], \
               timestamp[latest - 59] + timestamp[latest - 58], \
               timestamp[latest - 52] + timestamp[latest - 51], timestamp[latest - 45] + timestamp[latest - 44], \
               timestamp[latest - 38] + timestamp[latest - 37], \
               timestamp[latest - 31] + timestamp[latest - 30], timestamp[latest - 24] + timestamp[latest - 23], \
               timestamp[latest - 17] + timestamp[latest - 16], \
               timestamp[latest - 10] + timestamp[latest - 9], timestamp[latest - 3] + timestamp[latest - 2]

        timestamp = str(timestamp).replace("' ", "'")
        timestamp = str(timestamp).replace("(", "")
        timestamp = str(timestamp).replace(")", "")
        timestamp = str(timestamp).replace("'", "")
        timestamp = str(timestamp).replace(", ", ",")
        timestamp = str(timestamp).replace(" ", ":")
        timestamp = str(timestamp).split(',')

        return timestamp

    def getTempValueDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        if self.__cursor != self.__connection.cursor():
            self.__cursor = self.__connection.cursor()
        else:
            pass

        # Query met parameters
        sqlQuery = "SELECT * FROM temperature WHERE value = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result