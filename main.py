from src.data_fetcher import DataFetcher
from src.profit_calculator import ProfitCalculator
from src.notifier import Notifier
from src.utils import log_info, log_error

def main():
    """メイン処理: データ取得 -> 損益計算 -> 通知"""
    log_info(" 出雲インサイト: システム起動")
    
    try:
        # インスタンス生成
        data_fetcher = DataFetcher()
        profit_calculator = ProfitCalculator()
        notifier = Notifier()
        
        # データ取得
        attendance_data = data_fetcher.get_attendance_data()
        sales_data = data_fetcher.get_sales_data()
        
        if not attendance_data or not sales_data:
            log_error(" データ取得に失敗しました")
            return
        
        # 損益計算
        profit_report = profit_calculator.calculate_profit(
            sales_data.get("payments", []), 
            attendance_data.get("timesheets", [])
        )
        
        # 赤字の場合の警告
        if profit_report["operating_profit"] < 0:
            log_error(" 営業利益がマイナスです！")

        # 結果を整形
        message = (
            "📊 出雲インサイト: 損益レポート\n"
            f"💰 売上総額: {profit_report['total_revenue']} 円\n"
            f"👥 給与総額: {profit_report['total_salary']} 円\n"
            f"📉 売上原価: {profit_report['cost_of_goods_sold']} 円\n"
            f"🏆 営業利益: {profit_report['operating_profit']} 円\n"
        )
        
        # 通知送信
        notifier.send_slack_notification(message)
        notifier.send_line_notification(message)
        
        log_info("✅ 損益レポートを通知しました")

    except Exception as e:
        log_error(f" システムエラー発生: {str(e)}")

if __name__ == "__main__":
    main()
