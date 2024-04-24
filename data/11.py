import json

def transform_jsonl(input_file_path, output_file_path):
    # 打开原始的 JSONL 文件进行读取
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 准备新的数据集
    transformed_data = []
    
    # 遍历每一行数据
    for line in lines:
        # 解析 JSON 数据
        data = json.loads(line)
        
        # 提取需要的字段
        instruction = data['instruction']
        input_text = data['input']  # 假设每个任务只有一个实例
        output = data['output']
        
        # 构建新的 JSON 对象
        
        transformed_entry = {
            'instruction': instruction,
            'input': input_text,
            'output': output,
            'system':"You are a helpful system",
            'history':"",
        }
        # wrapped_data = [transformed_entry]
        transformed_data.append(transformed_entry)
        # wrapped_data=[transformed_data]

    
    # 打开输出文件，写入转换后的数据
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(transformed_data, output_file, ensure_ascii=False, indent=4)
        # for item in transformed_data:
        #     json_line = json.dumps(item,indent=4) + '\n'
        #     output_file.write(json_line)

# 调用函数进行文件转换
input_file_path = 'all_generated_instances.jsonl'
output_file_path = 'processed_seed_tasks.json'
transform_jsonl(input_file_path, output_file_path)
