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

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()

        temp = result

        latest = len(temp) - 1

        temp = temp[latest - 3] + temp[latest - 2], temp[latest - 10] + temp[latest - 9], \
                    temp[latest - 17] + temp[latest - 16], \
                    temp[latest - 24] + temp[latest - 23], temp[latest - 31] + temp[latest - 30], \
                    temp[latest - 38] + temp[latest - 37], \
                    temp[latest - 45] + temp[latest - 44], temp[latest - 52] + temp[latest - 51], \
                    temp[latest - 59] + temp[latest - 58], \
                    temp[latest - 66] + temp[latest - 65], temp[latest - 73] + temp[latest - 72]

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

        timestamp = timestamp[latest - 3] + timestamp[latest - 2], timestamp[latest - 10] + timestamp[latest - 9], \
                    timestamp[latest - 17] + timestamp[latest - 16], \
                    timestamp[latest - 24] + timestamp[latest - 23], timestamp[latest - 31] + timestamp[latest - 30], \
                    timestamp[latest - 38] + timestamp[latest - 37], \
                    timestamp[latest - 45] + timestamp[latest - 44], timestamp[latest - 52] + timestamp[latest - 51], \
                    timestamp[latest - 59] + timestamp[latest - 58], \
                    timestamp[latest - 66] + timestamp[latest - 65], timestamp[latest - 73] + timestamp[latest - 72], \
                    timestamp[latest - 80] + timestamp[latest - 79]

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

        hum = hum[latest - 3] + hum[latest - 2], hum[latest - 10] + hum[latest - 9], \
              hum[latest - 17] + hum[latest - 16], \
              hum[latest - 24] + hum[latest - 23], hum[latest - 31] + hum[latest - 30], \
              hum[latest - 38] + hum[latest - 37], \
              hum[latest - 45] + hum[latest - 44], hum[latest - 52] + hum[latest - 51], \
              hum[latest - 59] + hum[latest - 58], \
              hum[latest - 66] + hum[latest - 65], hum[latest - 73] + hum[latest - 72]

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
        timestamp = timestamp[latest-3] + timestamp[latest-2], timestamp[latest-10] + timestamp[latest-9], timestamp[latest-17] + timestamp[latest-16], \
                    timestamp[latest-24] + timestamp[latest-23], timestamp[latest-31] + timestamp[latest-30], timestamp[latest-38] + timestamp[latest-37], \
                    timestamp[latest-45] + timestamp[latest-44], timestamp[latest-52] + timestamp[latest-51], timestamp[latest-59] + timestamp[latest-58], \
                    timestamp[latest - 66] + timestamp[latest - 65], timestamp[latest - 73] + timestamp[latest-72], timestamp[latest-80] + timestamp[latest-79]

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