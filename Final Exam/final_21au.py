# Name: Agnes Li
# CSE 160
# Autumn 2021
# Final Exam

from operator import itemgetter


# Problem 1
def least_exp_store(ingred_price_dict, ingred1, ingred2):
    '''
    Arguments:
        ingred_price_dict: a dict of price_lists
        ingred1, ingred2: 2 strings representing ingredients

    Returns:
        A list containing two elements: a string representing the least
        expensive store to purchase ingred1 and ingred2 at, and the total cost
        of the two ingredients at that store. If there is a tie for lowest
        cost, returns the store with the higher index.
    '''
    # your solution code should start here
    store_num = 0
    ingred1_prices = ingred_price_dict[ingred1]
    ingred2_prices = ingred_price_dict[ingred2]
    store_total = {}
    for each in range(len(ingred1_prices)):
        store_total[store_num] = ingred1_prices[each] + ingred2_prices[each]
        store_num += 1
    store_total_sorted = sorted(store_total.items(), key=itemgetter(1))
    if len(store_total_sorted) > 1:
        if (store_total_sorted[0][1] == store_total_sorted[1][1]):
            return ["Store " + str(store_total_sorted[1][0]),
                    store_total_sorted[1][1]]
        else:
            return ["Store " + str(store_total_sorted[0][0]),
                    store_total_sorted[0][1]]
    else:
        return ["Store " + str(store_total_sorted[0][0]),
                store_total_sorted[0][1]]


def test_least_exp_store():
    ingred_price_dict = {"Flour": [1, 2, 3], "Sugar": [20, 19, 24],
                         "Butter": [2, 3, 4], "Molasses": [6, 7, 5]}

    assert least_exp_store(ingred_price_dict,
                           "Butter", "Molasses") == ["Store 0", 8]
    assert least_exp_store(ingred_price_dict,
                           "Flour", "Sugar") == ["Store 1", 21]

    ingred_price_dict2 = {"Flour": [10], "Sugar": [30]}

    assert least_exp_store(ingred_price_dict2,
                           "Flour", "Sugar") == ["Store 0", 40]


# Problem 2
def customer_loyalty(visit_tracker):
    '''
    Arguments:
        visit_tracker: a dictionary mapping customer names to a list of
        their visits to bubble tea stores

    Returns:
        a dictionary mapping stores to a set of their loyal customers.
        If a store does not have any loyal customers, it is not
        included in the returned dictionary. If the visit_tracker is empty
        or if there are no loyal customers, return an empty dictionary.
    '''
    # your solution code should start here
    stores_loyal_cust = {}
    for customer, visits in visit_tracker.items():
        stores_visited = {}
        for i in visits:
            if i not in stores_visited:
                stores_visited[i] = 0
            stores_visited[i] += 1
        sorted_stores_visited = sorted(stores_visited.items(),
                                       key=itemgetter(1), reverse=True)
        for store, total_visits in sorted_stores_visited:
            if total_visits >= 3 and len(sorted_stores_visited) <= 2:
                if store not in stores_loyal_cust:
                    stores_loyal_cust[store] = set()
                stores_loyal_cust[store].add(customer)
    return stores_loyal_cust


def test_customer_loyalty():
    visit_tracker1 = {"Evan": ["Ding Tea", "Ding Tea", "Yi Fang",
                               "Ding Tea", "Ding Tea"],
                      "Izzy": ["Boba Up", "Ding Tea", "Boba Up",
                               "Boba Up", "Ding Tea", "Ding Tea", "Ding Tea"]}

    assert customer_loyalty(visit_tracker1) == {"Boba Up": {"Izzy"},
                                                "Ding Tea": {"Evan", "Izzy"}}

    visit_tracker2 = {"Jackie": ["DIY Tea", "DIY Tea", "DIY Tea"],
                      "Evan": ["Yum Tea", "Ding Tea",
                               "Yi Fang", "Yum Tea", "Yum Tea"]}

    assert customer_loyalty(visit_tracker2) == {"DIY Tea": {"Jackie"}}


# Problem 3
def never_win(match_tuples):
    '''
    Arguments:
        match_tuples: a list of tuples that are size 2 representing matches
        played. Each tuple is in the form (string, boolean), which represents
        the champion played for the match and whether the match was won
        (True for won, False for lost). Assume match_tuples is not empty.

    Returns: a list of the unique champions that have no matches won in
        match_tuples, sorted in alphabetical order. Returns an empty list if
        there are no champions with zero matches won.
    '''
    # your solution code should start here
    winners = set()
    all_champs = set()
    for i in match_tuples:
        all_champs.add(i[0])
        if i[1] is True:
            winners.add(i[0])
    zero_won = sorted(list(set((all_champs - winners))))
    return zero_won


def test_never_win():
    win_list1 = [("Ezreal", False), ("Yasuo", False), ("Teemo", False),
                 ("Jinx", True), ("Ezreal", True), ("Teemo", False)]
    assert never_win(win_list1) == ["Teemo", "Yasuo"]
    assert never_win([('Ezreal', True), ('Yasuo', True),
                      ('Jinx', False), ('Jinx', True)]) == []


def main():
    test_least_exp_store()
    test_customer_loyalty()
    test_never_win()


if __name__ == "__main__":
    main()


# You will answer a question about collaboration in part 2.
