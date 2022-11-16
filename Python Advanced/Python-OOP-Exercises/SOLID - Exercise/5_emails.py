from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyContent(IContent):
    def format(self):
        return f"<myML>{self.text}</myML>"


class EncryptedContent(IContent):
    def format(self):
        result = ""
        for letter in self.text:
            result += chr(ord(letter) + 5)
        return result


class MaskedContent(IContent):
    def format(self):
        return '*' * len(self.text)


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        ...

    @abstractmethod
    def set_receiver(self, receiver):
        ...

    @abstractmethod
    def set_content(self, content):
        ...


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender

    def set_receiver(self, receiver):
        self.__receiver = receiver

    def set_content(self, content):
        self.__content = content

    def __repr__(self):
        template = "Sender: I`m {sender}\nReceiver: I`m {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content.format())


email = Email('IM')

email.set_sender('qmal')

email.set_receiver('james')

content = MyContent('Hello, there!')

email.set_content(content)

print(email)