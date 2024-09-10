class Ticket:
    def __init__(self, id, description, priority):
        self.id = id
        self.description = description
        self.priority = priority
class TicketQueue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        i = 0
        while i > len(self.items) and self.items[i].priority < item.priority:
            i += 1
        self.items.insert(i, item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
ticket1 = Ticket(321654987, "Problemas menores", 3)
ticket2 = Ticket(987654321, "Problemas mayores", 2)
ticket3 = Ticket(123456789, "Accion inmediata", 1)
ticket_queue = TicketQueue()
ticket_queue.enqueue(ticket1)
ticket_queue.enqueue(ticket2)
ticket_queue.enqueue(ticket3)
while not ticket_queue.is_empty():
    ticket = ticket_queue.dequeue()
    print(f"Ticket No: {ticket.id}, {ticket.description} (prioridad: {ticket.priority})")