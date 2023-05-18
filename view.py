from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore
from pystyle import Center, Colors, Colorate

def main():
	
	print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""
			  _____              _   _            _        __     __  _                                 
			 |_   _| __      __ (_) | |_    ___  | |__     \ \   / / (_)   ___  __      __   ___   _ __ 
			   | |   \ \ /\ / / | | | __|  / __| | '_ \     \ \ / /  | |  / _ \ \ \ /\ / /  / _ \ | '__|
			   | |    \ V  V /  | | | |_  | (__  | | | |     \ V /   | | |  __/  \ V  V /  |  __/ | |   
			   |_|     \_/\_/   |_|  \__|  \___| |_| |_|      \_/    |_|  \___|   \_/\_/    \___| |_|   
                                                                                         
            Improvements can be made to the code. If you're getting an error, visit my discord.
                                        Discord discord.gg/AFV9m8UXuT    
                                        Github  github.com/kichi779          
                       
                      
                      """)))

	twitch_username = input(Colorate.Vertical(Colors.green_to_blue, ("Enter your channel name:  ")))
	proxy_count = int(input(Colorate.Vertical(Colors.cyan_to_blue, ("How many proxy sites do you want to open? (Viewer to send): "))))

	chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
	driver_path = 'chromedriver.exe'

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_argument('--disable-logging')
	chrome_options.add_argument('--log-level=3')
	chrome_options.add_argument('--disable-extensions')
	chrome_options.add_argument('--headless')
	chrome_options.add_argument("--mute-audio")
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.binary_location = chrome_path
	driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)

	driver.get('https://www.blockaway.net')
	for i in range(proxy_count):
		try:
			driver.execute_script("window.open('https://www.blockaway.net')")
			driver.switch_to.window(driver.window_handles[-1])
			driver.get('https://www.blockaway.net')

			text_box = driver.find_element(By.ID, 'url')
			text_box.send_keys(f'www.twitch.tv/{twitch_username}')
			text_box.send_keys(Keys.RETURN)
		except Exception as e:
			print(f"Error al intentar utilizar el proxy {i+1}: {str(e)}")
			continue
		
	input(Colorate.Vertical(Colors.red_to_blue,("Viewers have all been sent. You can press enter to withdraw the views and the program will close..")))
	driver.quit()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print(Colorate.Vertical(Colors.orange, ("the script has been stopped")))
    
