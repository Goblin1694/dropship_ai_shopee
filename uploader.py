from playwright.sync_api import sync_playwright
import time

def upload_to_shopee_manual(product):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://seller.shopee.co.id/", timeout=60000)
        print("Login secara manual dalam 30 detik...")
        page.wait_for_timeout(30000)

        page.goto("https://seller.shopee.co.id/portal/product/new")

        page.fill("input[name='name']", product['name'])
        page.fill("input[name='price']", str(product['selling_price']))
        print("Produk berhasil diisi (simulasi).")
        time.sleep(5)
        browser.close()
