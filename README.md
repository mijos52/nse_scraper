# nse_scraper
--get stock information from nse indiatimes  website
--Look for stocks that are in play.
--faster variation of google finance based scanner

# 14/10/2021
-- found the api url from website
-- extracted changepct, volume , ticker , current price from dictionary

# 15/10/2021
-- Google sheets Api integration 
-- An executable was also built(using pyinstaller), and it works
-- All other values in sheets was also added 
-- project complete 
-- require code clean up and updates

# 16/10/2021
-- Added time based update (code refreshes automatically)
-- Entire main.py was made into a def main()
-- 3 variables are now being accepted as user inputs (page_size , min_price , max_price)(This was changed back)
-- Capital letters in functions names were removed (snake_case or smaller case used)
-- error handling using try and except (network error ,network reset error )
-- added more print statements for more code clarity during runtime (url fetch , prep data , upload )

# 23/4/2021
#TODO
-- get all nifty stocks 
-- make android executable script

# 25/4/2022

-- significant changes were mad
-- design was changed
-- api was changed 
-- variable names were changed

# 26/4/20222

-- variable (item_no) was added to remove error
-- page size is calculated from response url list item count
-- added new def delete_data to in sheets_auth for clearning sheets data
-- new nifty 500 filter added 

# 29/4/200
-- premarket scanner form nse india website added
-- new pre_market.py file