class Base(object):
    def __init__(self,user_json,gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

    def __check_suer_json(self):
        if not