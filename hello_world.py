garbled = "��¼+IM+SDK+ʧ��"
# 获取乱码的字节
bytes_data = garbled.encode('utf-8')
# 假设中间是 Latin-1 解码出错，尝试逆向
try:
    step1 = bytes_data.decode('latin-1')
    step2 = step1.encode('latin-1').decode('utf-8')
    print(step2)
except UnicodeDecodeError as e:
    print("解码失败:", e)/Users/dumingwei/Downloads/tchoused_sql_export_20250315163449.csv