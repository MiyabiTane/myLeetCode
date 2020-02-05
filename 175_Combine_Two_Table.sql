Create table Person (PersonId int, FirstName varchar(255), LastName varchar(255))
Create table Address (AddressId int, PersonId int, City varchar(255), State varchar(255))
Truncate table Person
insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen')
Truncate table Address
insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York')

select FirstName,LastName,City,State
/*left join : 右に指定されたテーブルに存在しなくても左のテーブルに存在すれば取得する*/
from Person left join Address
on Person.PersonId=Address.PersonId
;
/*参考サイト：https://qiita.com/naoki_mochizuki/items/3fda1ad6594c11d7b43c*/
