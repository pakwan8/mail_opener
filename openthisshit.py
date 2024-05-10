from simplegmail import Gmail
from time import sleep

if __name__ == '__main__':
    gmail = Gmail()
    print("getting messages...")
    messages = gmail.get_unread_inbox()
    total = len(messages)
    print(f"total of \033[93m{total}\033[0m unread messages")
    if input("continue? [y/n]: ").lower() == "y":
        print("\033[33mmarking messages...\033[0m")
        for i, message in enumerate(messages):
            print(f"marking \033[42m{message}\033[0m as read \033[90m({i + 1}/{total})\033[0m")
            message.mark_as_read()

    print("\033[96mdone!\033[0m")
