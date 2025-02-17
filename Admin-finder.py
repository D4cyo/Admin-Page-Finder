from requests import get
from colorama import Fore
import os

def clear():
    if system == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
      
# !!ADMIN PAGE FINDER | by D4cyo And L4nd0 | dont delete this text!!

print(Fore.BLUE + """
____ ___  _  _ _ _  _  ___  ____ ____ ____  ____ _ _  _ ___  ____ ____ 
|__| |  \ |\/| | |\ |  |__] |__| | __ |___  |___ | |\ | |  \ |___ |__/ 
|  | |__/ |  | | | \|  |    |  | |__] |___  |    | | \| |__/ |___ |  \ 

By : D4cyo                                                                     
                                                                                                """)



def admin_page_finder(url):
    common_paths = [
        "/admin",
        "/administrator",
        "/wp-admin",
        "/login",
        "/cp"  
    ]
    less_common_paths = [
        "/admin/login",
        "/admin/index",
        "/wp-login.php",
        "/admin.php",
        "/adminpanel",
        "/panel-administracion"
        "/admin/",
        "/administrator/",
        "/admin1/",
        "/admin2/",
        "/admin3/",
        "/admin4/",
        "/admin5/",
        "/usuarios/",
        "/usuario/",
        "/administrator/",
        "/moderator/",
        "/webadmin/",
        "/adminarea/",
        "/bb-admin/",
        "/adminLogin/",
        "/admin_area/",
        "/panel-administracion/",
        "/instadmin/",
        "/memberadmin/",
        "/administratorlogin/",
        "/adm/",
        "/admin/account.php",
        "/admin/index.php",
        "/admin/login.php",
        "/admin/admin.php",
        "/admin/account.php",
        "/admin_area/admin.php",
        "/admin_area/login.php",
        "/siteadmin/login.php",
        "/siteadmin/index.php",
        "/siteadmin/login.html",
        "/admin/account.html",
        "/admin/login.html",
        "/admin/admin.html",
        "/admin_area/index.php",
        "/bb-admin/index.php",
        "/bb-admin/login.php",
        "/bb-admin/admin.php",
        "/admin/home.php",
        "/admin/controlpanel.php",
        "/admin.php",
        "/admincp/index.asp",
        "/admincp/login.asp",
        "/admincp/index.html",
        "/admin/account.html",
        "/adminpanel.html",
        "/webadmin.html",
        "/webadmin/index.html",
        "/webadmin/admin.html",
        "/webadmin/login.html",
        "/admin/admin_login.html",
        "/admin_login.html",
        "/panel-administracion/login.html",
        "/admin/cp.php",
        "/cp.php",
        "/administrator/index.php",
        "/administrator/login.php",
        "/nsw/admin/login.php",
        "/webadmin/login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/bb-admin/index.html",
        "/bb-admin/login.html",
        "/bb-admin/admin.html",
        "/admin/home.html",
        "/login.php",
        "/modelsearch/login.php",
        "/moderator.php",
        "/moderator/login.php",
        "/moderator/admin.php",
        "/account.php",
        "/pages/admin/admin-login.html",
        "/admin/admin-login.html",
        "/admin-login.html",
        "/controlpanel.php",
        "/admincontrol.php",
        "/admin/adminLogin.html",
        "/adminLogin.html",
        "/admin/adminLogin.html",
        "/home.html",
        "/rcjakar/admin/login.php",
        "/adminarea/index.html",
        "/adminarea/admin.html",
        "/webadmin.php",
        "/webadmin/index.php",
        "/webadmin/admin.php",
        "/admin/controlpanel.html",
        "/admin.html",
        "/admin/cp.html",
        "/cp.html",
        "/adminpanel.php",
        "/moderator.html",
        "/administrator/index.html",
        "/administrator/login.html",
        "/user.html",
        "/administrator/account.html",
        "/administrator.html",
        "/login.html",
        "/modelsearch/login.html",
        "/moderator/login.html",
        "/adminarea/login.html",
        "/panel-administracion/index.html",
        "/panel-administracion/admin.html",
        "/modelsearch/index.html",
        "/modelsearch/admin.html",
        "/admincontrol/login.html",
        "/adm/index.html",
        "/adm.html",
        "/moderator/admin.html",
        "/user.php",
        "/account.html",
        "/controlpanel.html",
        "/admincontrol.html",
        "/panel-administracion/login.php",
        "/wp-login.php",
        "/adminLogin.php",
        "/admin/admin_login.php",
        "/admin/adminLogin.php",
        "/home.php",
        "/adminarea/index.php",
        "/adminarea/admin.php",
        "/adminarea/login.php",
        "/panel-administracion/index.php",
        "/panel-administracion/admin.php",
        "/modelsearch/index.php",
        "/modelsearch/admin.php",
        "/admincontrol/login.php",
        "/adm/admloginuser.php",
        "/admloginuser.php",
        "/admin2/login.php",
        "/admin2/index.php",
        "/admin2/index.html",
        "/yonetim.php",
        "/yonetim.html",
        "/yonetici.php",
        "/yonetici.html",
        "/admin/controlpanel.php",
        "/admin.php",
        "/admin/cp.php",
        "/cp.php",
        "/administrator/index.php",
        "/administrator/login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/admin/admin_login.php",
        "/admin_login.php",
        "/administrator/account.php"        
    ]

    for path in common_paths + less_common_paths:
        admin_url = url + path
        try:
            response = get(admin_url)
            if response.status_code == 200:
                print(Fore.LIGHTYELLOW_EX + f"[+] Potential Admin page found: {admin_url}")
            elif response.status_code == 403:
                print(Fore.RED + f"[!] Access forbidden: {admin_url}")
            elif response.status_code == 404:
                print(Fore.RED + f"[-] Page not found: {admin_url}")
            else:
                print(Fore.MAGENTA + f"[~] Interesting status code: {response.status_code} for {admin_url}")
        except requests.exceptions.RequestException:
            print(Fore.RED + f"[*] Connection error for URL: {admin_url}")


if __name__ == "__main__":
    while True:
        target_url = input(Fore.LIGHTYELLOW_EX + "Enter the target URL (or 'q' to quit): ")
        if target_url.lower() == 'q':
            break
        if not target_url.startswith("http"):
            print(Fore.RED + "Invalid URL format. Please start with http:// or https://")
            continue
        admin_page_finder(target_url)
