class Solution:
    def validIPAddress(self, IP: str) -> str:
        i4x = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        pat4 = re.compile(r'^(' + i4x + r'\.){3}'+ i4x + r'$')

        i6x = r'([A-Fa-f0-9]{1,4})'
        pat6 = re.compile(r'^(' + i6x + r'\:){7}' + i6x + r'$')

        if pat4.match(IP):
            return "IPv4"
        elif pat6.match(IP):
            return "IPv6"
        else:
            return "Neither"