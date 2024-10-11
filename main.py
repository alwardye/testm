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
ft.app(main)
