Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (Id, Salary) values ('1', '100')
insert into Employee (Id, Salary) values ('2', '200')
insert into Employee (Id, Salary) values ('3', '300')

/*
#select distinct : 重複データ削除
select distinct Salary as SecondHighestSalary
from Employee
#asc:昇順、desc:降順
order by Salary desc
#limit:返される行の数、offset:飛ばす行の数
limit 1 offset 1
*/

/*ifnull:NULLだった時に指定した値を返す*/
select
  ifnull(
    (select distinct Salary
    from Employee
    order by Salary desc
    limit 1 offset 1),
    null) as SecondHighestSalary
    
