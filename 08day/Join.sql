select * from emp2;
select * from dept2;

select * 
from emp2 e, dept2 d
where (e.deptno = d.deptno)
 and  (e.ename = 'Jane');

select * 
from emp2 e join dept2 d on (e.deptno = d.deptno)
where (e.ename = 'Jane');

select * 
from emp2 e join dept2 d on (e.deptno = d.deptno);

select * 
from emp2 e inner join dept2 d on (e.deptno = d.deptno);

select * 
from emp2 e natural join dept2 d ;

select * 
from emp2 e join dept2 d using (deptno);

select * 
from emp2 e left OUTER join dept2 d on (e.deptno = d.deptno);

select * 
from dept2 d  left OUTER join emp2 e on (e.deptno = d.deptno);

--> left / right / full outer join 

SELECT d.dname, count(e.ename)
from dept2 d left outer join emp2 e using(deptno)
group by d.dname;