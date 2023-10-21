from collections import deque

class BreadthFirstSearch:
    Person1 = []
    Person2 = []

    def __init__(self):
        return

    def Person1(self):
        return self.Person1

    def Person2(self):
        return self.Person2

    # @return the length of the shortest paths (in rooms)
    def compute(self, file_data):
        file_array = []
        visited = set()
        newarr = []
        start_locs = []
        adj_dict = {}
        x = 0
        z = 0
        for i in file_data:
            if x < 3:
                newarr.append(i)
                x = x+1
        del file_data[0:3]
        for i in file_data:
            split = i.split()
            file_array.append([int(i) for i in split])
        for i in newarr:
            split = i.split()
            start_locs.append(split)
        for i in file_array:
            i.append(z)
            z += 1
        need_to_visit_q = deque()
        for i in range(int(newarr[0])):
            adj_dict[i] = file_array[i]
        need_to_visit_q.append(([int(start_locs[1][0])], [int(start_locs[2][0])]))
        while len(need_to_visit_q) != 0:
            cont_bool = False
            current = need_to_visit_q.popleft()
            Person1 = current[0]
            Person2 = current[1]
            visited.add((Person1[-1], Person2[-1]))
            if Person1[-1] == Person2[-1]:
                continue
            for i in adj_dict[Person1[-1]]:
                if i == Person2[-1]:
                    cont_bool = True
                    break
            for i in adj_dict[Person2[-1]]:
                if i == Person1[-1]:
                    cont_bool = True
                    break
            if cont_bool == True:
                continue
            if Person1[-1] == int(start_locs[1][1]) and Person2[-1] == int(start_locs[2][1]):
                self.Person1 = Person1
                self.Person2 = Person2
                return len(Person1)
            for x in adj_dict[Person1[-1]]:
                for j in adj_dict[Person2[-1]]:
                    Person1_copy = Person1.copy()
                    Person2_copy = Person2.copy()
                    Person1_copy.append(x)
                    Person2_copy.append(j)
                    if (Person1_copy[-1],Person2_copy[-1]) not in visited:
                        need_to_visit_q.append((Person1_copy, Person2_copy))