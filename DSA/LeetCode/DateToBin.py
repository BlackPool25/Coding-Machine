class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        year,month,day = map(int, date.strip().split("-"))
        return f"{bin(year)[2:]}-{bin(month)[2:]}-{bin(day)[2:]}"
    