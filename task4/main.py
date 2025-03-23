from typing import Dict, Callable


def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Incorrect input."
        except KeyError:
            return "Contact not found."

    return inner


def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts: Dict[str, str]) -> str:
    name, phone = args
    if name in contacts:
        return "Contact is already exists!"
    contacts[name] = phone
    return "Contact added"


@input_error
def change_contact(args: list, contacts: Dict[str, str]) -> str:
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Contact phone changed to {phone}"


def all_contacts(contacts: Dict[str, str]) -> str:
    if len(contacts):
        return_str = ""
        for name, phone in contacts.items():
            return_str += f"{name}: {phone}, "
        return return_str[:-2]  # remove redundant coma and space for return
    return "Contacts not found"


@input_error
def phone_contact(args: list, contacts: Dict[str, str]) -> str:
    name = args[0]
    return contacts[name]


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
