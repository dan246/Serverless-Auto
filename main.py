import requests
import nuclio


def get_functions_list(nuclio_dashboard_url, port=8070):
    url = f"{nuclio_dashboard_url}:{port}/api/functions"
    params = {}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: Unable to fetch functions details. Status Code: {response.status_code}"


def get_project_list(nuclio_dashboard_url,port=8070):
    url = f"{nuclio_dashboard_url}:{port}/api/projects"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: Unable to fetch function details. Status Code: {response.status_code}"
    
def get_function_details(nuclio_dashboard_url, namespace, function_name,port=8070):
    # Nuclio 函數的 URL 組成
    url = f"{nuclio_dashboard_url}:{port}/api/functions/{function_name}?namespace={namespace}"

    # 發起 GET 請求
    response = requests.get(url)

    # 檢查響應狀態碼
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: Unable to fetch function details. Status Code: {response.status_code}"



def deploy_by_code_test(name,project,server,port=8070):
    # define my function code template
        code='''
def handler(context, event):
    return str("hello word")
        '''

        # substitute a string in the template 
        code = code.format('Hello World!')
        # define a file share (mount my shared fs home dir into the function /data dir)
        vol = nuclio.Volume('./','~/')
        spec = nuclio.ConfigSpec(env={'MYENV_VAR': 'something'}, mount=vol)
        addr = nuclio.deploy_code(code,name='myfunc',project='proj',verbose=True, spec=spec,dashboard_url=f'{server}:{port}')
        return addr[0].split(':')[1]
        


# 函數名稱和項目名稱
project_name = "testupload"
function_name = "nuclio"

# nuclio_dashboard_url = "http://url"
nuclio_dashboard_url = "http://localhost:8070"

# 建立新的 Nuclio 函數
function_port = deploy_by_code_test(project_name,function_name,nuclio_dashboard_url)
# 呼叫測試用的函數
resp = requests.get(f"{nuclio_dashboard_url}:{function_port}")
print(resp.text)

# 獲取項目列表
project_list = get_project_list(nuclio_dashboard_url)
functions = get_functions_list(nuclio_dashboard_url)
for key in functions:
    
    print(f'服務名稱：{key}，服務狀態：{functions[key]["status"]["state"]}')
    if functions[key]["status"]["state"] == 'ready':
        print(f"服務端口{functions[key]['status']['externalInvocationUrls']}")
    
