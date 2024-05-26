#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self._discount = discount
        self._total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value

    @property
    def total_due(self):
        """Property to get the current total amount due."""
        return self._total

    @property
    def total(self):
        """Property to get the current total amount including discounts."""
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def add_item(self, item, price, quantity=1):
        self._total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({"item": item, "quantity": quantity, "price": price})

    def apply_discount(self):
        if self._discount:
            self._total = int(self._total * ((100 - self._discount) / 100))
            print(f"After the discount, the total comes to ${self._total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        transaction = self.previous_transactions.pop()
        self._total -= transaction["price"] * transaction["quantity"]
        for _ in range(transaction["quantity"]):
            self.items.pop()