#!/usr/bin/env python3
"""
Build and Upload Slideshow Cast to App Store Connect

This script builds the app and uploads it to App Store Connect.

Usage:
    python3 build_and_upload.py [version] [build_number]

Example:
    python3 build_and_upload.py 1.0 1
"""

import sys
import os

# Add parent directory to path so we can import deployment module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deployment.build import build_and_upload
from deployment.config import APP_NAME, BUNDLE_ID


def main():
    print("=" * 60)
    print("🚀 Slideshow Cast Build & Upload")
    print("=" * 60)
    print(f"\nApp Name: {APP_NAME}")
    print(f"Bundle ID: {BUNDLE_ID}")
    print()

    # Get version and build number
    if len(sys.argv) >= 3:
        version = sys.argv[1]
        build_number = sys.argv[2]
    else:
        version = input("Version number (e.g., 1.0): ").strip()
        build_number = input("Build number (e.g., 1): ").strip()

    if not version or not build_number:
        print("\n❌ Version and build number are required")
        return 1

    print(f"\n📦 Building version {version} (build {build_number})")
    print()

    try:
        if build_and_upload(version, build_number):
            print("\n" + "=" * 60)
            print("✅ SUCCESS!")
            print("=" * 60)
            print(f"\nBuild {version} ({build_number}) uploaded successfully!")
            print("\n📝 NEXT STEPS:")
            print()
            print("1. Wait 5-15 minutes for build to process in App Store Connect")
            print("2. Check: https://appstoreconnect.apple.com")
            print("3. Once processed, attach build to version 1.0")
            print("4. Complete remaining manual steps:")
            print("   - App Privacy (no data collection)")
            print("   - Age Rating (4+)")
            print("   - Create In-App Purchase subscription")
            print("   - Add App Review Information")
            print("5. Submit for review")
            print()
            return 0
        else:
            print("\n❌ Build or upload failed - see errors above")
            return 1

    except KeyboardInterrupt:
        print("\n\n⚠️  Build cancelled by user")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
