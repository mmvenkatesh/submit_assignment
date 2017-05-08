import Module
from Module import db_operations


#create databse
a=Module.db_operations.Db_Operations('hyd1.db')
a.get_connection()

#create table in the databse
a=Module.db_operations.Db_Operations('hyd1.db')
query='create table New2(id int, age int)'
a.create_table(query)

#insert values in the database
a=Module.db_operations.Db_Operations('hyd1.db')
list2=[(4,20),(5,25),(6,35)]
query='insert into New values (?,?)'
a.insert_values_table(query,list2)

#delete values in the database
a=Module.db_operations.Db_Operations('hyd1.db')
query='delete from New where id=1'
a.delete_values_table(query)

#update values in the database
query='update New set age=40 where id=6'
a.update_values_table(query)



