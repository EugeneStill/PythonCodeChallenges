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
        graph, seen, ans = defaultdict(list), set(), []

        # build graph
        for acc in accounts:
            # starting at 2 bc we only need to add nodes to graph if account has > 1 email.  (0 = name, 1= 1st email)
            for i in range(2,len(acc)):
                # in the graph connect each email to the one before it in the account
                graph[acc[i]].append(acc[i-1])
                graph[acc[i-1]].append(acc[i])
                print(str(graph))

        # recursive dfs function
        def dfs(email):
            seen.add(email)
            emailList = [email]
            # if email isn't in graph then return email list, otherwise do dfs to add all connected emails to list
            for edge in graph[email]:
                if edge not in seen:
                    emailList.extend(dfs(edge))
            return emailList

        # dfs search of graph
        for acc in accounts:
            if acc[1] not in seen:
                ans.append([acc[0]] + sorted(dfs(acc[1])))
        return ans

    def test_accounts_merge(self):
        accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        output = [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"],
                 ["John", "johnnybravo@mail.com"]]
        self.assertEqual(sorted(self.accounts_merge(accounts)), sorted(output))