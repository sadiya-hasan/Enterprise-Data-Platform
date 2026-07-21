"""
Project Configuration
---------------------
Stores all project paths and constants.
"""

from pathlib import Path

# =====================================================
# Project Root Directory
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =====================================================
# Data Directories
# =====================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DATA_DIR = DATA_DIR / "output"
ARCHIVE_DATA_DIR = DATA_DIR / "archive"

# Kaggle Dataset Folder
KAGGLE_DATA_DIR = RAW_DATA_DIR / "kaggle"

# =====================================================
# Dataset Files
# =====================================================

ORDERS_FILE = KAGGLE_DATA_DIR / "olist_orders_dataset.csv"
PROCESSED_ORDERS_PATH = (
    PROJECT_ROOT /
    "data" /
    "processed" /
    "orders_clean"
)
CUSTOMERS_FILE = KAGGLE_DATA_DIR / "olist_customers_dataset.csv"
PRODUCTS_FILE = KAGGLE_DATA_DIR / "olist_products_dataset.csv"
SELLERS_FILE = KAGGLE_DATA_DIR / "olist_sellers_dataset.csv"
ORDER_ITEMS_FILE = KAGGLE_DATA_DIR / "olist_order_items_dataset.csv"
PAYMENTS_FILE = KAGGLE_DATA_DIR / "olist_order_payments_dataset.csv"
REVIEWS_FILE = KAGGLE_DATA_DIR / "olist_order_reviews_dataset.csv"
GEOLOCATION_FILE = KAGGLE_DATA_DIR / "olist_geolocation_dataset.csv"
CATEGORY_TRANSLATION_FILE = (
    KAGGLE_DATA_DIR / "product_category_name_translation.csv"
)