import uuid
import constants
from constants import mycursor

class SignupService():
    def __init__(self,data:dict):
        print("In constructor")
        self.user_data = data
    
    @staticmethod
    def user_exists(e:str):
        """Return list of values if email id already exists else return []"""
        
        mycursor.execute("use world")
        mycursor.execute("select * from project where email = '{}'".format(e))
        data = mycursor.fetchall()
        return len(data) > 0

    def __create_account(self):
        """Create an entry for that user and return userid"""
        
        user_id = uuid.uuid4()
        mycursor.execute("use world")

        b = self.user_data.get('name')
        c = self.user_data.get('email')
        d = self.user_data.get('password')
        
        query = f"insert into project values ('{user_id}', '{b}', '{c}', '{d}')"
        
        mycursor.execute(query)
        
        constants.mydb.commit()
        
        mycursor.execute("select * from project")
        
        print(mycursor.fetchall())

        return user_id

    @staticmethod
    def generate_expiry_token(user_id:str):
        token = uuid.uuid4()
        """EXPIRY_TOKEN_DB : userid, token, createdAt"""
        mycursor.execute("use world")

        query = f"insert into auth_key values ('{token}', '{user_id}')"
        mycursor.execute(query)
        constants.mydb.commit()
        return token

    def signup(self):
        
        exists = SignupService.user_exists(self.user_data.get('email'))
        if exists:
            return "Already Exists"
        try:
            user_id = self.__create_account()
        except Exception as ex:
            print(ex)

        auth_token = SignupService.generate_expiry_token(user_id)
        return auth_token