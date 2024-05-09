from simplegmail import Gmail

if __name__ == '__main__':
    gmail = Gmail()
    print("getting messages...")
    messages = gmail.get_unread_inbox()
    print(f"total of \033[93m{len(messages)}\033[0m unread messages")
    if input("continue? [y/n]: ").lower() == "y":
        for message in messages:
            print(f"marking \033[42m{message}\033[0m as read")
            message.mark_as_read()

    print("\033[92mdone\033[0m")
