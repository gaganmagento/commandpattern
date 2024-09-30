from django.core.management.base import BaseCommand
from user_management.commands import CreateUserCommand

class Command(BaseCommand):
    help = 'Create a new user interactively'

    def handle(self, *args, **options):
        username = self.get_input("Username: ")
        password = self.get_input("Password: ")

        command = CreateUserCommand(username, password)
        result = command.execute()

        if 'error' in result:
            self.stderr.write(self.style.ERROR(result['error']))
        else:
            self.stdout.write(self.style.SUCCESS(f"User {result['username']} created with ID {result['id']}"))

    def get_input(self, prompt):
        return input(prompt)
