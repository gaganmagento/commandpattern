from django.contrib.auth.models import User

class Command:
    def execute(self):
        raise NotImplementedError("You need to implement this method.")

class CreateUserCommand(Command):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def execute(self):
        if User.objects.filter(username=self.username).exists():
            return {"error": "User already exists."}
        
        user = User.objects.create_user(username=self.username, password=self.password)
        return {"id": user.id, "username": user.username}

class DeleteUserCommand(Command):
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self):
        try:
            user = User.objects.get(id=self.user_id)
            user.delete()
            return f"User {self.user_id} deleted."
        except User.DoesNotExist:
            return f"User {self.user_id} does not exist."
