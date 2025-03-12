from src.auth_manager import AuthManager
from src.data_fetcher import fetch_employee_data, fetch_sales_data
from src.profit_calculator import ProfitCalculator
from src.notifier import Notifier
from src.utils import log_info

def main():
    log_info("📢 システム起動...")

    # トークン取得
    auth_manager = AuthManager()
    access_token = auth_manager.get_access_token()

    # データ取得
    employee_data = fetch_employee_data(access_token)
    sales_data = fetch_sales_data(access_token)

    # 損益計算
    profit_calculator = ProfitCalculator()
    profit_report = profit_calculator.calculate_profit(employee_data, sales_data)

    # 通知
    notifier = Notifier()
    notifier.send_line_message(profit_report)

    log_info("✅ 完了！")

if __name__ == "__main__":
    main()
