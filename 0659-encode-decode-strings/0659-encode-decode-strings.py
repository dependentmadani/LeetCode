class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        joiner = "hamid"
        result = ""
        result = joiner.join(strs)
        return result

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        result = []
        spliter = "hamid"
        result = str.split(spliter)
        return result
