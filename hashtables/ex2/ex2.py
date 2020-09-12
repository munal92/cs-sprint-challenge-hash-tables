#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    store = {}
    merged_arr = ["NONE"]

    for i in tickets:
        if i not in store:
            store[i.source] = i.destination

    return merge_tickets(store, merged_arr, 0)


def merge_tickets(store, merged_arr, currentValue):

    if store[merged_arr[currentValue]] == "NONE":

        merged_arr.append(store[merged_arr[currentValue]])
        merged_arr.pop(0)
    else:
        if store[merged_arr[currentValue]] != "NONE":
            merged_arr.append(store[merged_arr[currentValue]])

        merge_tickets(store, merged_arr, currentValue+1)
        return merged_arr


ticket_1 = Ticket("PDX", "DCA")
ticket_2 = Ticket("NONE", "PDX")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]
result = reconstruct_trip(tickets, 3)
print(result)
