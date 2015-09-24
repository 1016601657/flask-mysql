import MySQLdb

try:
    conn = MySQLdb.connect(host='192.168.199.180',user='zhaosha',passwd='sqC2QPTwpfX6J4M4',db='zhaosha',port=3306)
    cur = conn.cursor()
    res = cur.execute('select * from pb_eqm_members limit 10')
    result=cur.fetchone()
    print result
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])