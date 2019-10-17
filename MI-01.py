def get(st):
  part = st.split('@')
  localList = part[0].split('+')
  local = "".join(localList[0].split('.'))
  domain = part[1]
  return local + "@" + domain
def numUniqueEmails(emails):
    mailList = []
    for email in emails:
      standardMail = get(email)
      print(standardMail)
      if standardMail not in mailList:
        mailList.append(standardMail)
    return len(mailList)

List = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]

print(numUniqueEmails(List))