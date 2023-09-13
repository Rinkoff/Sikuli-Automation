receiver = input("Who do you want to receive this message:")

subject = input("Enter an email subject:")

message = input("Enter your message here:")



type(Key.WIN)
type("Chrome")
type(Key.ENTER)
sleep(1)
type("https://mail.google.com/mail/u/0/#inbox")
type(Key.ENTER)


if exists("1694604151323.png"):
    click(Pattern("1694604167881.png").targetOffset(-226,82))
    password = input("Enter your password:")

    click(Pattern("1694604320106.png").targetOffset(16,-63))

    type(password)


click("1694604397846.png")

print receiver

type(receiver)
type(Key.TAB)
type(subject)
type(Key.TAB)
type(message)

click("1694604496101.png")


    

        