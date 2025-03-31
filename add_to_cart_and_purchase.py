from colorama import init, Fore, Back, Style
import numpy as np
from sklearn.model_selection import train_test_split as TTP
from sklearn.linear_model import LogisticRegression as lg

modle = lg()

x = np.array([[25,30,0],
             [30,40,1],
             [20,25,0],
             [35,45,11]]) # age, time, ad to cart yes or no 0,1== on no, 1= yes
y =  np.array([0,1,0,1])

x_train,x_test, y_train, y_test = TTP(x,y, test_size = 0.2, random_state = 42)

modle.fit(x_train, y_train)

accuracy = modle.score(x_test, y_test)
print(accuracy)

user_age = float(input(f"{Fore.GREEN}Enter customer age: {Fore.RESET}"))
use_time_spend = float(input(f"{Fore.CYAN}Enter customer spend in youe website: {Fore.RESET}"))
user_add_to_art = float(input(f"{Fore.BLUE}Enter 1 if user add to cart: else: Enter 0 else user fif not add to cart: {Fore.RESET}"))
if user_add_to_art > 1:
    print("Enter only 0 or 1")
else:
    user_data = np.array([[user_age, use_time_spend, user_add_to_art]])

    precidtion = modle.predict(user_data)
    if precidtion[0] == 1:
        print(f"{Fore.GREEN}Ther customer likely to purchase{Fore.RESET}")
    else:
        print(f"{Fore.RED}The user unlikely to purchase{Fore.RESET}")