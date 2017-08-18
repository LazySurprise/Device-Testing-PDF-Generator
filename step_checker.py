steps = ['step1', 'step2', 'step3']

def step_check(step):

    sect_list =  [1, 2, 3]
    for sect in sect_list:
        step_checker = 'step{}'.format(sect_list.index(sect) + 1)
        if step == step_checker:
            return step

for step in steps:
    print(step_check(step))


# get rid of ''
mylist = ['Section7_1', 'Section7_2', 'Section7_3', 'Section7_4', 'Section7_5', 'Section7_6', 
            'Section7_7', 'Section7_8', 'Section7_9', 'Section8', 'Section9', 'Section10_1', 'Section10_2']

def lowercase_first_letter(s):
    
    return s[0].lower() + s[1:]

def uppercase_first_letter(s):
    
    return s[0].upper() + s[1:]

newlist = []
for item in mylist:
    
    item = lowercase_first_letter(item)
    newlist.append(item)
print(newlist)

 

# admin.site.register loop
section_list_lowercase = ['section1', 'section2', 'section3', 'section4', 'section5',
        'section6', 'section7_1', 'section7_2', 'section7_3', 'section7_4',
        'section7_5', 'section7_6', 'section7_7', 'section7_8', 'section7_9', 'section8',
        'section9', 'section10_1', 'section10_2']


for section in section_list_lowercase:
    section = uppercase_first_letter(section)
    item = 'admin.site.register(models.{}'.format(section) + ')'
    print(item)
    
