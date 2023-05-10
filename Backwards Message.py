# Rewriting a message backwards

message = input("Type a message here: ")
new_message = ""

msg_len = len(message)

for i in range(1,msg_len+1):
    new_message = message[-i]
    print(new_message, end="")
