import uuid
from constants import mycursor
from services.signup_service import SignupService

class LoginService(object):
    def __init__(self,data:dict):
        self.user_data = data
    
    def user_exists(self,email:str,password:str):
        """Return userid if email and password match a user"""
        mycursor.execute('use world')
        print(email, password)
        query = f"select username from project where (email='{email}' and pas='{password}')"
        print(query)
        mycursor.execute(query)
        data = mycursor.fetchall()
        print(data)
        return len(data) > 0

    def login(self):
        user_id = self.user_exists(self.user_data.get('email'),self.user_data.get('password'))
        # print(name)
        if not user_id:
            return "UserNotFound"
        auth = SignupService.generate_expiry_token(user_id)
        return auth