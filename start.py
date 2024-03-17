import os
base_path = './model'
# download repo to the base_path directory using git
os.system(f'git clone https://code.openxlab.org.cn/ustbzgn/model.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
os.system('streamlit run web_demo.py --server.address=0.0.0.0 --server.port 7860')
