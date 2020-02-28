<h1 align="center">2019-CCF-BDCI-Car-Sales-Forecast-Top3-Solution</h1>

### 运行环境
- tensorflow-1.12.0
- python3.6

### 代码说明
- 目录结构：
	- chusai:       		# 初赛相关
		- data     			# 存放初赛数据集
		- model   			# 用于保存代码运行过程中生成的模型
		- submit			# 保存所有模型的预测结果以及融合结果
		- fusion.ipynb		# 模型融合代码
		- LGB_Model_1.ipynb	# 初赛-机器学习方案一代码
		- LGB_Model_2.ipynb	# 初赛-机器学习方案二代码
		- LGB_Model_3.ipynb	# 初赛-机器学习方案三代码
		- LSTM_Model_1.ipynb	# 初赛-深度学习方案一代码
		- LSTM_Model_2.ipynb	# 初赛-深度学习方案二代码
		- Rule_Model.ipynb		# 初赛-规则+机器学习模型方案代码

	- fusai:				# 复赛相关
		- data				# 存放复赛数据集
		- model			# 用于保存代码运行过程中生成的模型
		- submit			# 保存所有模型的预测结果以及融合结果
		- fusion.ipynb		# 模型融合代码
		- LGB_Model_1.ipynb	# 复赛-机器学习方案一代码
		- LGB_Model_2.ipynb	# 复赛-机器学习方案二代码
		- LGB_Model_3.ipynb	# 复赛-机器学习方案三代码
		- LSTM_Model_1.ipynb	# 复赛-深度学习方案一代码
		- LSTM_Model_2.ipynb	# 复赛-深度学习方案二代码

### 复现方案
- shift+鼠标右键进入命令行界面，使用命令【jupyter notebook】启动notebook，所有【. ipynb】文件里面的cell都是从上到下依次运行。
- 代码执行顺序(上一个运行完再运行下一个)
1. Cars/chusai/ LGB_Model_1.ipynb
2. Cars/chusai/ LGB_Model_2.ipynb
3. Cars/chusai/ LGB_Model_3.ipynb
4. Cars/chusai/ LSTM_Model_1.ipynb & LSTM_Model_1.ipynb   # 同时运行
5. Rule_Model.ipynb
6. fusion.ipynb
7. Cars/fusai/ LGB_Model_1.ipynb
8. Cars/fusai/ LGB_Model_2.ipynb
9. Cars/fusai/ LGB_Model_3.ipynb
10. Cars/fusai/ LSTM_Model_1.ipynb & LSTM_Model_2.ipynb	# 同时运行
11. Cars/fusai/ fusion.ipynb

### 总结
https://blog.csdn.net/roger_royer/article/details/104550765
