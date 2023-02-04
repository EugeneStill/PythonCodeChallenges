import unittest


class KthGrammar(unittest.TestCase):
    # def kth_symbol(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: int
    #     """
    #     print("\nN: {} K: {}".format(n, k))
    #     if n == 1 or k == 1:
    #         return 0
    #     whole, rem = divmod(k, 2)
    #     print("WHOLE: {} REM: {}".format(whole, rem))
    #     if self.kth_symbol(n - 1, whole + rem):
    #         return rem
    #     print("REM IS {}".format(rem))
    #     return 1 - rem


    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==1:
            if k==1:
                return 0
            else:
                return 1
        # for any level n, the first half of the string is the same as the string in n-1
        # get half point of n and handle K depending on which half of n, k is in
        half=2**(n - 1)
        # if K is in first half of n then return the position of k in n-1
        if k<=half:
            return self.kthGrammar(n - 1, k)
        # 2nd half of n is mirror of 1st half, so get k position in n-1 and flip result
        else:
            res=self.kthGrammar(n - 1, k - half)
            if res==0:
                return 1
            else:
                return 0
    def test_kth(self):
        self.assertEqual(self.kth_symbol(2, 2), 1)