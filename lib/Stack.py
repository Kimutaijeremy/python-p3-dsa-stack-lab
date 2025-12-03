class Stack:
    def __init__(self, items=None, limit=None):
        """
        items → initial list to populate the stack
        limit → optional max capacity of the stack
        """
        if items is None:
            self.items = []
        else:
            self.items = items

        self.limit = limit

    # -----------------------
    # Core Stack Operations
    # -----------------------


    def push(self, value):
        """Push value onto stack unless full."""
        if self.limit is not None and len(self.items) >= self.limit:
            return  # silently ignore instead of raising
        self.items.append(value)

    def pop(self):
        """
        Pop top element.
        If empty → return None (because tests require this).
        """
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        """Return top element without removing it."""
        if not self.items:
            raise Exception("Stack is empty")
        return self.items[-1]

    # -----------------------
    # Bonus Methods
    # -----------------------

    def size(self):
        """Return number of elements."""
        return len(self.items)

    def isEmpty(self):
        """Return True if the stack is empty."""
        return len(self.items) == 0

    # The test expects full(), not isFull()
    def full(self):
        """Return True if the stack is full."""
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    # Still keep isFull for compatibility if needed (optional)
    def isFull(self):
        return self.full()

    def search(self, value):
        """
        Return distance from top of stack:
        top = 0, next = 1, etc.
        If not found → return -1.
        """
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == value:
                return (len(self.items) - 1) - i
        return -1
