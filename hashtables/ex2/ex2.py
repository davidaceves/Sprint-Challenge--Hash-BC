#  Hin  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

ticketArray = [
  Ticket("PIT", "ORD" ),
  Ticket("XNA", "CID" ),
  Ticket("SFO", "BHM" ),
  Ticket( "FLG", "XNA" ),
  Ticket( "NONE", "LAX" ),
  Ticket( "LAX", "SFO" ),
  Ticket( "CID", "SLC" ),
  Ticket( "ORD", "NONE" ),
  Ticket( "SLC", "PIT" ),
  Ticket( "BHM", "FLG" )
]

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)

    for ticket in ticketArray: 
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    route = [None] * length
    arrayLen = 0

    if hash_table_retrieve(hashtable, "NONE"):
        route[arrayLen] = hash_table_retrieve(hashtable, "NONE")

    while arrayLen < length - 1 and route[arrayLen] is not None:
        destination = hash_table_retrieve(hashtable, route[arrayLen])
        
        arrayLen += 1
        route[arrayLen] = destination
        

    return route

print(reconstruct_trip(ticketArray, 10))