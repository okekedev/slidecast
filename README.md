# Memory Slideshow

A native iOS app that creates photo/video slideshows with optional intro text, saves them to Camera Roll, and supports AirPlay.

## Features

- **Easy Media Selection**: Multi-select photos and videos from your library
- **Optional Intro**: Add custom intro text (up to 100 characters)
- **Flexible Photo Duration**: Choose 3-10 seconds per photo
- **Video Support**: Videos play at their original length with audio
- **Loop Options**: No loop, 1 hour, 2 hours, or 4 hours
- **High Quality Export**: 1920x1080 HD output at 30fps
- **Simple Transitions**: Smooth crossfade between items
- **Save to Photos**: Automatic save to Camera Roll
- **Share & AirPlay**: Share via standard iOS share sheet or AirPlay from Photos app

## Requirements

- iOS 15.0 or later
- Xcode 15.0 or later
- Physical iOS device (Simulator has limited photo library access)

## Setup Instructions

1. **Open in Xcode**:
   ```bash
   cd MemorySlideshow
   open MemorySlideshow.xcodeproj
   ```

2. **Configure Signing**:
   - Select the project in Xcode
   - Go to "Signing & Capabilities"
   - Select your development team
   - Change the bundle identifier if needed (e.g., `com.yourname.MemorySlideshow`)

3. **Build and Run**:
   - Connect your iOS device
   - Select your device from the scheme picker
   - Press Cmd+R to build and run

## Usage

1. **Select Media**:
   - Tap "Select Photos & Videos"
   - Choose photos and videos from your library
   - Tap "Next" when done

2. **Configure Settings**:
   - Add optional intro text (appears for 4 seconds)
   - Adjust photo duration (3-10 seconds)
   - Choose loop duration
   - Review total slideshow length

3. **Create Video**:
   - Tap "Create Video"
   - Wait for processing (progress shown)
   - Video automatically saves to Photos

4. **Share & Play**:
   - Use share button to send via Messages, Email, etc.
   - Open Photos app to AirPlay to TV
   - Create another slideshow or close the app

## Technical Details

### Video Specifications
- **Resolution**: 1920x1080 (Full HD)
- **Frame Rate**: 30fps
- **Codec**: H.264 (MP4)
- **Transitions**: 0.5s crossfade
- **Audio**: Preserved from original videos

### Permissions Required
- **Photo Library (Read)**: To select photos and videos
- **Photo Library (Write)**: To save created slideshow

### Performance Notes
- Large videos (>5 minutes) will show a warning
- 100+ items will show a processing time warning
- Looped videos result in larger file sizes
- Processing happens on background thread

## Project Structure

```
MemorySlideshow/
├── MemorySlideshowApp.swift    # App entry point
├── ContentView.swift            # Navigation coordinator
├── Models.swift                 # Data models
├── MediaSelectionView.swift     # Photo/video picker screen
├── SettingsView.swift           # Configuration screen
├── VideoComposer.swift          # Core video composition logic
├── VideoCreationView.swift      # Progress display
├── CompletionView.swift         # Success screen with share
├── Info.plist                   # App permissions
└── Assets.xcassets              # App assets
```

## How It Works

1. **Media Selection**: Uses `PHPickerViewController` for native photo/video selection
2. **Composition**: Builds video using `AVFoundation`:
   - Creates intro slide from text (if provided)
   - Adds photos at specified duration
   - Inserts videos at original duration
   - Repeats sequence for looping
3. **Export**: Uses `AVAssetExportSession` with highest quality preset
4. **Save**: Stores to Camera Roll via `PHPhotoLibrary`

## Troubleshooting

### Photos Not Appearing
- Make sure you granted photo library access
- Try restarting the app
- Check Settings > Privacy > Photos

### Video Creation Fails
- Ensure you have enough storage space
- Try with fewer items
- Check that videos aren't corrupted

### Share Not Working
- Make sure video creation completed
- Check that file exists in Photos app
- Try creating a new video

## Limitations

- No per-item timing adjustments
- No video trimming/editing
- No custom music/audio overlay
- No transition style options
- Single font/color for intro text
- Loop creates larger files (not true looping)

## Future Enhancements

Potential improvements for future versions:
- Custom background music
- More transition effects
- Theme templates
- Ken Burns effect on photos
- Per-item duration control
- Video trimming
- True video looping (without file duplication)

## License

This project is provided as-is for personal use. Modify as needed.

## Support

For issues or questions, refer to the code comments or iOS documentation for:
- [PHPickerViewController](https://developer.apple.com/documentation/photokit/phpickerviewcontroller)
- [AVFoundation](https://developer.apple.com/documentation/avfoundation)
- [SwiftUI](https://developer.apple.com/documentation/swiftui)
