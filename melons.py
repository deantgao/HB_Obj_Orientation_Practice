"""Classes for melon orders."""

import random


class AbstractMelonOrder(object):
    """docstring for AbstractMelonOrder"""
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        #self.passed = False

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melon":
            base_price = 5 * 1.5
        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """ """

    # passed_inspection = False

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0)
        self.passed_inspection = False

    # def inspect(self):
    #     """Inspect the order"""

    #     return random.choice([True, False])


    def mark_inspection(self, passed):
        """Record the fact that an order has passed inspection."""
        # if passed:
        #     self.passed_inspection = True
        self.passed_inspection = passed



# order = GovernmentMelonOrder("watermelon", 8)
# did_pass = order.inspect()
# order.mark_inspection(did_pass)


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total = total + 3

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
