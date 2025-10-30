//
//  PaywallView.swift
//  SlideCast
//
//  Pro subscription paywall
//

import SwiftUI
import StoreKit

struct PaywallView: View {
    @EnvironmentObject var storeManager: StoreManager
    @Environment(\.dismiss) var dismiss

    var body: some View {
        ZStack {
            // Gradient background
            LinearGradient(
                gradient: Gradient(colors: [
                    Color.blue,
                    Color.cyan
                ]),
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
            .ignoresSafeArea()

            ScrollView {
                VStack(spacing: 30) {
                    Spacer().frame(height: 20)

                    // App Icon/Logo
                    ZStack {
                        Circle()
                            .fill(Color.white)
                            .frame(width: 100, height: 100)
                            .shadow(radius: 10)

                        Image(systemName: "tv")
                            .font(.system(size: 50))
                            .foregroundColor(.blue)
                    }

                    // Title
                    VStack(spacing: 12) {
                        Text("Unlock Pro Features")
                            .font(.system(size: 32, weight: .bold))
                            .foregroundColor(.white)

                        Text("Create unlimited slideshows")
                            .font(.system(size: 18))
                            .foregroundColor(.white.opacity(0.9))
                    }

                    // Feature list
                    VStack(alignment: .leading, spacing: 20) {
                        FeatureRow(icon: "infinity", title: "Unlimited Photos", description: "Create slideshows with as many photos as you want")
                        FeatureRow(icon: "rectangle.landscape.rotate", title: "Portrait & Landscape", description: "Choose your preferred video orientation")
                        FeatureRow(icon: "timer", title: "Custom Photo Duration", description: "Set how long each photo displays (3-10 seconds)")
                        FeatureRow(icon: "repeat", title: "Loop Settings", description: "Create extended videos for continuous playback")
                    }
                    .padding(.horizontal, 40)
                    .padding(.vertical, 30)
                    .background(Color.white.opacity(0.15))
                    .cornerRadius(20)
                    .padding(.horizontal, 30)

                    // Pricing
                    VStack(spacing: 12) {
                        Text("7-Day Free Trial")
                            .font(.system(size: 24, weight: .bold))
                            .foregroundColor(.white)

                        Text("Then $2.99/month")
                            .font(.system(size: 18))
                            .foregroundColor(.white.opacity(0.9))

                        Text("Cancel anytime • Family Sharing")
                            .font(.system(size: 14))
                            .foregroundColor(.white.opacity(0.7))
                    }

                    // Subscribe button
                    if let product = storeManager.products.first {
                        Button(action: {
                            Task {
                                do {
                                    let success = try await storeManager.purchase(product)
                                    if success {
                                        dismiss()
                                    }
                                } catch {
                                    print("❌ Purchase error: \(error)")
                                }
                            }
                        }) {
                            Group {
                                if storeManager.isLoading {
                                    ProgressView()
                                        .progressViewStyle(CircularProgressViewStyle(tint: .blue))
                                } else {
                                    Text("Start Free Trial")
                                        .font(.system(size: 20, weight: .bold))
                                }
                            }
                            .foregroundColor(.blue)
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 18)
                            .background(Color.white)
                            .cornerRadius(14)
                        }
                        .padding(.horizontal, 30)
                        .disabled(storeManager.isLoading)
                    } else {
                        ProgressView()
                            .progressViewStyle(CircularProgressViewStyle(tint: .white))
                    }

                    // Restore button
                    Button(action: {
                        Task {
                            await storeManager.restorePurchases()
                            if storeManager.isPro {
                                dismiss()
                            }
                        }
                    }) {
                        Text("Restore Purchases")
                            .font(.system(size: 16))
                            .foregroundColor(.white.opacity(0.8))
                    }
                    .disabled(storeManager.isLoading)

                    Spacer().frame(height: 30)

                    // Privacy and Terms links
                    HStack(spacing: 20) {
                        Link("Privacy Policy", destination: URL(string: "https://yourwebsite.com/privacy")!)
                            .font(.system(size: 12))
                            .foregroundColor(.white.opacity(0.6))

                        Text("•")
                            .foregroundColor(.white.opacity(0.4))

                        Link("Terms of Use", destination: URL(string: "https://yourwebsite.com/terms")!)
                            .font(.system(size: 12))
                            .foregroundColor(.white.opacity(0.6))
                    }

                    // Close button
                    Button(action: {
                        dismiss()
                    }) {
                        Text("Continue with Free Version")
                            .font(.system(size: 14))
                            .foregroundColor(.white.opacity(0.6))
                    }
                    .padding(.bottom, 40)
                }
                .padding(.horizontal, 0)
            }
        }
    }
}

// MARK: - Feature Row
struct FeatureRow: View {
    let icon: String
    let title: String
    let description: String

    var body: some View {
        HStack(spacing: 16) {
            Image(systemName: icon)
                .font(.system(size: 24))
                .foregroundColor(.white)
                .frame(width: 40)

            VStack(alignment: .leading, spacing: 4) {
                Text(title)
                    .font(.system(size: 18, weight: .semibold))
                    .foregroundColor(.white)

                Text(description)
                    .font(.system(size: 14))
                    .foregroundColor(.white.opacity(0.8))
            }

            Spacer()
        }
    }
}
