import configparser
import os
from os.path import dirname

MAIN_DIRECTORY = dirname(dirname(__file__))
config = configparser.RawConfigParser()
config.read(MAIN_DIRECTORY+"/Configuration/config.ini")
# print(MAIN_DIRECTORY)
# config.read(".//Configuration//config.ini")







class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url


    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password