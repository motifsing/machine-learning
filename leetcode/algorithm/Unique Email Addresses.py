class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        email_set = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            index = local_name.find('+')
            if index:
                local_name = local_name[:index].replace('.', '')
            else:
                local_name = local_name.replace('.', '')
            email = '@'.join([local_name, domain_name])
            email_set.add(email)
        return len(email_set)

if __name__ == '__main__':
    email_list = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    solution = Solution()
    print(solution.numUniqueEmails(email_list))