import flet as ft

def request_storage_permission(page):
    """طلب إذن الوصول إلى التخزين."""
    ph = ft.PermissionHandler()
    
    # تحقق من إذن التخزين
    if not ph.check_permission(ft.PermissionType.STORAGE):
        result = ph.request_permission(ft.PermissionType.STORAGE)
        if result:
            page.add(ft.Text("تم منح إذن الوصول إلى التخزين."))
        else:
            page.add(ft.Text("تم رفض إذن الوصول إلى التخزين."))
    else:
        page.add(ft.Text("إذن التخزين موجود بالفعل."))

def init_db():
    """تهيئة قاعدة البيانات."""
    # أضف هنا كود تهيئة قاعدة البيانات إذا لزم الأمر
    pass

def manage_client_storage(page, action, key, prefix=""):
    """إدارة تخزين بيانات العميل."""
    # قم بتعريف كيفية إدارة التخزين هنا
    if action == "get":
        # أعد قيمة للبحث الأخير كمثال
        return "example_search_query"
    return None

def add_navigation(page):
    """إضافة شريط تنقل."""
    # أضف هنا كود شريط التنقل
    return ft.NavigationBar(items=[])

def create_bottom_app_bar(page): 
    explore_button = ft.IconButton(
        icon=ft.icons.EXPLORE, 
        icon_color=ft.colors.WHITE,
        on_click=lambda e: navigate_to("explore", page)
    )
    
    folder_button = ft.IconButton(
        icon=ft.icons.FOLDER, 
        icon_color=ft.colors.WHITE,
        on_click=lambda e: navigate_to("folder", page)
    )
    
    bottom_app_bar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[explore_button, folder_button]
        ),
    )
    
    # احتفظ بالشريط السفلي في الصفحة
    page.bottom_app_bar = bottom_app_bar  
    page.add(bottom_app_bar)  # تأكد من إضافته إلى الصفحة


# استدعاء الدالة عند بدء التطبيق
def main(page: ft.Page):
    init_db()
    
    # طلب إذن التخزين عند بدء التطبيق
    request_storage_permission(page)
    
    last_search = manage_client_storage(page, "get", "last_search", prefix="my_app")
    if last_search:
        print(f"Last search query: {last_search}")

    page.nav_bar = add_navigation(page)  
    create_bottom_app_bar(page)

    page.update()

# تشغيل التطبيق
ft.app(target=main)
