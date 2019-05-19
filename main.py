import sqlite3 as lite
import sys
import pickle

con = None

query_string_first_task = '''
select CustomerId, FirstName, Company, Phone, Email from Customer as c
where 50 < (select 2019 - BirthDate from Employee as e where e.EmployeeId == c.SupportRepId) and
      exists(select t.GenreId
             from (Invoice
              inner join InvoiceLine on Invoice.InvoiceId = InvoiceLine.InvoiceId
              inner join Track on InvoiceLine.TrackId = Track.TrackId)
          where c.CustomerId = t.CustomerId and t.GenreId != (select GenreId from Genre where Name == 'Rock'))
order by c.City, c.Email DESC limit 10
'''

query_string_second_task = '''
select FirstName, Phone, ReportsTo from Employee where ReportsTo
'''

query_string_third_task = '''
SELECT FirstName, Phone from Customer as c
'''


def dbBase(query_string):
    try:
        con = lite.connect('Chinook_Sqlite.sqlite')    
        cur = con.cursor()
        cur.execute(query_string)  

        con.commit()   
        data = cur.fetchall()  
        print(data)
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        if con is not None:
            con.close()
    return data
