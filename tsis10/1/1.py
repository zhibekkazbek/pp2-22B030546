from config import config
import psycopg2
import csv
import os


param = config()
connection = psycopg2.connect(**param)
cursor = connection.cursor()


mode = int(input(
"Select mode:\n1)add data from consol\n2)add data from csv file\n3)update data\n4)query data\n5)delete data\nEnter:"
))

if mode == 1:
    data = []
    name = input("Enter name:")
    number = input("Enter number:")
    data.append([name,number])
    for dat in data:
        cursor.execute(f"INSERT INTO phonebook (first_name,phone_number) VALUES ('{dat[0]}', {dat[1]})")
    
    connection.commit()
    print("Done")



elif mode == 2:
    path = input("Enter the csv file path:")
    data = []
    if not os.path.exists(path):
        print("ERROR: Path does not exists")
    with open(path) as file:
        row = csv.reader(file)
        next(row)

        for dat in row:
            data.append(dat)

    for row in data:
        cursor.execute(f"INSERT INTO phonebook (first_name, phone_number) VALUES ('{row[0]}', {row[1]})")

    connection.commit()
    print("Done !")



elif mode == 3:
    pname = input("Enter name of contact:")
    pnumber = int(input("Enter number of contuct:"))

    cursor.execute(f"SELECT * FROM phonebook WHERE first_name = '{pname}' AND phone_number = {pnumber}")
    if cursor.rowcount == 0:
        print("Contact does not exist")

    neni = input("first_name - update name\nphone_number - update number\nEnter:")
    if neni not in ['first_name','phone_number']:
        print('Error')


    if neni == 'first_name':
        zhana = str(input(f"Enter new {neni}:"))
        cursor.execute(f"UPDATE phonebook SET first_name = '{zhana}' WHERE phone_number = {pnumber}")


    elif neni == 'phone_2number':
        zhana = int(input("Enter new number:"))
        cursor.execute(f"UPDATE phonebook SET phone_number = {zhana} WHERE first_name = '{pname}'")

    else:print("error")


    connection.commit()
    print("Done")


elif mode == 4:
    kanday = int(input(
    "Choose query mode:\n1 - search by first_name\n2 - search by phone_number\n3 - query all rows(in the next section you can enter anything)\nEnter: "
    ))

    if kanday not in [1,2,3]:
        print("error")
        
    value = input("Enter query:")
    query_dict = {
        1 : f"WHERE first_name = '{value}'",
        2 : f"WHERE phone_number = {value}",
        3 : f""
        }
    
    cursor.execute(f"SELECT * FROM phonebook {query_dict[kanday]}")

    result = cursor.fetchall()
    if len(result) == 0:
        print("No results")
    else:
        print("Results:")

    for row in result:
        print(row)

elif mode == 5:
    mode1 = input("Select mode:\nname - delete by name\nnum - delete by number\nEnter:")

    if mode1 == 'name':
        data1 = str(input('Enter name:'))
        cursor.execute(f"DELETE FROM phonebook WHERE first_name = '{data1}'")

    elif mode1 == 'num':
        data1 = int(input(f"Enter number:"))
        cursor.execute(f'DELETE FROM phonebook WHERE phone_number = {data1}')

    else:print("error")

    connection.commit()
    print("Done")

else:print("Error")

connection.close()
cursor.close()