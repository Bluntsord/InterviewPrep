import bisect

INSERT = "insert"
GET = "get"
ADD_TO_KEY = "addToKey"
ADD_TO_VALUE = "addToValue"

def solution(queryType, query):
    my_map = HashMap()
    for i in range(len(queryType)):
        command_string = queryType[i]
        query_arr = query[i]
        my_map.handle_operation(command_string, query_arr)

    return my_map.get_acc()

class HashMap:
    def __init__(self):
        self.map = {}
        self.acc = 0
        self.key_carry_dict = {}
        self.key_carry_arr = []
        self.value_carry_arr = []
        self.value_carry_dict = {}
        self.command = 0

    def handle_operation(self, command_string, query_arr):
        self.command += 1
        if command_string == INSERT:
            self.insert(query_arr)
        elif command_string == GET:
            self.get(query_arr)
        elif command_string == ADD_TO_VALUE:
            self.addToValue(query_arr)
        elif command_string == ADD_TO_KEY:
            self.addToKey(query_arr)

    def insert(self, arr):
        pass

    def get(self, arr):
        pass

    def get_acc(self):
        return self.acc

    def addToKey(self, arr):
        self.carry += arr[0]

    def addToValue(self, arr):
        pass


commands1 = [INSERT, ADD_TO_VALUE, INSERT, ADD_TO_KEY, ADD_TO_VALUE, GET, GET]
inputs1 = [[1, 2], [1], [2, 3], [2], [2], [3], [4]]
answer = 10
print(solution(commands1, inputs1) == answer)

