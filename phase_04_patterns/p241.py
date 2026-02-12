class OldAPI:
    def get_user(self, id):
        return {"user_id": id, "user_name": "John"}

class NewAPI:
    def __init__(self, old_api):
        self.old_api = old_api

    def fetch_user(self, id):
        old_data = self.old_api.get_user(id)
        new_data = {
            "id": old_data["user_id"],
            "name": old_data["user_name"]
        }
        return new_data

old_api = OldAPI()
new_api = NewAPI(old_api)

result = new_api.fetch_user(123)
print(result)