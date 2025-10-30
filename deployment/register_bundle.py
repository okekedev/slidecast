#!/usr/bin/env python3
"""
Register Bundle ID for SlideCast

This script registers the bundle ID with Apple Developer Portal via API.
Run this before creating the app manually in App Store Connect.

Usage:
    python3 register_bundle.py
"""

import sys
import os

# Add parent directory to path so we can import deployment module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deployment.api import AppStoreAPI
from deployment.bundle import register_bundle_id
from deployment.config import BUNDLE_ID, APP_NAME


def main():
    print("=" * 60)
    print("🚀 SlideCast Bundle ID Registration")
    print("=" * 60)
    print(f"\nApp Name: {APP_NAME}")
    print(f"Bundle ID: {BUNDLE_ID}")
    print()

    try:
        # Initialize API client
        api = AppStoreAPI()
        print("✅ Connected to App Store Connect API")

        # Register bundle ID
        if register_bundle_id(api):
            print("\n" + "=" * 60)
            print("✅ SUCCESS!")
            print("=" * 60)
            print(f"\nBundle ID '{BUNDLE_ID}' is registered!")
            print("\n📝 NEXT STEPS:")
            print()
            print("1. Go to: https://appstoreconnect.apple.com")
            print("2. My Apps → + → New App")
            print(f"3. Name: {APP_NAME}")
            print(f"4. Bundle ID: {BUNDLE_ID} (select from dropdown)")
            print("5. SKU: slidecast-2025")
            print("6. Language: English")
            print("7. User Access: Full Access")
            print()
            print("Then you can configure screenshots, descriptions, etc.")
            print()
            return 0
        else:
            print("\n❌ FAILED - See errors above")
            return 1

    except FileNotFoundError as e:
        print("\n❌ ERROR: API key file not found")
        print("Make sure AuthKey_3M7GV93JWG.p8 is in the deployment/ folder")
        print(f"Details: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelled by user")
        sys.exit(1)
