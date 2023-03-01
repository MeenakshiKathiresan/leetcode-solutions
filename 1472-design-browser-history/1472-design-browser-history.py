class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.fstack = []
        self.bstack = []
        self.curr = homepage
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        
        self.bstack.append(self.curr)
        self.fstack = []
        self.curr = url
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for step in range(steps):
            if len(self.bstack) > 0:
                self.fstack.append(self.curr)
                back = self.bstack.pop()
                self.curr = back
                
        return self.curr
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for step in range(steps):
            if len(self.fstack) > 0:
                self.bstack.append(self.curr)
                front = self.fstack.pop()
                self.curr = front
                
        return self.curr