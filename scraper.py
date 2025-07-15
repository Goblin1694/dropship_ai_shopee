from playwright.sync_api import sync_playwright

MAX_PRICE = 150000
TARGET_PROFIT = 2000

def scrape_trending_products(keyword="lampu tidur", max_price=MAX_PRICE, max_items=20):
    result = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://shopee.co.id/search?keyword={keyword.replace(' ', '%20')}", timeout=60000)
        page.wait_for_selector("div.shopee-search-item-result__item")

        items = page.query_selector_all("div.shopee-search-item-result__item")[:max_items]
        for item in items:
            try:
                name = item.query_selector("div[data-sqe='name']").inner_text()
                price_text = item.query_selector("span[data-sqe='price']").inner_text()
                price = int(price_text.replace('.', '').replace('Rp', '').split(" ")[0])

                if price <= max_price:
                    result.append({
                        "name": name,
                        "price": price,
                        "selling_price": price + TARGET_PROFIT
                    })
            except:
                continue

        browser.close()

    return result


def save_to_csv(data, filename="produk_terfilter.csv"):
    import csv
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price", "selling_price"])
        writer.writeheader()
        writer.writerows(data)
