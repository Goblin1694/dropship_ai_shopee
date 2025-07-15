from scraper import scrape_trending_products, save_to_csv
from uploader import upload_to_shopee_manual

def run():
    print("🔍 Scraping produk trending dari Shopee...")
    produk = scrape_trending_products("lampu tidur")
    save_to_csv(produk)
    print(f"✅ {len(produk)} produk disimpan di produk_terfilter.csv")

    print("📦 Upload ke Shopee dimulai (1 produk contoh)...")
    if produk:
        upload_to_shopee_manual(produk[0])
    else:
        print("❌ Tidak ada produk ditemukan.")

if __name__ == "__main__":
    run()
