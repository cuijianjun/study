from common.utils import checkfile

class Base(object):
    def __init__(self,user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

        self.__check_user_json()

    def __check_user_json(self):
       checkfile(self.user_json)