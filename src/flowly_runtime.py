# flowly_runtime.py

class FlowlyRuntime:
    def __init__(self):
        self.memory = {}
        self.commands = {
            '/start': self.start,
            '/agent': self.invoke_agent,
            '/flow': self.show_flow
        }

    def start(self):
        return "✅ FlowCascade Runtime Activated"

    def invoke_agent(self, name):
        return f"🎯 Invoking agent: {name}"

    def show_flow(self):
        return "🔁 Displaying duality flow structure..."

    def run(self, command, arg=None):
        return self.commands.get(command, lambda: 'Unknown command')(arg) if arg else self.commands.get(command, lambda: 'Unknown command')()

if __name__ == '__main__':
    runtime = FlowlyRuntime()
    print(runtime.run('/start'))
