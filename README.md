# KCL-Computational-Finance-Projects-HFF
tick data management (MySQL) and algorithmic FX trading strategy based on the Intrinsic Time framework.

## 🚀 Core Features | 核心功能

### 1. Financial Data Engineering | 金融数据工程
* Built a Python-to-MySQL pipeline to safely ingest, query, and clean over **270,000 lines of tick data**. Enforced rigid SQL schemas to prevent dirty data from corrupting the quantitative models.
* 搭建 Python 至 MySQL 的自动化数据管道，安全摄取、清洗并查询超 **27 万条高频订单数据**。利用严格的 SQL 表结构阻断脏数据，确保底层量化模型的纯净度。

### 2. Intrinsic Time Strategy | 内在时间交易策略
* Designed an FX (EUR/USD) trading algorithm that captures market momentum through "Overshoot" events following Directional Changes (DC).
* 针对外汇市场 (EUR/USD)，利用方向性变化 (DC) 后的“价格动量 (Overshoot)”特征，开发了不依赖固定时间频率的算法交易策略。

### 3. Advanced Risk Exposure Control | 高级风险敞口控制
* Implemented strict dynamic stop-loss and take-profit mechanisms. Introduced a **"Maximum Time Window"** exit rule to automatically cut off risk exposure during low-volatility, sideways market regimes in later strategy.
* 部署严格的动态止损与止盈平仓机制。发现回测中发现的痛点，反思认为以后可以引入**“最大时间窗口”**强制退出规则，在低波动震荡市中自动切断风险敞口。

## 🛠 Tech Stack | 技术栈
* **Languages:** Python, SQL
* **Database:** MySQL
