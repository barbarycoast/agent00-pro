from feeds import dexscreener, pumpfun, safety
from strategy import scorer
from risk import manager
from exec import soldriver
from notify import telegram
def run_bot():
    market_data = dexscreener.get_market_data()
    tokens = pumpfun.get_new_tokens()
    for token in tokens:
        if safety.is_safe(token) and manager.check_risk():
            if scorer.score_token(token) > 80:
                soldriver.execute_trade(token, "BUY", 1)
                telegram.send_message(f"Bought {token}")
    print("Bot run complete.")
if __name__ == "__main__": run_bot()
