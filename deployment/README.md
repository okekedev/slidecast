# SlideCast Deployment

## Bundle ID Registration (Completed ✅)

The bundle ID `com.christianokeke.slidecast` has been successfully registered with Apple Developer Portal.

## Next Steps

### 1. Create App in App Store Connect (Manual)

Go to [App Store Connect](https://appstoreconnect.apple.com) and create the app:

1. My Apps → + → New App
2. **Name:** SlideCast
3. **Bundle ID:** com.christianokeke.slidecast (select from dropdown)
4. **SKU:** slidecast-2025
5. **Language:** English
6. **User Access:** Full Access

### 2. Configure In-App Purchase Subscription

Create the subscription product:

1. Go to your app → In-App Purchases
2. Create new subscription
3. **Product ID:** com.christianokeke.slidecast.pro.monthly
4. **Type:** Auto-renewable subscription
5. **Duration:** 1 month
6. **Price:** $2.99/month
7. **Free trial:** 7 days
8. **Family Sharing:** Enabled

### 3. Upload Screenshots

Use screenshots from `/Assests/` folder:
- iPhone 11 Pro Max (6.5" - 1242 x 2688)
- Optional: iPad screenshots

### 4. App Information

- **Category:** Photo & Video
- **Age Rating:** 4+
- **Privacy:** No data collection

## Files in This Folder

- `config.py` - App configuration
- `api.py` - App Store Connect API client
- `bundle.py` - Bundle ID registration
- `register_bundle.py` - Registration script (already run)
- `AuthKey_3M7GV93JWG.p8` - API authentication key

## API Credentials

- **Key ID:** 3M7GV93JWG
- **Issuer ID:** 196f43aa-4520-4178-a7df-68db3cf7ee76
- **Team ID:** TUG3BHLSM4
