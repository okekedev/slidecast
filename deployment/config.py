"""Configuration for App Store Connect API"""

# API Credentials
KEY_ID = "3M7GV93JWG"
ISSUER_ID = "196f43aa-4520-4178-a7df-68db3cf7ee76"
KEY_FILE = "deployment/AuthKey_3M7GV93JWG.p8"

# App Configuration
BUNDLE_ID = "com.christianokeke.slidecast"
APP_NAME = "SlideCast"
SKU = "slidecast"
TEAM_ID = "TUG3BHLSM4"

# API Base URL
BASE_URL = "https://api.appstoreconnect.apple.com/v1"

# Build Configuration
XCODE_SCHEME = "MemorySlideshow"
ARCHIVE_PATH = "build/SlideCast.xcarchive"
EXPORT_PATH = "build"
IPA_NAME = "MemorySlideshow.ipa"
EXPORT_OPTIONS = "deployment/ExportOptions.plist"
