# metaclass learn
# a simple orm
import pymysql.cursors

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='learn',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connect.cursor()


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return f'<{self.__class__.__name__}: self.name>'


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')


class ModelMetaClass(type):
    """
    __new__()方法接收到的参数依次是：

    cls,
    准备创建类的名字；
    类继承的父类集合；
    类的属性/方法{名字:方法/属性}

    class Animal(object):
    def __new__(cls, *args, **kwargs):
        print("in __new__")
        instance = object.__new__(cls)
        return instance

    为什么要继承至type:
        1,普通类"实例化"时,会调用自己(或父类)的__new__方法
        2,__new__方法返回要创建的实例(object.__new__(cls)创建),object.__new__()只接收一个参数,
        3,元类(type的子类)的子类"加载"时,会调用元类的__new___方法(type.__new__()),type.__new__(),可接受多个参数,用于动态修改类
        4,普通__new__方法 返回 object.__new__(),元类返回type.__new__()
    """

    def __new__(mcs, name, bases, attrs: dict):
        if name == 'Model':
            return type.__new__(mcs, name, bases, attrs)
        table = {key: value for key, value in attrs.items() if isinstance(value, Field)}
        table_name = attrs.get('__tablename__', name.lower())
        attrs.clear()
        attrs['__table__'] = table
        attrs['__tablename__'] = table_name
        return type.__new__(mcs, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Model' object has no attribute '{key}'")

    def save(self):
        fields = []
        value = []
        for k, v in self.__table__.items():
            fields.append(v.name)
            value.append(getattr(self, k, None))
        sql = f'INSERT INTO `{self.__tablename__}` ({",".join(fields)}) VALUES ({",".join(["%s"] * len(value))});'
        cursor.execute(sql, tuple(value))
        connect.commit()

    def insert(self, **kwargs):
        fields = []
        value = []
        for k, v in kwargs.items():
            if self.__table__.get(k):
                fields.append(k)
                value.append(v)

        sql = f'INSERT INTO `{self.__tablename__}` ({",".join(fields)}) VALUES ({",".join(["%s"] * len(value))});'
        cursor.execute(sql, tuple(value))
        connect.commit()

    def query(self, field, value):
        if not self.__table__.get(field):
            return 'error'
        sql = f'SELECT {field} FROM `{self.__tablename__}` WHERE {field} = {value};'
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)
        connect.commit()

    def delete(self, field, value):
        sql = f'DELETE FROM {self.__tablename__} WHERE {field} = {value}'
        cursor.execute(sql)
        connect.commit()


class User(Model):
    __tablename__ = 'user'
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')


u = User(name='name', email='email', password='password')
u.save()
u.query('name', 'name')
u.delete('name', 'name')

"""
    sql = f'INSERT INTO {user} ({",".join(["name","password","email"])}) VALUES ({",".join(["password","name","email"])});'
    cursor.execute(sql)
    这样插入,提交到数据库后,值全为空
    正解:
    sql = f'INSERT INTO {user} ({",".join(["name", "password", "email"])}) VALUES (%s, %s, %s);'
    cursor.execute(sql, ("password", "name", "email"))
    
    sql = 'INSERT INTO %s ({",".join(["name", "password", "email"])}) VALUES (%s, %s, %s);'
    cursor.execute(sql, ("user","password", "name", "email"))
    这种写法,user会被转为字符串,插入失败
"""
# user = 'user'
# sql = f'INSERT INTO {user} ({",".join(["name","password","email"])}) VALUES (%s, %s, %s);'
# sql = f'INSERT INTO {user} ({",".join(["name", "password", "email"])}) VALUES (%s, %s, %s);'
# cursor.execute(sql, ("password", "name", "email"))
# connect.commit()
