import unittest
from collections import defaultdict

class AccountsMerge(unittest.TestCase):
    """
    Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0]
    is a name, and the rest of the elements are emails representing emails of the account.

    Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some
    common email to both accounts. Note that even if two accounts have the same name, they may belong to different
    people as people could have the same name. A person can have any number of accounts initially,
    but all of their accounts definitely have the same name.

    After merging the accounts, return the accounts in the following format:
    the first element of each account is the name, and the rest of the elements are emails in sorted order.
    The accounts themselves can be returned in any order.

    Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

    Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]]
    """
    def accounts_merge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_graph, used_emails, result = defaultdict(list), set(), []

        # build graph
        for a in accounts:
            # start at 2 bc we only need to add nodes to graph if account has > 1 email.
            # (0 = name, 1 = 1st email 2 or higher = additional emails)
            for i in range(2, len(a)):
                curr_email, prev_email = a[i], a[i-1]
                email_graph[curr_email].append(prev_email)
                email_graph[prev_email].append(curr_email)

        # recursive dfs function
        def dfs(email):
            used_emails.add(email)
            email_list = [email]
            # find any associated emails
            for eml in email_graph[email]:
                if eml not in used_emails:
                    email_list.extend(dfs(eml))
            return email_list

        # build result
        for a in accounts:
            user, first_email = a[0], a[1]
            if first_email not in used_emails:
                result.append([user] + sorted(dfs(first_email)))
        return result

    def test_accounts_merge(self):
        accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        output = [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"],
                 ["John", "johnnybravo@mail.com"]]
        self.assertEqual(sorted(self.accounts_merge(accounts)), sorted(output))