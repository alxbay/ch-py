import clickhouse_connect
client = clickhouse_connect.get_client(host='192.168.2.240', username='admin', password='qwe', database='db1',port='8123', client_name='oppa==popa')

result = client.query('select count() from hits_v1')

print(result.result_rows)
