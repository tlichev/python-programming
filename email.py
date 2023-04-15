class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails_list = []
command = input()
while command != "Stop":
    sender = command.split()[0]
    receiver = command.split()[1]
    content = command.split()[2]
    email = Email(sender, receiver, content)
    emails_list.append(email)
    command = input()

indexes_list = input().split(", ")
indexes = [int(s) for s in indexes_list]

for i in indexes:
    emails_list[i].send()

for email in emails_list:
    print(email.get_info())
