import json

me = [
    {
        "csdn": "John",
        "age": 23
    },
    {
        "major": "cs",
        "years": 4
    }
]
with open('me.json', 'w') as file:
    file.write(json.dumps(me, indent=2))  # indent为了缩进
import json

with open('me.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)
    print(type(data))  # python列表的类型
