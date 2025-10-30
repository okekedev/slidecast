#!/usr/bin/env python3
"""
Upload Screenshots for Slideshow Cast

This script uploads screenshots to App Store Connect via API.

Usage:
    python3 upload_screenshots.py
"""

import sys
import os

# Add parent directory to path so we can import deployment module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deployment.api import AppStoreAPI
from deployment.bundle import get_app_id
from deployment.screenshots import upload_screenshots
from deployment.config import BUNDLE_ID, APP_NAME


def main():
    print("=" * 60)
    print("🚀 Slideshow Cast Screenshot Upload")
    print("=" * 60)
    print(f"\nApp Name: {APP_NAME}")
    print(f"Bundle ID: {BUNDLE_ID}")
    print()

    try:
        # Initialize API client
        api = AppStoreAPI()
        print("✅ Connected to App Store Connect API")

        # Get App ID
        app_id = get_app_id(api)
        if not app_id:
            print("\n❌ App not found in App Store Connect")
            return 1

        # Get the version ID (look for latest version in PREPARE_FOR_SUBMISSION)
        print("\n" + "=" * 60)
        print("🔍 Finding Latest Version")
        print("=" * 60)
        versions_result = api.get(f"apps/{app_id}/appStoreVersions?filter[appStoreState]=PREPARE_FOR_SUBMISSION&filter[platform]=IOS")

        if not versions_result.get("data") or len(versions_result["data"]) == 0:
            print("\n❌ No iOS version found in PREPARE_FOR_SUBMISSION state")
            print("Create a version in App Store Connect first.")
            return 1

        version_id = versions_result["data"][0]["id"]
        version_string = versions_result["data"][0]["attributes"]["versionString"]
        print(f"✅ Found version {version_string}")

        # Upload screenshots
        print("\n" + "=" * 60)
        print("📸 Uploading Screenshots")
        print("=" * 60)

        if upload_screenshots(api, version_id):
            print("\n" + "=" * 60)
            print("✅ SUCCESS!")
            print("=" * 60)
            print("\nScreenshots uploaded successfully!")
            print("\n📝 NEXT STEPS:")
            print()
            print("1. Review screenshots in App Store Connect")
            print("2. Configure App Privacy (no data collection)")
            print("3. Set Age Rating (4+)")
            print("4. Add App Review Information")
            print("5. Build and upload the app")
            print()
            print("Visit: https://appstoreconnect.apple.com")
            print()
            return 0
        else:
            print("\n⚠️  Screenshot upload had issues")
            return 1

    except FileNotFoundError as e:
        print("\n❌ ERROR: File not found")
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
