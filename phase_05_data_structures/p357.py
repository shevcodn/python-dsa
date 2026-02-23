def unique_emails(emails):
    unique = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.','')
        unique.add(local + '@' + domain)
    
    return len(unique)
    
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(unique_emails(emails))
