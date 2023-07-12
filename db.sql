drop database if exists ems_6jan26;
create database if not exists ems_6jan23;
use ems_6jan23;

create table if not exists employee
(
id int unsigned primary key,
name varchar(100) not null,
salary decimal(10,8) unsigned not null
);
desc employee;




delimiter $$
drop trigger if exists t1 $$
create trigger t1 before insert on employee for each row
begin
	if(new.id is null) or (new.id < 1) then
		signal SQLSTATE '11111' set message_text = "Invalid ID";
	end if;


	if(new.name is null) or (length(trim(new.name))=0)
	or (length(new.name) < 2) or (not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '22222' set message_text = "Invalid name";
	end if;


	if(new.salary is null) or (new.salary < 8000) then
		signal SQLSTATE '33333' set message_text = "Salary shoud not be null/below 8k";
	end if;

end $$
drop trigger if exists t2 $$
create trigger t2 before update on employee for each row
begin
	if(new.id is null) or (new.id < 1) then
		signal SQLSTATE '11111' set message_text = "Invalid ID";
	end if;


	if(new.name is null) or (length(trim(new.name))=0)
	or (length(new.name) < 2) or (not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '22222' set message_text = "Invalid name";
	end if;


	if(new.salary is null) or (new.salary < 8000) then
		signal SQLSTATE '33333' set message_text = "Salary shoud not be null/below 8k";
	end if;
end $$
delimiter ;

