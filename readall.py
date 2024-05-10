from simplegmail.message import Message
from simplegmail import Gmail
from time import perf_counter
from os import remove

if __name__ == '__main__':
    gmail: Gmail = Gmail()

    try:
        print("getting messages...")
        messages: list[Message] = gmail.get_unread_inbox()
        total: int = len(messages)

        print(f"total of \033[93m{total}\033[0m unread messages")
        if input("continue? [y/n]: ").lower() in ["y", "yes"]:
            i: int
            message: Message
            start: float = perf_counter()
            for i, message in enumerate(messages):
                print(f"marking \033[42m{message}\033[0m as read \033[90m({i + 1}/{total})\033[0m")
                message.mark_as_read()
            end: float = perf_counter()

            print(f"\033[96mfinished in \033[1m{end - start:.2f}s\033[0m\033[0m")
            remove("gmail_token.json")
        else:
            print("\033[96mabort\033[0m")

    except KeyboardInterrupt:
        remove("gmail_token.json")

