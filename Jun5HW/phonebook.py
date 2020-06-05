import json

with open('phonebook.json', 'rb') as f:
    pb = json.load(f)

def lookup(lu_name):
    resp = pb.get(lu_name)
    if resp != None:
        print(resp)
    else:
        print('Not in Phonebook')

while True:
    print('''\nElectronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit''')
    funct = input('')
    print('')

    if funct == "1":
        lu_name = input("Name to Lookup? ")
        lookup(lu_name)

    if funct == "2":
        set_name = input('Name to add? ')
        set_num = input('Number to add? ')
        pb[set_name] = set_num

    if funct == "3":
        del_name = input('Name to delete? ')
        try:
            del pb[del_name]
        finally:
            pass

    if funct == "4":
        for key in pb:
            print(key + " : " + pb[key])

    if funct == "5":
        json = json.dumps(pb)
        b = open('phonebook.json', 'w')
        b.write(json)
        b.close()
        break