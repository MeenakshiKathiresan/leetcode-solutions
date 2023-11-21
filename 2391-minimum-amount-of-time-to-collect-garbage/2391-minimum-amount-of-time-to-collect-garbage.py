class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m_counter, g_counter, p_counter = 0,0,0
        m_travel, g_travel, p_travel = 0,0,0
        
        for i, gar in enumerate(garbage):
            curr_travel = travel[i-1] if i > 0 else 0
            m_travel += curr_travel
            g_travel += curr_travel
            p_travel += curr_travel
            
            if gar.count("M") > 0:
                m_counter += m_travel + gar.count("M")
                m_travel = 0
            if gar.count("G") > 0:
                g_counter += g_travel + gar.count("G")
                g_travel = 0
            if gar.count("P") > 0:
                p_counter += p_travel + gar.count("P")
                p_travel = 0
        
        print(m_counter, g_counter, p_counter)
        return m_counter + g_counter + p_counter
                    
                  