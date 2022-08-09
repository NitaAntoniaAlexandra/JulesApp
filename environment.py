from browser import Browser
from pages.sign_in_page import Sign_in_page
from pages.forgot_password_page import Forgot_password_page
from pages.search_all_page import Search_all_page
from pages.menu_page import Menu_page
from pages.add_page import Add_page
from pages.add_property_page import Add_property_page


def before_all(context):
    context.browser = Browser()
    context.forgot_password_page = Forgot_password_page()
    context.sign_in_page = Sign_in_page()
    context.search_all_page = Search_all_page()
    context.menu_page = Menu_page()
    context.add_page = Add_page()
    context.add_property_page = Add_property_page()


def after_all(context):
    context.browser.close()

    # contextul este o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
    # before all = BDD
    # after all = BDD
    # de fiecare data cand adaugam o pagina noua in proiect o vom adauga in context/un obiect de tipul paginii noi
