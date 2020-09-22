from heapq import heappush, heappop


class PQ: 'dimiourgw klasi PQ stin opoia arxikopoiw ta aparaitita stoixeia gia tis functions pou ousiastika einai panw-katw auta pou mas eixate stin proteinomeni selida'
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.count = 0

    def push(self, task, priority=0):
        '''Add a new task
        '''
        self.count += 1
        entry = [priority, self.count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def update(self, task, priority=0):
        '''Add a new task or update the priority of an existing task
        '''
        if task in self.entry_finder:
            self.remove_task(task)

        self.count += 1
        entry = [priority, self.count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        '''Mark an existing task as REMOVED.  Raise KeyError if not found.
        '''
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        '''Remove and return the lowest priority task. Raise KeyError if empty.
        '''
        while self.pq:
            priority, count, task = heappop(self.pq)

            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task

        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return len(self.pq) == 0

    def sort(self):
        return [heappop(self.pq) for i in range(len(self.pq))]








