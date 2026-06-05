import json
while 1:
    try:
        with open("records.json","r") as f:
            records=json.load(f)
    except FileNotFoundError:
        records=[]
    q={}
    print("="*10,"菜单","="*10,sep="")
    print("1.添加支出记录\n2.查看所有支出记录\n3.退出程序")
    n=input("请输入数字：")
    if n=="1":
        for i in ["金额","类别","备注"]:
            q[i]=input(f"输入{i}:")
        records.append(q)
        with open("records.json","w") as f:
            json.dump(records,f)
    elif n=="2":
        for j in records:
            print(j)

    elif n=="3":
        break
    else:
        print("输入不合法，请重新输入:")
        continue

