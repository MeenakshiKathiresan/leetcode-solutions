class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = {}
        
        for ticket in tickets:
            if ticket[0]  not in flights:
                flights[ticket[0]] = []
            flights[ticket[0]].append(ticket[1])
        
        for key, to in flights.items():
            to.sort(reverse=True)
        itinerary = []
        
        def dfs(start):
            
            if len(itinerary) == len(tickets) + 1:
                return True
            
            if start not in flights:
                return False
            
            temp = list(flights[start])
            
            for i in range(len(temp)):
                
                next_neigh = flights[start].pop()
                itinerary.append(next_neigh)
                if dfs(next_neigh): return True
                
                flights[start].insert(0,next_neigh)
                itinerary.pop()
                
        itinerary.append("JFK")
        dfs("JFK")
        return itinerary
            