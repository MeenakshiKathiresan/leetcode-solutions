class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # process the string and get all sub domains
        # store sub domains in a dictionary and add counts
        # construct result

        sub_domains_dict = defaultdict(int)
        res = []

        for cpdomain in cpdomains: 
            count, domain = cpdomain.split(" ") 
            
            count_int = int(count)
            curr = ""
            for i in range(len(domain) - 1, -1, -1):
                if domain[i] == ".":
                    sub_domains_dict[curr] += count_int
                curr = domain[i] + curr
            sub_domains_dict[curr] += count_int
        
        for k, v in sub_domains_dict.items():
            res.append(f"{v} {k}")
    
        return res