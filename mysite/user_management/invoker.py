class UserCommandInvoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        results = []
        for command in self.commands:
            results.append(command.execute())
        return results
