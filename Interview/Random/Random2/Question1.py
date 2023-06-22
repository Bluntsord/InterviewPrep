from typing import *


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans_dict = {}
        answer = set()
        transactions.sort(key=lambda x: int(x.split(',')[1]))

        for transaction in transactions:
            name, time_stamp, amount, city = transaction.split(",")
            time_stamp_int, amount_int = int(time_stamp), int(amount)
            if amount_int > 1000:
                answer.add(transaction)
                trans_dict[name] = trans_dict.get(name, [])
                trans_dict[name].append([time_stamp, amount, city])
            elif name in trans_dict:
                list_of_previous_details = trans_dict[name]
                for prev_time, prev_amount, prev_city in list_of_previous_details:
                    if time_stamp_int - int(prev_time) <= 60 and city != prev_city:
                        answer.add(','.join([name, prev_time, prev_amount, prev_city]))
                        answer.add(transaction)
                trans_dict[name] = trans_dict.get(name, [])
                trans_dict[name].append([time_stamp, amount, city])
            else:
                trans_dict[name] = trans_dict.get(name, [])
                trans_dict[name].append([time_stamp, amount, city])

        answer = list(answer)
        for transaction, count in dict(Counter(transactions)).items():
            for i in range(1, count):
                answer.append(transaction)
        answer.sort(key=lambda x: int(x.split(',')[1]))
        return answer

transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
solution = Solution()
print(solution.invalidTransactions(transactions))