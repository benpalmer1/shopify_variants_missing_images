# Import the Shopify API library
import shopify

# Toggle for including products with only one variant in the search
include_single_variant_products = False  # Change to True if you want to include products with only one variant

# Initialize the Shopify API with your credentials
shopify.ShopifyResource.set_user("API key goes here") #API key
shopify.ShopifyResource.set_password("Admin API access token goes here") #Admin API access token (not the secret key)
shopify.ShopifyResource.set_site("https://Store_Name_Here.myshopify.com/admin/api/2021-10")

# Counter for products with more than one variant
multi_variant_products = 0

# Counter for variants missing images
variants_missing_images = 0

# Pagination: Initialize empty list for all products
all_products = []

# Pagination: Loop through all pages of products
page_info = None
while True:
    if page_info:
        products = shopify.Product.find(limit=250, page_info=page_info)
    else:
        products = shopify.Product.find(limit=250)

    all_products.extend(products)
    
    # Break the loop if we are on the last page
    if not products.has_next_page():
        break

    # Get the next page info
    page_info = products.next_page_info

# Loop through each product
for product in all_products:
  # Get the variants of the product
  variants = product.variants

  # If not including single variant products, skip products with only one variant
  if not include_single_variant_products and len(variants) <= 1:
    continue

  # Increment counter for products with more than one variant
  if len(variants) > 1:
    multi_variant_products += 1

  # Get the images of the product
  images = product.images

  # Loop through each variant
  for variant in variants:
    # Get the image ids associated with the variant
    variant_image_ids = [image.id for image in images if variant.id in image.variant_ids]

    # Check if the variant has any associated images
    if not variant_image_ids:
      # Increment counter for variants missing images
      variants_missing_images += 1
      # Print the product name and variant title that has a missing image
      print(f"Product Name: {product.title}, Variant Title: {variant.title}")

# Print the total number of products
print(f"\nTotal Number of Products: {len(all_products)}")

# Print the number of products with more than one variant
print(f"Number of Products with More Than One Variant: {multi_variant_products}")

# Print the number of variants missing images
print(f"Number of Variants Missing Images: {variants_missing_images}\n")
