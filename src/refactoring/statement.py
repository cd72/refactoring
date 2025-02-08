class Statement:
    def amount_for(self, a_performance: dict, play) -> int:
        result = 0

        if play["type"] == "tragedy":
            result = 40000
            if a_performance["audience"] > 30:
                result += 1000 * (a_performance["audience"] - 30)
        elif play["type"] == "comedy":
            result = 30000
            if a_performance["audience"] > 20:
                result += 10000 + 500 * (a_performance["audience"] - 20)
            result += 300 * a_performance["audience"]
        else:
            raise ValueError(f"unknown type: {play['type']}")

        return result


    def statement(self, invoice, plays):
        total_amount = 0
        volume_credits = 0
        result = f"Statement for {invoice['customer']}\n"

        def format(amount):
            return f"${amount:,.2f}"

        for perf in invoice["performances"]:
            play = plays[perf["playID"]]
            this_amount = self.amount_for(perf, play)

            # add volume credits
            volume_credits += max(perf["audience"] - 30, 0)
            # add extra credit for every ten comedy attendees
            if play["type"] == "comedy":
                volume_credits += perf["audience"] // 5

            # print line for this order
            result += f"  {play['name']}: {format(this_amount / 100)} ({perf['audience']} seats)\n"
            total_amount += this_amount

        result += f"Amount owed is {format(total_amount / 100)}\n"
        result += f"You earned {volume_credits} credits\n"
        return result
