#!/usr/bin/env python3
"""
Upload Metadata for Slideshow Cast

This script uploads app metadata to App Store Connect via API.

Usage:
    python3 upload_metadata.py
"""

import sys
import os

# Add parent directory to path so we can import deployment module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deployment.api import AppStoreAPI
from deployment.bundle import get_app_id
from deployment.metadata import upload_metadata, upload_version_metadata
from deployment.config import BUNDLE_ID, APP_NAME


def main():
    print("=" * 60)
    print("🚀 Slideshow Cast Metadata Upload")
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
            print("Make sure you've created the app manually first.")
            return 1

        # Upload App Info metadata (name, subtitle, privacy URL)
        print("\n" + "=" * 60)
        print("📝 Uploading App Info Metadata")
        print("=" * 60)
        if not upload_metadata(api, app_id):
            print("⚠️  App info upload had issues")

        # Get the version ID (look for latest version in PREPARE_FOR_SUBMISSION)
        print("\n" + "=" * 60)
        print("🔍 Finding Latest Version")
        print("=" * 60)
        versions_result = api.get(f"apps/{app_id}/appStoreVersions?filter[appStoreState]=PREPARE_FOR_SUBMISSION")

        if versions_result.get("data") and len(versions_result["data"]) > 0:
            version_id = versions_result["data"][0]["id"]
            version_string = versions_result["data"][0]["attributes"]["versionString"]
            print(f"✅ Found version {version_string}")

            # Upload version-specific metadata (description, keywords, etc.)
            print("\n" + "=" * 60)
            print("📝 Uploading Version Metadata")
            print("=" * 60)
            if upload_version_metadata(api, version_id):
                print("\n" + "=" * 60)
                print("✅ SUCCESS!")
                print("=" * 60)
                print("\nMetadata uploaded successfully!")
                print("\n📝 NEXT STEPS:")
                print()
                print("1. Upload screenshots via App Store Connect or API")
                print("2. Configure App Privacy (no data collection)")
                print("3. Set Age Rating (4+)")
                print("4. Add App Review Information")
                print("5. Build and upload the app")
                print()
                print("Visit: https://appstoreconnect.apple.com")
                print()
                return 0
            else:
                print("\n⚠️  Version metadata upload had issues")
                return 1
        else:
            print("\n⚠️  No version found in PREPARE_FOR_SUBMISSION state")
            print("The app info metadata was uploaded successfully.")
            print("\nCreate a version in App Store Connect, then run this again to upload version metadata.")
            return 0

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
