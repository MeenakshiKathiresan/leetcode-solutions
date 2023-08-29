class Solution:
    def bestClosingTime(self, customers: str) -> int:
        no_left_counter = 0
        yes_right_counter = customers.count("Y")
        
        
        
        # encounter a yes - reduce yes counter
        # encounter a no - increase no counter
        # at one point, find penalty by calculating nocounter and yes_counter
        # return the least penalty
        
        least_penalty = yes_right_counter + no_left_counter
        least_index = 0
        
        for i, customer in enumerate(customers):
            if customer == "Y":
                yes_right_counter -= 1
            else:
                no_left_counter += 1
            
            
            penalty = yes_right_counter + no_left_counter
            
            if penalty < least_penalty:
                least_penalty = penalty
                least_index = i+1
                
        
        return least_index
        