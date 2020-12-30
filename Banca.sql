create database Banca;
use Banca;

create table ADMINISTRADOR(
Nombre varchar(15) not null,
contra varchar(20) not null,
primary key(Nombre)
);
insert into ADMINISTRADOR(Nombre,contra) values('admin','admin');
select * from clienteindividual;


create table USUARIOINDIVIDUAL(
CUI bigint(20) primary key,
NIT int(11),
nombres varchar(30),
apellidos varchar(30),
fechaNacimiento date
);

create table USUARIOEMPRESARIAL(
idUsuarioemp int auto_increment primary key,
tipoEmpresa enum('sociedad anonima','compañia limitada','empresa individual'),
nombre varchar(40),
nombreComercial varchar(40),
nombresRepresentante varchar(35),
apellidosRepresentante varchar(35)
);
create table USUARIO(
idUsuario int auto_increment primary key,
contra varchar(20),
CUI bigint(20),
idUsuarioemp int,
foreign key (CUI) references USUARIOINDIVIDUAL(CUI),
foreign key (idUsuarioemp) references USUARIOEMPRESARIAL(idUsuarioemp)
);
alter table USUARIO add deuda decimal(65,3);
alter table USUARIO add cantidadtarjetas int(1);
alter table USUARIO modify cantidadtarjetas int(1) default 0;
DESC USUARIO;

create table CUENTA(
numerocuenta int auto_increment primary key,
idUsuario int,
tipomoneda enum('Q','$'),
estaActiva enum('si','no'),
foreign key(idUsuario)references USUARIO(idUsuario)
);
alter table cuenta add tipocuenta enum('ahorro','monetaria','plazo fijo');

create table CUENTAMONETARIA(
numerocuenta int primary key,
preautoriza enum('si','no'),
nocheques int(2),
foreign key(numerocuenta) references CUENTA(numerocuenta)
);

create table CUENTAAHORRO(
numerocuenta int primary key,
interes int,
saldo decimal(35,3),
foreign key(numerocuenta) references CUENTA(numerocuenta)
);

insert into cuenta(idUsuario,tipomoneda,estaActiva,tipocuenta) values(1,'Q','si','ahorro');
insert into cuentaahorro values(2,2,50484.50);

create table CUENTAPF(
numerocuenta int primary key,
interes int,	
saldo decimal(35,3),
tiempo enum('3','6','12','24'),
foreign key(numerocuenta) references CUENTA(numerocuenta)
);

create table TARJETADECREDITO(
numerotarjeta int auto_increment primary key ,
idUsuario int,
marca enum('puntos','cashback'),
foreign key(idUsuario)references USUARIO(idUsuario)
);

create table TARJETADEPUNTOS(
numerotarjeta int primary key,
limite decimal(15,3),
puntos decimal(35,3) default 0,
foreign key(numerotarjeta) references TARJETADECREDITO(numerotarjeta)
);
insert into tarjetadepuntos(numerotarjeta,limite,puntos) values(1,250,120);

create table TARJETADECASHBACK(
numerotarjeta int primary key,
limite decimal(15,3),	
cashback decimal(35,3) default 0,
foreign key(numerotarjeta) references TARJETADECREDITO(numerotarjeta)
);

create table COMPRATARJETA(
id_compra int auto_increment primary key,
fechacompra date,
idUsuario int,
descripcion varchar(60),
monto decimal(15,2),
numerotarjeta int,
moneda enum('Q','$'),
foreign key(idUsuario)references USUARIO(idUsuario),
foreign key(numerotarjeta) references TARJETADECREDITO(numerotarjeta)
);


drop table tarjetadecredito;
drop table tarjetadepuntos;
drop table tarjetadecashback;

/*PRUEBAS*/
update usuario set cantidadtarjetas = 0 where idusuario !=0;
insert into USUARIO(cantidadtarjetas) values(1);
desc usuario;

select * from tarjetadecredito where idUsuario=2;
select * from usuario;	
select * from tarjetadecredito;
select * from tarjetadecashback;
select * from tarjetadepuntos;
select * from cuenta where idUsuario=1;
insert into TARJETADECREDITO(idUsuario,marca) values(3,'puntos');




