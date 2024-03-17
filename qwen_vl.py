import dashscope
dashscope.api_key_file_path = "" #Your Aliyun Dashscope API Key Path. For more info: https://help.aliyun.com/zh/dashscope/developer-reference/api-key-settings

def qwen_vl(filepath):
    """Sample of use local file.
       linux&mac file schema: file:///home/images/test.png
       windows file schema: file://D:/images/abc.png
    """
    local_file_path1 = 'file://'+filepath
    messages = [{
        'role': 'system',
        'content': [{
            'text': 'You are a helpful assistant."'
        }]
    }, {
        'role':
        'user',
        'content': [
            {
                'image': local_file_path1
            },
            {
                'text': '回答格式为:"天气；摄影类型；最多10个画面中的物品。按照我要求的格式对图片进行描述。对图片进行描述？回答格式为:"天气；摄影类型；最多10个画面中的物品"'
                #'text': 'Answer format: "Weather, Photography Type, Less than 10 objects in the picture." You should describe the picture in my required format. Answer format: "Weather, Photography Type, Less than 10 objects in the picture."'
            },
        ]
    }]
    response = dashscope.MultiModalConversation.call(model='qwen-vl-plus', messages=messages)
    text_content = response['output']['choices'][0]['message']['content'][0]['text']
    print(text_content)
    return text_content