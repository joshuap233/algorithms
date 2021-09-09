# https://leetcode-cn.com/problems/validate-ip-address/
# 468. 验证IP地址


class Solution:
    """
        这题目描述...真是吐了...

        同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如:
            02001:0db8:85a3:0000:0000:8a2e:0370:7334
        是无效的

        这里多余的 0 指的是 02001 超过了 4 位....
    """
    def validIPAddress(self, ip: str) -> str:
        def validIpv4() -> bool:
            ips = ip.split('.')
            if len(ips) != 4:
                return False

            for i in ips:
                if len(i) > 3:
                    return False
                if len(i) >= 2 and i[0] == '0':
                    return False
                if i > '255' or (not i.isdigit()):
                    return False
            return True

        def validIpv6() -> bool:
            ips = ip.split(':')
            if len(ips) != 8:
                return False

            for i in ips:
                if len(i) == 0 or len(i) >= 5:
                    return False
                try:
                    int(i, base=16)
                except:
                    return False
            return True

        if '.' in ip:
            return 'IPv4' if validIpv4() else 'Neither'
        return 'IPv6' if validIpv6() else 'Neither'


s = Solution()
s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")
