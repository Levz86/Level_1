#class Email
class Email:
   #constructor to initialise variables
    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents 
        self.has_been_read = False
        self.is_spam = False
    #method to mark email as read
    def mark_as_read(self):
        self.has_been_read = True
    #method to mark email as spam
    def mark_as_spam(self):
        self.is_spam = True

#method to add email to inbox

class Inbox:
    def __init__(self):
        self.emails = []
    # method to add email
    def add_email(self, from_address, subject_line, email_contents):
        new_email = Email(from_address, subject_line, email_contents)
        self.emails.append(new_email)
    #method to list messages from sender
    def list_messages_from_sender (self, sender_address):
        sender_emails = [(i, e.subject_line) for i, e in enumerate(self.emails)if e.from_address == sender_address]
        if not sender_emails:
            return "No emails found from this sender."
        else:
            return "\n" .join([f"{i} {subject}" for i, subject in sender_emails])
     # method to get email   
    def get_email (self, sender_address, index):
        for email in self.emails:
            if email.from_address == sender_address and email.subject_line == self.list_messages_from_sender(sender_address).split()[index+1]:
                email.mark_as_read()
                return email 
            
#method to mark as spam
    def mark_as_spam (self, sender_address, index):
        for email in self.emails:
             if email.from_address == sender_address and email.subject_line == self.list_messages_from_sender(sender_address):
                email.mark_as_spam()
                return
             
    # method to get list of unread emails
    def get_unread_email (self):
        unread_emails = [email.subject_line for email in self.emails if not email.has_been_read]
        if not unread_emails:
            return "No unread emails."
        else:
            return '\n'.join(unread_emails)
        
        # method to get list of spam emails
    def get_spam_emails (self):
        spam_emails = [email.subject_line for email in self.emails if email.is_spam]
        if not spam_emails:
            return "No spam emails"
        else:
            return "\n" .join(spam_emails)
        
        # method to delete email at a given index
    def delete (self, sender_address, index):
        for i, email in enumerate (self.emails):
            if email.for_address == sender_address and email.subject_line == self.list_messages_from_sender(sender_address).split()[index]:
                del self.emails[i]
                return



usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''



#An Email Simulation

 



user_choice = ""
inbox = Inbox()
while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email (Create a new Email object)
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        contents = input("Please enter the contents of the email\n:")

        # Now add the email to the Inbox

        # Print a success message
        print("Email has been added to inbox.")

        pass
    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")

        # Now list all emails from this sender
        print(inbox.list_messages_from_sender(sender_address))

        pass
    elif user_choice == "r":
        # Read an email

        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Step 2: show all emails from this sender (with indexes)
        print(inbox.list_messages_from_sender(sender_address))
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email that you would like to read\n:"))

        # Step 4: display the email
        print(inbox.get_email(sender_address,email_index))
        pass
    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)

        print(inbox.list_messages_from_sender(sender_address))

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be marked as spam\n:"))

        # Step 4: mark the email as spam
        print(inbox.mark_as_spam(sender_address,email_index))

        # Step 5: print a success message
        print("Email has been marked as spam")

        pass
    elif user_choice == "gu":
        # List all unread emails
        print(inbox.get_unread_email())
        pass
    elif user_choice == "gs":
        # List all spam emails
        print(inbox.get_spam_emails())
        pass
    elif user_choice == "e":
        print("Goodbye")
        break
    elif user_choice == "d":
        # Delete an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        print(inbox.delete(sender_address))

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be deleted\n:"))

        # Step 4: delete the email
        print(inbox.delete(sender_address,email_index))

        # Step 5: print a success message
        print("Email has been deleted")

        pass
    else:
        print("Oops - incorrect input")
