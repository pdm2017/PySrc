create table emp(
  empno    number,
  ename    varchar2(10),
  job      varchar2(9),
  mgr      number(4,0),
  hiredate date,
  sal      number(7,2),
  comm     number(7,2),
  deptno   number,
  constraint pk_emp primary key (empno),
  constraint fk_deptno foreign key (deptno) references dept (deptno)
);

insert into emp values( 7839, 'KING', 'PRESIDENT', null, date('1996-11-17'), 5000, null, 10);
insert into emp values( 7698, 'BLAKE', 'MANAGER', 7839, date('1991-01-05'), 2850, null, 30);
insert into emp values( 7782, 'CLARK', 'MANAGER', 7839, date('1999-09-06'), 2450, null, 10);
insert into emp values( 7566, 'JONES', 'MANAGER', 7839, date('2001-02-04'), 2975, null, 20);
insert into emp values( 7788, 'SCOTT', 'ANALYST', 7566, date('2003-06-17'), 3000, null, 20);
insert into emp values( 7902, 'FORD', 'ANALYST', 7566, date('1981-03-12'), 3000, null, 20);
insert into emp values( 7369, 'SMITH', 'CLERK', 7902, date('2007-12-01'), 800, null, 20);
insert into emp values( 7499, 'ALLEN', 'SALESMAN', 7698, date('1981-02-20'), 1600, 300, 30);
insert into emp values( 7521, 'WARD', 'SALESMAN', 7698, date('1981-02-22'), 1250, 500, 30);
insert into emp values( 7654, 'MARTIN', 'SALESMAN', 7698, date('1981-09-28'), 1250, 1400, 30);
insert into emp values( 7844, 'TURNER', 'SALESMAN', 7698, date('1981-09-08'), 1500, 0, 30);
insert into emp values( 7876, 'ADAMS', 'CLERK', 7788, date('1987-07-13'), 1100, null, 20);
insert into emp values( 7900, 'JAMES', 'CLERK', 7698, date('1981-03-12'), 950, null, 30);
insert into emp values( 7934, 'MILLER', 'CLERK', 7782, date('2003-01-23'), 1300, null, 10);


