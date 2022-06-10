
class Airline_Ticket:

    def __init__(self,name, depart, dest, ticket_type, price):
        self.name = name
        self.depart_airport = depart
        self.destination_airport = dest
        self.ticket_class = ticket_type
        self.price = price

    def change_class(self,new_class, new_price):
        self.ticket_class = new_class
        self.price = new_price

    def __str__(self):
        out = "Name: " + self.name + "\n"
        out += "Departing Airport: " + self.depart_airport + "\n"
        out += "Destination Airport: " + self.destination_airport + "\n"
        out += "Ticket Class: " + self.ticket_class + "\n"
        out += "Price: " + str(self.price)
        return out

     


def tester():
    ticket1 = Airline_Ticket("Tom Thumb", "DSM", "ORD", "economy", 250 )
    print(ticket1)
    # ticket2 = ticket1.copy()
    # ticket1.change_class("first", 1000)
    # print(ticket1)
    # print(ticket2)

if __name__ == "__main__":
    tester()