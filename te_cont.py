
import socket
import sys
# from  sesstion.sessio import Session
# from  sesstion.sessio import session_manger
HEADER=64
# DISCONNECT_MESSAGE='DISCONNECT'
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def send(msg,conn):
    message=msg.encode('utf-8')
    msg_len=len(message)
    send_length=str(msg_len).encode('utf-8')

    send_length+=b' ' * (HEADER -len(send_length))
    conn.send(send_length)
    print(message,"masss")
    conn.send(message)

def recv_msg(conn):
    msg_length=conn.recv(64).decode('utf-8')
    if msg_length:
        msg_length=int(msg_length)
        return conn.recv(msg_length).decode('utf-8')
    else:
        return False
class TYPE:

    NODE='node'
    COLUMN='column'
    TYPLE='typle'
    DOCUMENT='document'


class connect:

    connected=False
    strConnet=None
    def __repr__(self):
        return repr(self.strConnet)
    def __init__(self,hostname=socket.gethostname(),username='root',password='beta',dbname='beta',port='1515'):

        self.hostname=hostname
        self.username=username
        self.password=password
        self.dbname=dbname
        self.port=int(port)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:

            s.connect((self.hostname, self.port))
            self.conn=s
        except ConnectionRefusedError:

            s=False
        self.helpcon=self.logining(s)
        if self.helpcon==True:

            self.strConnet='Successfully connection'
        elif self.helpcon==-2:
            self.strConnet='Error in db name'
        elif self.helpcon==-3:
            self.strConnet='error on hostname or port'

        else:
            self.strConnet='Error in user or pass'

    def isConnected(self):
        return self.connected




    def logining(self,conn):

        query="{'user':'"+self.username+"','pass':'"+self.password+"','db':'"+self.dbname+"'}"
        if conn==False:
            return -3
        msg=recv_msg(conn)

        if 'login' == msg:
            send(query,conn)
            msg = recv_msg(conn)


            if msg =='sql':
                self.connected=True
                print("yes")
                return True
            elif msg =='error cxdb name':
                conn.close()
                return -2
            else:
                print("no")
                conn.close()
                return False



    def cursor(self):
        if self.connected==False:
            print('Login')
            return -1

        return self.temp_cor(self.conn)








    class temp_cor:
        def __init__(self,conn):
            self.conn=conn

        def delete(self):
            pass

        def insertTable(self,TableKey,valuesOnJson):
            query = "insert table.rows " + str(valuesOnJson) + " to " + TableKey
            return self.exQuery(query)
        def insertColumn(self,ColumnKey,value):
            query="insert column.row '"+value+"' to "+ColumnKey
            return self.exQuery(query)

        def AlterName(self):
            pass
        def updateColumnRow(self):
            pass
        def updateTableRows(self):
            pass

        def updateDocument(self,DocumentKey, valueJson):

            query = "update document " + str(valueJson) + " to " + DocumentKey
            return self.exQuery(query)

        def createDocument(self,onKey,DocumentKey,valueJson):
            query = "create document " + DocumentKey +" "+str(valueJson)+ " to " + onKey
            return self.exQuery(query)



        def execute(self, query):

            send(query, self.conn)

            code = recv_msg(self.conn)

            return self.ex(self.conn,code)

        def exQuery(self, query):

            send(query, self.conn)

            code = recv_msg(self.conn)

            return code
        def exQuery1(self, query):
            # se_code=f"create column {query} to ahmed.person.cahmed;"
            send(query, self.conn)
            print(query, "ffddfff")
            code = recv_msg(self.conn)
            print(code, "fffff")
            return code
        class ex:

            def __init__(self,conn,code):
                self.conn=conn
                self.code=code
                print(self.code)

            def Next(self):
                send('next'+self.code,self.conn)
                return recv_msg(self.conn)



            def fetchall(self):
                temp=None
                if temp==-1:
                    return -1
                while temp!='-1':
                    temp=self.Next()
                    yield temp


            def close(self):

                self.conn.close()



        def close(self):

            self.conn.close()


