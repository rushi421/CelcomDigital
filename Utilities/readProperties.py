import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Hello\\PycharmProjects\\CelcomDigital\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getDealerURL():
        dealerurl = config.get('basic info', 'dealerURL')
        return dealerurl

    @staticmethod
    def getUserName():
        username = config.get('basic info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('basic info', 'password')
        return password

    @staticmethod
    def getMassURL():
        appurl = config.get('basic info', 'appURL')
        return appurl

    @staticmethod
    def getIDNumber():
        idnumber = config.get('basic info', 'IDNumber')
        return idnumber

    @staticmethod
    def getFullName():
        fullname = config.get('basic info', 'fullName')
        return fullname

    @staticmethod
    def getLine1():
        line1 = config.get('basic info', 'line1')
        return line1

    @staticmethod
    def getLine2():
        line2 = config.get('basic info', 'line2')
        return line2

    @staticmethod
    def getPostCode():
        postcode = config.get('basic info', 'postcode')
        return postcode

    @staticmethod
    def getCity():
        city = config.get('basic info', 'city')
        return city

    @staticmethod
    def getDLine1():
        dline1 = config.get('basic info', 'dline1')
        return dline1

    @staticmethod
    def getDLine2():
        dline2 = config.get('basic info', 'dline2')
        return dline2

    @staticmethod
    def getDPostCode():
        dpostcode = config.get('basic info', 'dPostcode')
        return dpostcode

    @staticmethod
    def getDCity():
        dcity = config.get('basic info', 'dCity')
        return dcity

    @staticmethod
    def getMobileNumber():
        mobilenumber = config.get('basic info', 'mobilenumber')
        return mobilenumber

    @staticmethod
    def getEmail():
        email = config.get('basic info', 'email')
        return email

    @staticmethod
    def getAgentURL():
        agenturl = config.get('basic info', 'agentURL')
        return agenturl

    @staticmethod
    def getAgentUsername():
        agentusername = config.get('basic info', 'agentUsername')
        return agentusername

    @staticmethod
    def getAgentPassword():
        agentpassword = config.get('basic info', 'agentPassword')
        return agentpassword
