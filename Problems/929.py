class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_dict = {}
        for email in emails:
            new_email = email
            #print(new_email)
            at_rate_index = new_email.find('@')
            plus_index = new_email.find('+')
            if plus_index < at_rate_index and plus_index != -1:
                #print('+', new_email)
                new_email = email[:plus_index] + email[at_rate_index:]
            
            at_rate_index = new_email.find('@')
            dot_index = new_email.find('.')
            
            if dot_index < at_rate_index:
                #print('dot', new_email)
                new_email = new_email[:at_rate_index].replace('.','') + new_email[at_rate_index:]
            
            email_dict[new_email] = 1
            
        #print(email_dict)
        return len(email_dict.keys())