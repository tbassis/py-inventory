from datetime import datetime, date


class BaseItem:
    """Base of all items in the inventory.
    
    attributes: title, author, info, release_year, purchase_year, purchase_price, giveaway_year, giveaway_price
    """

    def __init__(self, title, author, info, release_year, purchase_year = datetime.now().date(), purchase_price = 0.00,
     giveaway_year = None, giveaway_price = 0.00):
        self.title = title
        self.author = author
        self.info = info
        self.release_year = release_year
        self.purchase_year = purchase_year
        self.purchase_price = purchase_price
        self.giveaway_year = giveaway_year
        self.giveaway_price = giveaway_price

    def item_age(self):
        """TIme I own the item."""
        time_with_me = datetime.now().date().year - self.purchase_year.year
        return time_with_me
    
    def work_age(self):
        """Time since the release of the work."""
        age = datetime.now().date().year - self.release_year.year
        return age

    def money_invested(self):
        """Amount that the money impacted my finances."""
        amount = self.giveaway_price - self.purchase_price
        return amount


class Book(BaseItem):
    def __init__(self, title, author, genre, publisher, info, release_year, purchase_year, purchase_price, giveaway_year, giveaway_price):
        super().__init__(title, author, info, release_year, purchase_year, purchase_price, giveaway_year, giveaway_price)
        self.genre = genre
        self.publisher = publisher
    pass


class CD(BaseItem):
    pass


class Vinyl(BaseItem):
    pass