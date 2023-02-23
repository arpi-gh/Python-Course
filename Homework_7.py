'''Ստեղծել contacts.txt ֆայլ, ավելացնել հետևյալ
(First_Name Last_Name, Title, Extension, Email)  տեքստը՝ օգտագվելով Python-ի ֆայլային ֆունկցիոնալից,
դուրս բերել AUTHORS: դաշտը իր ենթատողերով և ավելացնել contacts.txt ֆայլում։
Վերջնական պատկերը պետք է լինի հետևյալը
First_Name Last_Name, Title, Extension, EmailAUTHORS:
Amy Baker, Finance Chair, x345, abaker@ourcompany.com
Chris Donaldson, Accounting Dir., x621, cdonaldson@ourcompany.com
Erin Freeman, Sr. VP, x879, efreeman@ourcompany.com
'''

import PyPDF2


contacts = open('contacts.txt', 'w')
contacts.write('First_Name\tLast_Name\tTitle\tExtension\tEmail\t')
contacts.close()
contacts = open('contacts.txt')
file = PyPDF2.PdfReader('Business_Proposal.pdf')
page = file.pages[1]
page_content = page.extract_text().splitlines()
page_content = page_content[1:]
contacts = open('contacts.txt', 'a')
contacts.write('\n')
for line in page_content:
    contacts.write(line)
    contacts.write('\n')
contacts.close()
contacts = open('contacts.txt')
contacts_content = contacts.read()
print(contacts_content)



