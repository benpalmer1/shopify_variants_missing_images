# Shopify Product Images & Variants with Missing Images

This script checks all products in a Shopify store for variants & products missing images. It prints out the total number of products, the number of products with more than one variant, and the number of variants missing images, along with the product name and variant title for each variant without an associated image that belongs to a product with more than one variant.

## Prerequisites

- Python 3 installed on your machine
- Shopify Python API library. Install it using pip:

```bash
pip install --upgrade ShopifyAPI
```

- A Shopify store with products

## Getting Started

To use the script, you need to generate an API key and an Admin API access token from your Shopify store. (as at July 2023)

Follow these steps:

1. Go to your Shopify admin panel.
2. Navigate to "Settings" -> "Apps and sales channels".
3. Click on "Develop Apps".
4. Click on "Create a new app".
5. Fill in the necessary details for your app.
6. Under the "Admin API Permissions" section, add "Read Products" permissions.
7. Save your app.

After saving, you'll be provided with an API key and an Admin API access token.

## Configuring the Script

1. Open the Python script in your preferred text editor.
2. Find these lines in the script:

```python
include_single_variant_products = True  # Change to True if you want to include products with only one variant
shopify.ShopifyResource.set_user("API key goes here")
shopify.ShopifyResource.set_password("Admin API access token goes here")
shopify.ShopifyResource.set_site("https://Store_Name_Here.myshopify.com/admin/api/2021-10")
```

3. Replace the arguments of `set_user`, `set_password`, `set_site` with your API key, Admin API access token and Shopify site name "Store_Name_Here" respectively. Change "include_single_variant_products" to True if you want to include products with only one variant
4. Save the script.

## Running the Script

Open a terminal and navigate to the location of the script. Run the script using Python:

```bash
python variants_missing_images.py
```

The script will now check your Shopify store's products and print out the required information.

---
