import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# ========== 币安 API 配置 ========== 
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY', '')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET', '')

# ========== 监控参数配置 ========== 
# 检查间隔（秒）
CHECK_INTERVAL = 300  # 5分钟

# 价格上升阈值（百分比）
PRICE_INCREASE_THRESHOLD = 5.0  # 5%

# 回看日线根数（用最高价比对）
LOOKBACK_CANDLES = 3  # 前三根线

# 最小 24h 交易额（USDT），用于过滤冷币
MIN_24H_VOLUME = 100000  # 100k USDT

# ========== 日志配置 ========== 
LOG_FILE = 'monitor.log'
LOG_LEVEL = 'INFO'

# ========== 合约类型配置 ========== 
# 监控的合约类型：USDT永续合约
CONTRACT_TYPE = 'PERPETUAL'
# 交易对基础币种
QUOTE_ASSET = 'USDT'