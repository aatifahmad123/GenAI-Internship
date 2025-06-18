import json

json_file_path = "dataHinglish.json"
working_dir = f'../Google Cloud Hinglish'

with open(json_file_path, "r", encoding="utf-8") as jsonf:
    data = json.load(jsonf)

for i in range(1,51):
    call_id = f'{i:02d}'
    key = f'call_{call_id}'
    value = data.get(key, {})

    agent = 0
    if i % 10 == 0:
        agent = i // 10
    else:
        agent = (i // 10) + 1

    call = i - (10 * (agent - 1))

    call_folder = f"{working_dir}/Agent {agent:02d}/Call {call:02d}"
    
    with open(f'{call_folder}/data.json', 'w', encoding='utf-8') as f:
        json.dump(value, f, ensure_ascii=False, indent=4)


    


